import datetime
import json
import unittest
from src.chaster import conversation, extensions, lock, triggers, user
from . import response_examples
from types import SimpleNamespace


class DTOsTest(unittest.TestCase):

    def compare_obj_params(self, obj, dictionary: dict, known_additional_obj_params: set[str] = set(),
                           known_additional_dict_params: set[str] = set()):
        for entry in obj.__dict__:
            if entry in known_additional_obj_params:
                continue
            self.assertTrue(entry in dictionary, msg=f'{entry} is not present in source dictionary')
        for entry in dictionary:
            if entry in known_additional_dict_params:
                continue
            self.assertTrue(entry in obj.__dict__, msg=f'{entry} is not present in dto')
        obj.update(json.loads(json.dumps(dictionary), object_hook=lambda d: SimpleNamespace(**d)))
        self.maxDiff = None
        self.assertEqual(obj.dump(), dictionary)

    """
    Shared Locks
    """

    def test_shared_lock_params(self):
        base = json.loads(response_examples.shared_lock)
        cmp = lock.SharedLock()
        self.compare_obj_params(cmp, base, known_additional_obj_params={'joinRules'})

    def test_create_shared_lock_params(self):
        base = json.loads(response_examples.create_shared_lock)
        cmp = lock.CreateSharedLock()
        self.compare_obj_params(cmp, base)

    def test_pageinatedSharedLockList_params(self):
        base = json.loads(response_examples.get_favorited_share_locks)
        cmp = lock.PaginatedSharedLockList()
        self.compare_obj_params(cmp, base)

    """
    Locks
    """

    def test_lock_params(self):
        base = json.loads(response_examples.user_lock)
        cmp = lock.Lock()
        self.compare_obj_params(cmp, base)

    def test_lock_combinations_params(self):
        base = json.loads(response_examples.lock_combination)
        cmp = user.LockCombination()
        self.compare_obj_params(cmp, base)

    def test_PageinatedLockHistory_params(self):
        base = json.loads(response_examples.lock_history)
        cmp = lock.PaginatedLockHistory()
        self.compare_obj_params(cmp, base)
        cmp = lock.ActionLog()
        self.compare_obj_params(cmp, base['results'][0])

    @unittest.SkipTest
    def test_ExtensionInformation_params(self):
        base = json.loads(response_examples.lock_with_extension)
        base['lock']['extensions'] = []
        base['extension'] = {}
        cmp = lock.ExtensionInformation()
        self.compare_obj_params(cmp, base)

    """
    Triggers
    """

    def test_ShareLinkGetInfoResponse_params(self):
        base = json.loads(response_examples.share_link_info_response)
        cmp = triggers.ShareLinkInfoResponse()
        self.compare_obj_params(cmp, base)

    def test_PilloryVotes_params(self):
        base = json.loads(response_examples.pillory_info)
        cmp = triggers.PilloryVotes()
        self.compare_obj_params(cmp, base)

    def test_DiceRollResult_params(self):
        base = json.loads(response_examples.dice_roll_result)
        cmp = triggers.DiceRollResult()
        self.compare_obj_params(cmp, base)

    def test_WheelOfFortuneResult_params(self):
        base = json.loads(response_examples.wheel_of_fortune_result)
        cmp = triggers.WheelOfFortuneResult()
        self.compare_obj_params(cmp, base)

    def test_GuessTheTimerResponse_params(self):
        base = json.loads(response_examples.guess_the_timer_result)
        cmp = triggers.GuessTheTimerResponse()
        self.compare_obj_params(cmp, base)

    """
    Lock Creation
    """
    def test_Extensions_params(self):
        base = json.loads(response_examples.extensions_input)
        cmp = extensions.Extensions()
        base['extensions'] = []
        self.compare_obj_params(cmp, base)

    def test_LockInfo_params(self):
        base = json.loads(response_examples.lock_info_input)
        cmp = lock.LockInfo()
        self.compare_obj_params(cmp, base)

    """
    profile
    """

    def test_User_params(self):
        base = json.loads(response_examples.user_profile)
        cmp = user.User()
        self.compare_obj_params(cmp, base)

    def test_DetailedUser_params(self):
        base = json.loads(response_examples.detailed_user_profile)
        base['sharedLocks'] = []
        cmp = user.DetailedUser()
        self.compare_obj_params(cmp, base)

    def test_Badges_params(self):
        base = json.loads(response_examples.user_badges)
        cmp = user.Badges()
        self.compare_obj_params(cmp, base)

    def test_AuthProfile_params(self):
        base = json.loads(response_examples.user_auth_profile)
        cmp = user.AuthProfile()
        self.compare_obj_params(cmp, base)

    """
    Files
    """

    """
    Combinations
    """

    """
    Extensions
    """

    def test_KnownExtension_params(self):
        base = json.loads(response_examples.all_known_extensions)
        base[10]['defaultConfig'] = {}
        cmp = extensions.KnownExtension()
        self.compare_obj_params(cmp, base[10])

    """
    Session Offer
    """

    def test_KeyholderOfferEntry_params(self):
        base = json.loads(response_examples.keyholder_offers)
        cmp = user.KeyholderOfferEntry()
        self.compare_obj_params(cmp, base[0])

    """
    Messaging
    """

    def test_Conversations_params(self):
        base = json.loads(response_examples.conversations_list)
        cmp = conversation.Conversations()
        self.compare_obj_params(cmp, base)

    def test_Conversation_params(self):
        base = json.loads(response_examples.conversation)
        cmp = conversation.Conversation()
        self.compare_obj_params(cmp, base)

    def test_Message_params(self):
        base = json.loads(response_examples.conversation_messasge)
        cmp = conversation.Message()
        self.compare_obj_params(cmp, base)

    def test_ConversationMessages_params(self):
        base = json.loads(response_examples.conversation_messages)
        cmp = conversation.ConversationMessages()
        self.compare_obj_params(cmp, base)

    """
    Extensions - Temporary Opening
    """

    def test_LockCombination_params(self):
        base = json.loads(response_examples.lock_combination)
        cmp = user.LockCombination()
        self.compare_obj_params(cmp, base)

    """
    Community Events
    """

    def test_CommunityEventCategory_params(self):
        base = json.loads(response_examples.community_event_category_list)
        base[0]['hidden'] = False
        cmp = user.CommunityEventCategory()
        self.compare_obj_params(cmp, base[0])

    @unittest.SkipTest
    def test_CommunityEventDetails_params(self):
        base = json.loads(response_examples.community_event_details)
        cmp = user.CommunityEventDetails()
        self.compare_obj_params(cmp, base)

    """
    Settings
    """

    """
    Users
    """

    """
    Keyholder
    """

    def test_LockedUsers_params(self):
        base = json.loads(response_examples.locked_users)
        cmp = lock.LockedUsers()
        self.compare_obj_params(cmp, base)

    """
    Public Locks
    """

    def test_PublicSharedLockInfo_params(self):
        base = json.loads(response_examples.public_shared_lock)
        base['locks'] = []
        base['createdAt'] = None
        base['updatedAt'] = None
        base['unlockedAt'] = None
        base['deletedAt'] = None
        cmp = lock.PublicSharedLockInfo()
        self.compare_obj_params(cmp, base)

    def test_PageinatedSharedLockList_params(self):
        base = json.loads(response_examples.search_public_locks)
        base['lastId'] = ''
        cmp = lock.PaginatedSharedLockList()
        self.compare_obj_params(cmp, base)

    def test_ExplorePageLock_params(self):
        base = json.loads(response_examples.explore_page_locks)
        base[0]['locks'] = []
        cmp = lock.ExplorePageLock()
        self.compare_obj_params(cmp, base[0])

    def test_SearchPublicLock_params(self):
        base = json.loads(response_examples.search_for_public_locks)
        cmp = lock.SearchPublicLock()
        self.compare_obj_params(cmp, base)

    """
    Extensions - Verification Picture
    """

    def test_VerificationPhotoHistory_params(self):
        base = json.loads(response_examples.verification_history)
        cmp = lock.VerificationPhotoHistory()
        self.compare_obj_params(cmp, base[0])

    def test_AppSettings_params(self):
        base = json.loads(response_examples.app_settings)
        cmp = user.AppSettings()
        self.compare_obj_params(cmp, base)

    """
    Extension Objects
    """
