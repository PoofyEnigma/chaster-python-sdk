import datetime
import json
import unittest
from src.api import conversation, lock, user, triggers, extensions
from types import SimpleNamespace
from . import response_examples


class DTOsTest(unittest.TestCase):

    def compare_obj_params(self, obj, dictionary: dict):
        for entry in obj.__dict__:
            self.assertTrue(entry in dictionary, msg=f'{entry} is not present in source dictionary')
        for entry in dictionary:
            self.assertTrue(entry in obj.__dict__)

    """
    Shared Locks
    """

    def test_response_id_params(self):
        base = json.loads(response_examples.created_shared_lock)
        cmp = lock.IdResponse()
        self.compare_obj_params(cmp, base)

    def test_shared_lock_params(self):
        base = json.loads(response_examples.shared_lock)
        cmp = lock.SharedLock()
        self.compare_obj_params(cmp, base)

    def test_create_shared_lock_params(self):
        base = json.loads(response_examples.create_shared_lock)
        cmp = lock.CreateSharedLock()
        self.compare_obj_params(cmp, base)

    def test_pageinatedSharedLockList_params(self):
        base = json.loads(response_examples.get_favorited_share_locks)
        cmp = lock.PageinatedSharedLockList()
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
        cmp = lock.PageinatedLockHistory()
        self.compare_obj_params(cmp, base)
        cmp = lock.ActionLog()
        self.compare_obj_params(cmp, base['results'][0])

    def test_ExtensionInformation_params(self):
        base = json.loads(response_examples.lock_with_extension)
        cmp = lock.ExtensionInformation()
        self.compare_obj_params(cmp, base)

    """
    Triggers
    """

    def test_ShareLinksVote_params(self):
        base = json.loads(response_examples.share_link_vote_ack)
        cmp = triggers.ShareLinksVoteReturn()
        self.compare_obj_params(cmp, base)

    def test_ShareLinkUrlResponse_params(self):
        base = json.loads(response_examples.share_link_url_response)
        cmp = triggers.ShareLinkUrlResponse()
        self.compare_obj_params(cmp, base)

    def test_ShareLinkGetInfoResponse_params(self):
        base = json.loads(response_examples.share_link_info_response)
        cmp = triggers.ShareLinkGetInfoResponse()
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

    def test_LockId_params(self):
        base = json.loads(response_examples.lock_id_response)
        cmp = lock.LockId()
        self.compare_obj_params(cmp, base)

    def test_Extensions_params(self):
        base = json.loads(response_examples.extensions_input)
        cmp = extensions.Extensions()
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

    # def upload_file(self) -> tuple[requests.models.Response, user.FileToken]:

    # def find_file(self, file_key) -> tuple[requests.models.Response, user.FileUrl]:

    """
    Combinations
    """

    # def upload_combination_image(self) -> tuple[requests.models.Response, lock.Combination]:

    # def create_combination_code(self, code: str) -> tuple[requests.models.Response, lock.Combination]:

    """
    Extensions
    """
    def test_AuthProfile_params(self):
        base = json.loads(response_examples.all_known_extensions)
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
    """

    def test_base_conversation_message_has_correct_params(self):
        base = json.loads(_conversation_messages)
        cmp = conversation.ConversationMessages()
        self.compare_obj_params(cmp, base)


_conversation_messages = """
{
  "count": 31,
  "hasMore": false,
  "results": [
    {
      "_id": "65963d6516512461ec4609df",
      "type": "message",
      "message": "#PatrolBot#Welcome back to the Island! Your account has been marked as a TESTER account, so you can access to special fun new features! Please share any feedback on the testers channel at https://discord.com/invite/pfjPV5VXKT !New feature link: http://209.97.129.195/pb?uuid=7192cae0-90bb-42ad-bf85-965d3414b1bb [Please note that some browsers may mark this site as unsafe until I set up the server properly for guests!]",
      "createdAt": "2024-01-04T05:08:53.905Z",
      "updatedAt": "2024-01-04T05:08:53.905Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "65813614ca4b0cb9ac7f1ef6",
      "type": "message",
      "message": "#PatrolBot#Welcome back to the Island! Your account has been marked as a TESTER account, so you can access to special fun new features! Please contribute to the testers channel with your thoughts and feedback at https://discord.com/invite/pfjPV5VXKT !http://209.97.129.195/pb?uuid=a9d1e92a-5dec-4458-a40e-4aaa8ed858ff [Please note that some browsers may mark this site as unsafe until I set up the server properly for guests!]",
      "createdAt": "2023-12-19T06:20:04.029Z",
      "updatedAt": "2023-12-19T06:20:04.029Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f99cef3ce584d386829a4",
      "type": "message",
      "message": "#PatrolBot#The hairs on the back of your neck stand up on end. You instantly get the feeling that you are NOT SAFE. Your eyes dart and scan your surroundings; a tree, a bird, a cloud - nothing. Your heart races. The air around you falls silent just for just a few moments before - **A cacophonous roar, a blinding red light**, and then... nothing.You have been caught by PatrolBot - 12 hours have been added to your timer!",
      "createdAt": "2023-12-18T01:01:02.867Z",
      "updatedAt": "2023-12-18T01:01:02.867Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f917c5a6c90625ad6c69d",
      "type": "message",
      "message": "#PatrolBot#You hear a faint pulsing in the distance. Is PatrolBot...recharging? The air around you is oddly quiet, you try to get up, but your body is still unresponsive.PatrolBot is recharging; all players are safe for a little longer. But it won't be for long...Be careful - PatrolBot will trap you for 24 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-12-18T00:25:32.968Z",
      "updatedAt": "2023-12-18T00:25:32.968Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f85a5f3ce584d38665f39",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a beacon to MARK all players!You have now been MARKED. Your penalty if PatrolBot traps you will be doubled!Be careful - PatrolBot will trap you for 24 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-12-17T23:35:01.297Z",
      "updatedAt": "2023-12-17T23:35:01.297Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f809955e3a6fdf3cc4291",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up by the CLIFFS. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.com/invite/pfjPV5VXKT !Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture)",
      "createdAt": "2023-12-17T23:13:29.476Z",
      "updatedAt": "2023-12-17T23:13:29.476Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f7fc85317f5c30195c003",
      "type": "message",
      "message": "#PatrolBot#You finally manage to convince your body to move, hauling yourself to your feet and shuffling as quickly as you can towards a nearby rowboat. You're still none the wiser as to how you got here, but there will be time for that later. As you pull away from the shore, you can *feel* PatrolBot watching you from somewhere on the Island.In time, you may forget your short time on the Island. But something tells you that it won't forget you...You have successfully escaped PatrolBot this time around. Your game score has been increased by 1; the next time you visit the Island, your penalty will be higher, and the risk of capture even greater.Thanks for playing, and see you again soon on the Island...",
      "createdAt": "2023-12-17T23:10:00.413Z",
      "updatedAt": "2023-12-17T23:10:00.413Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f7d1c5a6c90625ad4b798",
      "type": "message",
      "message": "#PatrolBot#You are startled by a sudden, deafening boom, which thunders across the island in an instant. In the distance, a single pulse of dazzling red light momentarily lights up the sky. You instinctively shield your eyes with your palm.And then...silence. Your pulse returns to its normal patter. What on earth was THAT?Be careful - PatrolBot will trap you for 6 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture)",
      "createdAt": "2023-12-17T22:58:36.867Z",
      "updatedAt": "2023-12-17T22:58:36.867Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f741fc7589934687e54a0",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a drone to SCAN for players, and will next move to the area with the most players!WOODS: 4 playersTOWN: 1 playersCLIFFS: 4 playersPatrolBot's next move will be to the WOODSBe careful - PatrolBot will trap you for 6 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture)",
      "createdAt": "2023-12-17T22:20:15.179Z",
      "updatedAt": "2023-12-17T22:20:15.179Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f6878c7175481a8da7f9b",
      "type": "message",
      "message": "#PatrolBot#You are startled by a sudden, deafening boom, which thunders across the island in an instant. In the distance, a single pulse of dazzling red light momentarily lights up the sky. You instinctively shield your eyes with your palm.And then...silence. Your pulse returns to its normal patter. What on earth was THAT?Be careful - PatrolBot will trap you for 6 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture)",
      "createdAt": "2023-12-17T21:30:32.864Z",
      "updatedAt": "2023-12-17T21:30:32.864Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "657f63a755e3a6fdf3c87e1d",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up in the WOODS. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.com/invite/pfjPV5VXKT !Be careful - PatrolBot will trap you for 6 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture)",
      "createdAt": "2023-12-17T21:09:59.973Z",
      "updatedAt": "2023-12-17T21:09:59.973Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e82789ba41add684cdb1c7",
      "type": "message",
      "message": "Your bot game locks were really fun. I hope that and your discord server comes back.",
      "createdAt": "2023-08-25T04:01:13.959Z",
      "updatedAt": "2023-08-25T04:01:13.959Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "64e5b481b533a5ccfe61567f",
      "attachments": []
    },
    {
      "_id": "64e655dd2f626eb789cfa750",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has moved to the TOWN, and trapped 2 players:  - PupPoofy (trapped for 24 hours) - Sim_Sub_Boy (trapped for 24 hours)You have been found and trapped by PatrolBot! 24 hours have been added to your timer! You should have been faster...",
      "createdAt": "2023-08-23T18:54:21.424Z",
      "updatedAt": "2023-08-23T18:54:21.424Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e64c7b17af93c93bd62f74",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a drone to SCAN for players, and will next move to the area with the most players!LAKE: 1 playersTOWN: 2 playersBEACH: 1 playersCLIFFS: 1 playersPatrolBot's next move will be to the TOWNBe careful - PatrolBot will trap you for 24 hours if it catches you! (6 hours standard trap time x 4 game(s) without capture)",
      "createdAt": "2023-08-23T18:14:19.771Z",
      "updatedAt": "2023-08-23T18:14:19.771Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e64a9b60dc7581e94d22ea",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up in the TOWN. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.gg/34r6VdjDj !Be careful - PatrolBot will trap you for 24 hours if it catches you! (6 hours standard trap time x 4 game(s) without capture)",
      "createdAt": "2023-08-23T18:06:19.507Z",
      "updatedAt": "2023-08-23T18:06:19.507Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e649abfaa9d2c6a2d74a08",
      "type": "message",
      "message": "#PatrolBot#You finally manage to convince your body to move, hauling yourself to your feet and shuffling as quickly as you can towards a nearby rowboat. You're still none the wiser as to how you got here, but there will be time for that later. As you pull away from the shore, you can *feel* PatrolBot watching you from somewhere on the Island.In time, you may forget your short time on the Island. But something tells you that it won't forget you...You have successfully escaped PatrolBot this time around. Your game score has been increased by 1; the next time you visit the Island, your penalty will be higher, and the risk of capture even greater.Thanks for playing, and see you again soon on the Island...",
      "createdAt": "2023-08-23T18:02:19.399Z",
      "updatedAt": "2023-08-23T18:02:19.399Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e6450260dc7581e94c2953",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a beacon to MARK all players!You have now been MARKED. Your penalty if PatrolBot traps you will be doubled!Be careful - PatrolBot will trap you for 36 hours if it catches you! (6 hours standard trap time x 3 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-08-23T17:42:26.732Z",
      "updatedAt": "2023-08-23T17:42:26.732Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e63df6128b2c5b77113b36",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a drone to SCAN for players, and will next move to the area with the most players!LAKE: 2 playersBEACH: 1 playersCLIFFS: 1 playersPatrolBot's next move will be to the LAKEBe careful - PatrolBot will trap you for 36 hours if it catches you! (6 hours standard trap time x 3 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-08-23T17:12:22.766Z",
      "updatedAt": "2023-08-23T17:12:22.766Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e6323b2f626eb789c9e816",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a beacon to MARK all players!You have now been MARKED. Your penalty if PatrolBot traps you will be doubled!Be careful - PatrolBot will trap you for 36 hours if it catches you! (6 hours standard trap time x 3 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-08-23T16:22:19.351Z",
      "updatedAt": "2023-08-23T16:22:19.351Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e62d8f2f626eb789c9286d",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up by the LAKE. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.gg/34r6VdjDj !Be careful - PatrolBot will trap you for 18 hours if it catches you! (6 hours standard trap time x 3 game(s) without capture)",
      "createdAt": "2023-08-23T16:02:23.781Z",
      "updatedAt": "2023-08-23T16:02:23.781Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e6260c2f626eb789c7e197",
      "type": "message",
      "message": "#PatrolBot#You finally manage to convince your body to move, hauling yourself to your feet and shuffling as quickly as you can towards a nearby rowboat. You're still none the wiser as to how you got here, but there will be time for that later. As you pull away from the shore, you can *feel* PatrolBot watching you from somewhere on the Island.In time, you may forget your short time on the Island. But something tells you that it won't forget you...You have successfully escaped PatrolBot this time around. Your game score has been increased by 1; the next time you visit the Island, your penalty will be higher, and the risk of capture even greater.Thanks for playing, and see you again soon on the Island...",
      "createdAt": "2023-08-23T15:30:20.338Z",
      "updatedAt": "2023-08-23T15:30:20.338Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e61f05a7d105554e97611f",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has moved to the TOWN, but has claimed no victims.You have evaded PatrolBot this time, but PatrolBot never sleeps. It will make its next move soon...Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture)",
      "createdAt": "2023-08-23T15:00:21.893Z",
      "updatedAt": "2023-08-23T15:00:21.893Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e61530faa9d2c6a2cec0b7",
      "type": "message",
      "message": "#PatrolBot#You hear a faint pulsing in the distance. Is PatrolBot...recharging? The air around you is oddly quiet, you try to get up, but your body is still unresponsive.PatrolBot is recharging; all players are safe for a little longer. But it won't be for long...Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture)",
      "createdAt": "2023-08-23T14:18:24.060Z",
      "updatedAt": "2023-08-23T14:18:24.060Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e60b5420632a8460674281",
      "type": "message",
      "message": "#PatrolBot#You are startled by a sudden, deafening boom, which thunders across the island in an instant. In the distance, a single pulse of dazzling red light momentarily lights up the sky. You instinctively shield your eyes with your palm.And then...silence. Your pulse returns to its normal patter. What on earth was THAT?Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture)",
      "createdAt": "2023-08-23T13:36:20.951Z",
      "updatedAt": "2023-08-23T13:36:20.951Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e609ef17af93c93bcb9b80",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up in the WOODS. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.gg/34r6VdjDj !Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 2 game(s) without capture)",
      "createdAt": "2023-08-23T13:30:23.893Z",
      "updatedAt": "2023-08-23T13:30:23.893Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e5d1374cf3cc3a0aa4aa46",
      "type": "message",
      "message": "#PatrolBot#You finally manage to convince your body to move, hauling yourself to your feet and shuffling as quickly as you can towards a nearby rowboat. You're still none the wiser as to how you got here, but there will be time for that later. As you pull away from the shore, you can *feel* PatrolBot watching you from somewhere on the Island.In time, you may forget your short time on the Island. But something tells you that it won't forget you...You have successfully escaped PatrolBot this time around. Your game score has been increased by 1; the next time you visit the Island, your penalty will be higher, and the risk of capture even greater.Thanks for playing, and see you again soon on the Island...",
      "createdAt": "2023-08-23T09:28:23.736Z",
      "updatedAt": "2023-08-23T09:28:23.736Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e5c6e3faa9d2c6a2c4b919",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has moved to the CLIFFS, but has claimed no victims.You have evaded PatrolBot this time, but PatrolBot never sleeps. It will make its next move soon...Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-08-23T08:44:19.288Z",
      "updatedAt": "2023-08-23T08:44:19.288Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e5bba32f626eb789ba069e",
      "type": "message",
      "message": "#PatrolBot#PatrolBot has used a beacon to MARK all players!You have now been MARKED. Your penalty if PatrolBot traps you will be doubled!Be careful - PatrolBot will trap you for 12 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture x 2 (you are MARKED))",
      "createdAt": "2023-08-23T07:56:19.832Z",
      "updatedAt": "2023-08-23T07:56:19.832Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e5b6494cf3cc3a0aa1bb46",
      "type": "message",
      "message": "Noted and thank you",
      "createdAt": "2023-08-23T07:33:29.661Z",
      "updatedAt": "2023-08-23T07:33:29.661Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "64e5b481b533a5ccfe61567f",
      "attachments": []
    },
    {
      "_id": "64e5b51517af93c93bc0c394",
      "type": "message",
      "message": "#PatrolBot#Welcome to the IslandYou have woken up in the TOWN. In the distance, you hear PatrolBot searching for players to capture. Your body is still numb and lifeless - it will take some time for you to regain your mobility and make your escape. In the meantime, all you can do is pray that it doesn't find you...Come chat with other islanders on the ShockBots discord server at: https://discord.gg/34r6VdjDj !Be careful - PatrolBot will trap you for 6 hours if it catches you! (6 hours standard trap time x 1 game(s) without capture)",
      "createdAt": "2023-08-23T07:28:21.460Z",
      "updatedAt": "2023-08-23T07:28:21.460Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    },
    {
      "_id": "64e5b51490c9c4140139b493",
      "type": "message",
      "message": "Welcome to the game!",
      "createdAt": "2023-08-23T07:28:20.911Z",
      "updatedAt": "2023-08-23T07:28:20.911Z",
      "conversation": "64e5b51490c9c4140139b48f",
      "user": "6474ddcc4782931001f5e410",
      "attachments": []
    }
  ]
}
"""
