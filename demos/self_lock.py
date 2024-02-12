# Print some data about your shared locks
import datetime
import os
import logging

from chaster import api, lock, extensions

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='self_lock_creator/1.0')

# Create a combination
_, combination = chaster_api.create_combination_code('1234')

# Create Wheel of Fortune
s1 = extensions.WheelOfFortuneSegment()
s1.type = 'add-time'
s1.duration = datetime.timedelta(hours=1).total_seconds()

s2 = extensions.WheelOfFortuneSegment()
s2.type = 'remove-time'
s2.duration = datetime.timedelta(hours=1).total_seconds()

s3 = extensions.WheelOfFortuneSegment()
s3.type = 'set-freeze'

s4 = extensions.WheelOfFortuneSegment()
s4.type = 'set-unfreeze'

s5 = extensions.WheelOfFortuneSegment()
s5.type = 'text'
s5.text = 'do a thing'

wof = extensions.WheelOfFortune()
wof.config = extensions.WheelOfFortuneConfig()
wof.regularity = datetime.timedelta(hours=1).total_seconds()
wof.config.segments.append(s1)
wof.config.segments.append(s2)
wof.config.segments.append(s3)
wof.config.segments.append(s4)
wof.config.segments.append(s5)

# Create Verification Requirement extension
verification = extensions.VerificationPicture()
verification.config = extensions.VerificationPictureConfig()
verification.regularity = int(datetime.timedelta(days=1).total_seconds())
verification.config.visibility = 'all'
verification.config.peerVerification = extensions.PeerVerification()
verification.config.peerVerification.enabled = True
pillory_punishment = extensions.PunishmentPillory(datetime.timedelta(hours=1).total_seconds())
verification.config.peerVerification.punishments.append(pillory_punishment)

# Create Dice Extension
dice = extensions.Dice()
dice.config = extensions.DiceConfig()
dice.regularity = datetime.timedelta(hours=1).total_seconds()
dice.config.multiplier = datetime.timedelta(hours=1).total_seconds()

# Create Hygiene Opening Extension
hygiene_opening = extensions.HygieneOpening()
hygiene_opening.config = extensions.HygieneOpeningConfig()
hygiene_opening.regularity = datetime.timedelta(days=3).total_seconds()
hygiene_opening.config.openingTime = datetime.timedelta(minutes=15).total_seconds()
hygiene_opening.config.penaltyTime = datetime.timedelta(days=12).total_seconds()
hygiene_opening.config.allowOnlyKeyholderToOpen = False

# Create Pillory Extension
pillory = extensions.Pillory()
pillory.config = extensions.PilloryConfig()
pillory.config.timeToAdd = datetime.timedelta(hours=1).total_seconds()
pillory.config.limitToLoggedUsers = True

# Create Lock
create_lock = lock.CreateLock()
create_lock.minDuration = datetime.timedelta(hours=1).total_seconds()
create_lock.maxDuration = datetime.timedelta(hours=6).total_seconds()
create_lock.maxLimitDuration = datetime.timedelta(days=1).total_seconds()
create_lock.displayRemainingTime = True
create_lock.limitLockTime = True
create_lock.combinationId = combination
create_lock.extensions = []
create_lock.allowSessionOffer = False
create_lock.isTestLock = False
create_lock.hideTimeLogs = False

# Add extensions to the lock
create_lock.extensions.append(wof)
create_lock.extensions.append(verification)
create_lock.extensions.append(dice)
create_lock.extensions.append(hygiene_opening)
create_lock.extensions.append(pillory)

_, lock_id_data = chaster_api.create_personal_lock(create_lock)
_, lock = chaster_api.get_lock_details(lock_id_data)

eh = extensions.ExtensionsHandler()
eh.load_defined(lock.extensions)

chaster_api.roll_dice(lock._id, eh.dice[0]._id)
chaster_api.spin_wheel_of_fortune(lock._id, eh.wheel_of_fortunes[0]._id)
