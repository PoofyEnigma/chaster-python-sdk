import datetime
import time

import requests

import src.chaster.api as api
import src.chaster.lock as lock
import src.chaster.extensions as extensions
import unittest
import uuid
import logging
import os
from dateutil.tz import tzutc

chaster_api = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'), user_agent='PythonSDKDeveloplment/1.0')
chaster_api_lockee = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN_II'), user_agent='PythonSDKDeveloplment/1.0')


class ApiTestCases(unittest.TestCase):

    def out_test(self, response, data):
        time.sleep(0)

    @unittest.SkipTest
    def test_request_hook(self):
        count = 0

        def func_count(response: requests.models.Response, *args, **kwargs):
            nonlocal count
            count += 1

        chaster_api_temp = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'),
                                          user_agent='PythonSDKDeveloplment/1.0', request_hook=func_count)
        chaster_api_temp.get_user_shared_locks()
        self.assertEqual(count, 1)

    @unittest.SkipTest
    def test_request_hooks(self):
        count = 0

        def func_count(response: requests.models.Response, *args, **kwargs):
            nonlocal count
            count += 1

        chaster_api_temp = api.ChasterAPI(os.environ.get('CHASTER_BEARER_TOKEN'),
                                          user_agent='PythonSDKDeveloplment/1.0', request_hook=[func_count, func_count])
        chaster_api_temp.get_user_shared_locks()
        self.assertEqual(count, 2)

    """
    Shared Locks
    """

    @unittest.SkipTest
    def test_get_shared_locks_active(self):
        response, data = chaster_api.get_user_shared_locks()
        self.out_test(response, data)
        assert response.status_code == 200

    @unittest.SkipTest
    def test_get_locks(self):
        response, data = chaster_api.get_user_locks()
        self.out_test(response, data)
        assert response.status_code == 200

    @unittest.SkipTest
    def test_create_get_update_get_archive_shared_lock(self):
        csl = lock.CreateSharedLock()
        csl.minDuration = 3600
        csl.maxDuration = 7200
        csl.maxLimitDuration = None
        csl.minDate = datetime.datetime.now()
        csl.maxDate = datetime.datetime.now() + datetime.timedelta(days=7)
        csl.maxLimitDate = None
        csl.displayRemainingTime = True
        csl.limitLockTime = False
        csl.maxLockedUsers = None
        csl.isPublic = False
        csl.password = ''
        csl.requireContact = False
        csl.name = uuid.uuid4().hex
        csl.description = 'Test'
        csl.photoId = ''
        csl.hideTimeLogs = False
        csl.isFindom = False
        response, lock_id = chaster_api.create_shared_lock(csl)

        ho = extensions.ShareLinks()
        ho.config.limitToLoggedUsers = False
        ext = extensions.Extensions()
        ext.extensions.append(ho)
        response = chaster_api.put_shared_lock_extensions(lock_id, ext)
        self.assertEqual(response.status_code, 200)
        response, data = chaster_api.get_shared_lock_details(lock_id)
        self.assertFalse(data.hideTimeLogs)
        self.assertEqual(1, len(data.extensions))
        csl.hideTimeLogs = True
        _ = chaster_api.update_shared_lock(lock_id, csl)
        response, data = chaster_api.get_shared_lock_details(lock_id)
        self.assertTrue(data.hideTimeLogs)
        _ = chaster_api.archive_shared_lock(lock_id)

    @unittest.SkipTest
    def test_favortie_check_remove(self):
        id = '659c6b549e2355d6c5e8dd55'
        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data)

        response = chaster_api.favorite(id)
        self.assertEqual(response.status_code, 200)

        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data)

        response = chaster_api.remove_favorite(id)
        self.assertEqual(response.status_code, 200)

        response, data = chaster_api.check_if_favorited(id)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(data)

    @unittest.SkipTest
    def test_get_favorited_shared_locks(self):
        response, data = chaster_api.get_favorite_shared_locks()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(len(data.results) > 0)

    """
    Locks
    """

    @unittest.SkipTest
    def test_get_locks_and_details(self):
        response, locks = chaster_api.get_user_locks('archived')
        self.assertEqual(response.status_code, 200)

        response, profile = chaster_api.get_user_profile()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(locks[0].user._id, profile._id)

        response, lock = chaster_api.get_lock_details(locks[0]._id)
        self.assertEqual(response.status_code, 200)

    @unittest.SkipTest
    def test_update_lock_time(self):
        response, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)

        response, locks = chaster_api_lockee.get_user_locks()
        lock_before = locks[0]

        _ = chaster_api.set_freeze(lock_id, True)
        _ = chaster_api_lockee.update_lock_duration(lock_id, 10000)

        response, locks = chaster_api_lockee.get_user_locks()
        lock_after = locks[0]
        self.assertFalse(lock_before.isFrozen)
        self.assertGreater(lock_after.endDate, lock_before.endDate)
        self.assertTrue(lock_after.isFrozen)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_set_keyholder_as_trusted(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.LockInfo()
        l.isTestLock = False
        l.combinationId = combination
        l.password = 'puppy'
        _, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)

        response = chaster_api.update_lock_settings(lock_id, False, True)
        self.assertEqual(response.status_code, 204)
        response = chaster_api_lockee.trust_keyholder(lock_id)
        self.assertEqual(response.status_code, 204)
        max_limit_date = datetime.datetime.now(tz=tzutc()) + datetime.timedelta(days=30)
        response = chaster_api_lockee.set_max_limit_date(lock_id,
                                                         max_limit_date, False)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.find_locked_users()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_before = locked_users.locks[0]
        self.assertTrue(lock_before.trusted)
        # self.assertEqual(lock_before.maxLimitDate, max_limit_date)
        self.assertFalse(lock_before.displayRemainingTime)
        self.assertTrue(lock_before.hideTimeLogs)

        max_limit_date = datetime.datetime.now(tz=tzutc()) + datetime.timedelta(days=40)
        response = chaster_api_lockee.set_max_limit_date(lock_id, max_limit_date, True)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.find_locked_users()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_after = locked_users.locks[0]
        self.assertIsNone(lock_after.maxLimitDate)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)
        response = chaster_api_lockee.set_as_test_lock(lock_id)
        self.assertEqual(response.status_code, 200)

    """
    Triggers
    """

    def prep_lock(self, extension):
        _, combination = chaster_api_lockee.create_combination_code('1234')
        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination
        _, lock_data = chaster_api_lockee.create_personal_lock(l)
        response, user = chaster_api.get_user_profile()
        response = chaster_api_lockee.create_keyholding_offer(lock_data, user.username)
        response, offers = chaster_api.get_keyholding_offers_from_wearers()
        response = chaster_api.resolve_keyholding_offer(offers[0]._id, True)
        response = chaster_api_lockee.trust_keyholder(lock_data)

        response = chaster_api.edit_extensions(lock_data, extension)
        self.assertEqual(response.status_code, 201)
        _, locks = chaster_api_lockee.get_user_locks()
        return locks

    @unittest.SkipTest
    def test_share_link(self):
        eh = extensions.ExtensionsHandler()
        ho = extensions.ShareLinks()
        ho.config.limitToLoggedUsers = False
        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()

        locks = self.prep_lock(e)
        lock_id = locks[0]._id
        _, url = chaster_api.get_share_link_vote_url(lock_id, locks[0].extensions[0]._id)
        self.assertIsNotNone(url)

        _, slvr = chaster_api.vote_in_share_links(lock_id, locks[0].extensions[0]._id, 'add',
                                                  url[len('https://chaster.app/sessions/'):])
        self.assertIsNotNone(slvr)

        _, info = chaster_api_lockee.get_share_link_vote_info(lock_id, locks[0].extensions[0]._id)
        self.assertIsNotNone(info)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_pillory(self):
        eh = extensions.ExtensionsHandler()
        ho = extensions.Pillory()
        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        locks = self.prep_lock(e)
        lock_id = locks[0]._id

        response = chaster_api.place_user_into_pillory(lock_id, locks[0].extensions[0]._id, 'getting caught', 3600)
        self.assertEqual(response.status_code, 201)

        _, info = chaster_api.get_current_pillory_info(lock_id, locks[0].extensions[0]._id)
        self.assertIsNotNone(info)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_roll_dice_wof_guess_timer(self):
        dice = extensions.Dice()
        wof = extensions.WheelOfFortune()
        wofs = extensions.WheelOfFortuneSegment()
        wofs.type = 'add-time'
        wofs.duration = 2600
        wof.config.segments.append(wofs)
        wofs = extensions.WheelOfFortuneSegment()
        wofs.type = 'add-time'
        wofs.duration = 3600
        wof.config.segments.append(wofs)
        gtt = extensions.GuessTheTimer()

        eh = extensions.ExtensionsHandler()
        eh.add(dice)
        eh.add(wof)
        eh.add(gtt)

        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        locks = self.prep_lock(e)
        lock_id = locks[0]._id

        eh = extensions.ExtensionsHandler()
        eh.load_defined(locks[0].extensions)

        _, drr = chaster_api_lockee.roll_dice(lock_id, eh.dice[0]._id)
        self.assertIsNotNone(drr)

        _, wofr = chaster_api_lockee.spin_wheel_of_fortune(lock_id, eh.wheel_of_fortunes[0]._id)
        self.assertIsNotNone(wofr)

        _, gttr = chaster_api_lockee.trigger_guess_the_timer(lock_id, eh.guess_timers[0]._id)
        self.assertIsNotNone(gttr)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_tasks(self):
        t1 = extensions.Task()
        t1.task = 'ride dildo 15 min'
        t2 = extensions.Task()
        t2.task = 'beg kh for more time'
        t3 = extensions.Task()
        t3.task = 'butt plug 60 min'

        eh = extensions.ExtensionsHandler()
        ho = extensions.Tasks()
        ho.config.tasks.append(t1)
        ho.config.tasks.append(t2)
        ho.config.tasks.append(t3)
        ho.mode = extensions.mode_unlimited

        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        locks = self.prep_lock(e)
        lock_id = locks[0]._id

        response = chaster_api_lockee.request_a_random_task(lock_id, locks[0].extensions[0]._id)
        self.assertEqual(response.status_code, 201)

        response = chaster_api_lockee.mark_task_done(lock_id, locks[0].extensions[0]._id, True)
        self.assertEqual(response.status_code, 201)

        response = chaster_api_lockee.assign_task(lock_id, locks[0].extensions[0]._id,
                                                  locks[0].extensions[0].config.tasks[1])
        self.assertEqual(response.status_code, 201)

        response = chaster_api_lockee.mark_task_done(lock_id, locks[0].extensions[0]._id, True)
        self.assertEqual(response.status_code, 201)

        response = chaster_api_lockee.community_vote_next_task(lock_id, locks[0].extensions[0]._id, 3600)
        self.assertEqual(response.status_code, 201)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_unlock_for_hygiene(self):
        ho = extensions.HygieneOpening()
        ho.regularity = 1

        eh = extensions.ExtensionsHandler()
        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        locks = self.prep_lock(e)
        lock_id = locks[0]._id

        response = chaster_api_lockee.unlock_for_hygiene(lock_id, locks[0].extensions[0]._id, True)
        self.assertEqual(response.status_code, 201)

        _, lock_combo = chaster_api_lockee.get_temporary_opening_combination(lock_id)
        self.assertIsNotNone(lock_combo)

        _, combination = chaster_api_lockee.create_combination_code('1234')

        response = chaster_api_lockee.set_temporary_opening_new_combination(lock_id, combination)
        self.assertEqual(response.status_code, 201)

        _, history = chaster_api_lockee.get_lock_history(lock_id)
        print(history)

        _, combo = chaster_api_lockee.get_temporary_opening_combination_from_action_log(history.results[1]._id, lock_id)
        self.assertIsNotNone(combo)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_trigger_new_verification(self):
        vp = extensions.VerificationPicture()
        vp.regularity = 1
        vp.config.visibility = 'keyholder'
        vp.config.peerVerification.enabled = False

        eh = extensions.ExtensionsHandler()
        eh.add(vp)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        locks = self.prep_lock(e)
        lock_id = locks[0]._id

        response = chaster_api.trigger_new_verification(lock_id, locks[0].extensions[0]._id)
        self.assertEqual(response.status_code, 201)

        response = chaster_api_lockee.submit_verification(lock_id, './tests/test.png',
                                                          'test.png',
                                                          'image/png')
        self.assertEqual(response.status_code, 201)

        _, history = chaster_api_lockee.get_verification_history(lock_id)
        self.assertIsNotNone(history)

        _ = chaster_api.unlock(lock_id)
        _ = chaster_api_lockee.archive_lock(lock_id)

    """
    Lock Creation
    """

    @unittest.SkipTest
    def test_create_personal_lock(self):
        response, combination = chaster_api_lockee.create_combination_code('1234')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination, '')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination
        response, lock_data = chaster_api_lockee.create_personal_lock(l)
        self.assertIsNotNone(lock_data)
        self.assertNotEqual(lock_data, '')
        time.sleep(l.maxDuration)
        response = chaster_api_lockee.unlock(lock_data)
        self.assertEqual(response.status_code, 204)

        response = chaster_api_lockee.archive_lock(lock_data)
        self.assertEqual(response.status_code, 204)

        response, lock_data = chaster_api_lockee.get_user_locks()
        self.assertIsNotNone(lock_data)
        self.assertEqual(len(lock_data), 0)
        self.assertEqual(response.status_code, 200)

    @unittest.SkipTest
    def test_add_extensions(self):
        response, combination = chaster_api_lockee.upload_combination_image('./tests/test.png',
                                                                            'test.png',
                                                                            'image/png')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination, '')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)
        self.assertIsNotNone(lock_id)
        self.assertNotEqual(lock_id, '')

        response = chaster_api_lockee.trust_keyholder(lock_id)
        self.assertEqual(response.status_code, 204)

        eh = extensions.ExtensionsHandler()
        ho = extensions.HygieneOpening()
        eh.add(ho)
        e = extensions.Extensions()
        e.extensions = eh.generate_array()
        response = chaster_api.edit_extensions(lock_id, e)
        self.assertEqual(response.status_code, 201)

        response, locked_users = chaster_api.find_locked_users()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 1)
        lock_after = locked_users.locks[0]

        response, extensions_info = chaster_api.get_lock_extension_information(lock_id,
                                                                               lock_after.extensions[0]._id)
        self.assertIsNotNone(extensions_info)
        self.assertIsNotNone(extensions_info.extension)

        _ = chaster_api.unlock(lock_id)

        response, lock_combo = chaster_api_lockee.get_lock_combination(lock_id)
        self.assertIsNotNone(lock_combo)

        response, lock_history = chaster_api_lockee.get_lock_history(lock_id)
        self.assertIsNotNone(lock_history)

        _ = chaster_api_lockee.archive_lock(lock_id)

    @unittest.SkipTest
    def test_create_lock_from_shared_lock(self):
        response, combination = chaster_api_lockee.upload_combination_image('./tests/test.png',
                                                                            'test.png',
                                                                            'image/png')
        self.assertIsNotNone(combination)
        self.assertNotEqual(combination, '')

        l = lock.LockInfo()
        l.isTestLock = True
        l.combinationId = combination
        l.password = 'puppy'
        response, lock_id = chaster_api_lockee.create_lock_from_shared_lock('64e69feb2f626eb789dafd6e', l)
        self.assertIsNotNone(lock_id)
        self.assertNotEqual(lock_id, '')

        response = chaster_api.unlock(lock_id)
        self.assertEqual(response.status_code, 204)

        response = chaster_api.archive_lock_as_keyholder(lock_id)
        self.assertEqual(response.status_code, 204)

        response, locked_users = chaster_api.find_locked_users()
        self.assertIsNotNone(locked_users)
        self.assertEqual(len(locked_users.locks), 0)

        response = chaster_api_lockee.archive_lock(lock_id)
        self.assertEqual(response.status_code, 204)

        response, lock_data = chaster_api_lockee.get_user_locks()
        self.assertIsNotNone(lock_data)
        self.assertEqual(len(lock_data), 0)
        self.assertEqual(response.status_code, 200)

    """
    Profile
    """

    @unittest.SkipTest
    def test_get_your_profile(self):
        response, profile = chaster_api.get_user_profile()
        self.assertIsNotNone(profile)

        response, profile = chaster_api.update_profile()
        self.assertIsNotNone(profile)

        response, badges = chaster_api.get_badges()
        self.assertIsNotNone(badges)

        response, detailed_user = chaster_api.find_profile_detailed('PupHimbo')
        self.assertIsNotNone(detailed_user)

        response, user = chaster_api.find_profile('PupHimbo')
        self.assertIsNotNone(user)

        response, profile = chaster_api.get_profile(profile._id)
        self.assertIsNotNone(profile)

        response, locks = chaster_api.get_user_public_locks(profile._id)
        self.assertIsNotNone(locks)

    """
    Files
    """

    @unittest.SkipTest
    def test_upload_and_find_file(self):
        response, file_info = chaster_api.upload_file('./tests/test.png',
                                                      'test.png',
                                                      'image/png')
        self.assertIsNotNone(file_info)

    """
    Combinations
    """

    """
    Extensions
    """

    @unittest.SkipTest
    def test_get_all_known_extensions(self):
        response, known_extensions = chaster_api.get_all_known_extensions()
        self.assertIsNotNone(known_extensions)

    """
    Session Offer
    """

    @unittest.SkipTest
    def test_accept_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_user_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_sent_keyholding_offers(lock_data)
        self.assertIsNotNone(user_offers)
        self.assertGreaterEqual(len(user_offers), 1)

        response, offers = chaster_api.get_keyholding_offers_from_wearers()
        self.assertIsNotNone(offers)
        self.assertGreaterEqual(len(offers), 1)

        response = chaster_api.resolve_keyholding_offer(offers[0]._id, True)
        self.assertEqual(response.status_code, 201)

        _ = chaster_api.unlock(lock_data)
        _ = chaster_api_lockee.archive_lock(lock_data)

    @unittest.SkipTest
    def test_refuse_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_user_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_sent_keyholding_offers(lock_data)
        self.assertIsNotNone(user_offers)
        self.assertGreaterEqual(len(user_offers), 1)

        _, locks = chaster_api_lockee.get_user_locks()

        response, user_lock = chaster_api.retrieve_keyholder_request_lock_info(locks[0].offerToken)
        self.assertIsNotNone(user_lock)

        response = chaster_api.accept_keyholding_request(locks[0].offerToken)
        self.assertEqual(response.status_code, 200)

        _ = chaster_api.unlock(lock_data)
        _ = chaster_api_lockee.archive_lock(lock_data)

    @unittest.SkipTest
    def test_archive_session_offer(self):
        _, combination = chaster_api_lockee.create_combination_code('1234')

        l = lock.CreateLock()
        l.minDuration = 0
        l.maxDuration = 1
        l.isTestLock = True
        l.combinationId = combination
        _, lock_data = chaster_api_lockee.create_personal_lock(l)

        response, user = chaster_api.get_user_profile()

        response = chaster_api_lockee.create_keyholding_offer(lock_data, user.username)
        self.assertEqual(response.status_code, 201)

        response, user_offers = chaster_api_lockee.get_sent_keyholding_offers(lock_data)

        response = chaster_api_lockee.archive_keyholding_offer(user_offers[0]._id)
        self.assertEqual(response.status_code, 200)

        _ = chaster_api_lockee.unlock(lock_data)
        _ = chaster_api_lockee.archive_lock(lock_data)

    """
    Messaging
    """

    @unittest.SkipTest
    def test_conversations(self):
        response, conversations = chaster_api.get_conversations()
        self.assertIsNotNone(conversations)

        response, conversation = chaster_api.get_conversation(conversations.results[0]._id)
        self.assertIsNotNone(conversation)

        response, messages = chaster_api.get_conversation_messages(conversations.results[0]._id)
        self.assertIsNotNone(messages)

    @unittest.SkipTest
    def test_conversations_sending_messages(self):
        _, profile = chaster_api_lockee.get_user_profile()
        _, conversation = chaster_api.get_user_conversation(profile._id)
        self.assertIsNotNone(conversation)

        response, message = chaster_api.send_message(conversation._id, 'hello')
        self.assertIsNotNone(message)

        _, conversation = chaster_api.create_conversation(profile._id, 'create')
        self.assertIsNotNone(conversation)

        response = chaster_api.set_conversation_status(conversation._id, 'approved')
        self.assertEqual(response.status_code, 200)

        response = chaster_api.set_conversation_unread(conversation._id, True)
        self.assertEqual(response.status_code, 200)

    """
    Extensions - Temporary Opening
    """

    """
    Community Events
    """

    @unittest.SkipTest
    def test_community_events(self):
        _, ced = chaster_api.get_community_event_details()
        self.assertIsNotNone(ced)
        _, cec = chaster_api.get_community_event_categories()
        self.assertIsNotNone(cec)

    """
    Settings
    """

    @unittest.SkipTest
    def test_get_app_settings(self):
        _, settings = chaster_api.get_app_settings()
        self.assertIsNotNone(settings)

    """
    Users
    """

    @unittest.SkipTest
    def test_users(self):
        _, users = chaster_api.search_for_users('pup')
        self.assertIsNotNone(users)

        _, user = chaster_api.search_for_users_by_discord('1153172669559214141')
        self.assertIsNotNone(users)

    """
    Public Locks
    """

    @unittest.SkipTest
    def test_public_locks(self):
        _, details = chaster_api.find_public_shared_lock('64e69feb2f626eb789dafd6e')
        self.assertIsNotNone(details)

        response = chaster_api.generate_public_shared_lock_flyer('64e69feb2f626eb789dafd6e', './here.png')
        self.assertEqual(response.status_code, 200)

        _, page = chaster_api.search_for_public_locks(lock.SearchPublicLock())
        self.assertIsNotNone(page)

        _, data = chaster_api.find_explore_page_locks()
        self.assertIsNotNone(data)

    """
    Extensions - Verification Picture
    """


if __name__ == '__main__':
    log_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
    root_logger = logging.getLogger()
    logging.basicConfig(filename='./out.log',
                        format=log_format,
                        level=logging.DEBUG)

    stream_handler = logging.StreamHandler()
    root_logger.addHandler(stream_handler)
    stream_handler.setFormatter(logging.Formatter(log_format))
    unittest.main()
