lock_info_input="""
{
  "password": "string",
  "combinationId": "string",
  "isTestLock": false
}"""
extensions_input = """{
  "extensions": [
    {
      "slug": "string",
      "config": {},
      "partnerConfigurationToken": "string",
      "mode": "cumulative",
      "regularity": 0
    }
  ]
}
  """
lock_id_response="""{"lockId": "string"}"""

guess_the_timer_result = """{"canBeUnlocked":false}"""
wheel_of_fortune_result = """{"index":0,"action":{"segment":{"type":"add-time","text":"","duration":3600}},"text":"Added 1 hour"}"""
dice_roll_result = """{"adminDice":5,"playerDice":4,"duration":3600}"""
pillory_info = """{"votes":[{"_id":"659ee3029e46da74718e83b8","nbVotes":0,"totalDurationAdded":0,"voteEndsAt":"2024-01-10T18:48:38.396Z","canVote":true,"reason":"puppy was bad","createdAt":"2024-01-10T18:33:38.397Z"}]}"""
share_link_info_response = """{"lockId":"659ee2ce9e46da74718e5f2d","extensionId":"659ee2ce9e46da74718e5f34","votes":1,"minVotes":0,"canVote":false}"""
share_link_url_response = """{"link":"https://chaster.app/sessions/z3lyGWVABT6VYmXs"}"""
share_link_vote_ack = """{"duration":3600}"""
lock_with_extension = """
{
  "lock": {
    "_id": "65a08fee021e79d9e94197b7",
    "startDate": "2024-01-12T01:03:42.000Z",
    "endDate": "2024-01-12T02:47:46.000Z",
    "minDate": "2024-01-12T02:03:42.000Z",
    "maxDate": "2024-01-12T03:03:42.000Z",
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "status": "locked",
    "combination": "65a08fed682e738986cc75c1",
    "sharedLock": null,
    "createdAt": "2024-01-12T01:03:42.291Z",
    "updatedAt": "2024-01-12T01:03:42.455Z",
    "unlockedAt": null,
    "archivedAt": null,
    "frozenAt": null,
    "keyholderArchivedAt": null,
    "totalDuration": 38568,
    "allowSessionOffer": false,
    "isTestLock": false,
    "offerToken": "8a81a595-91ec-4c24-9e79-7478b20350d9",
    "hideTimeLogs": false,
    "trusted": false,
    "user": {
      "_id": "64e5b481b533a5ccfe61567f",
      "username": "PupHimbo",
      "isPremium": false,
      "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
      "location": "San Francisco ",
      "gender": "Male",
      "age": 27,
      "role": "switch",
      "isFindom": false,
      "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
      "online": false,
      "lastSeen": null,
      "isAdmin": false,
      "isModerator": false,
      "metadata": {
        "locktober2020Points": 0,
        "locktober2021Points": 0,
        "chastityMonth2022Points": 0,
        "locktober2022Points": 0,
        "locktober2023Points": 1240
      },
      "fullLocation": "San Francisco , California, United States",
      "discordId": "1153172669559214141",
      "discordUsername": "puphimbo",
      "isDisabled": false,
      "isSuspended": false,
      "features": [],
      "joinedAt": "2023-08",
      "isNewMember": false,
      "isSuspendedOrDisabled": false
    },
    "keyholder": null,
    "isAllowedToViewTime": true,
    "canBeUnlocked": false,
    "canBeUnlockedByMaxLimitDate": false,
    "isFrozen": false,
    "extensions": [
      {
        "slug": "wheel-of-fortune",
        "displayName": "Wheel of Fortune",
        "summary": "Turn the wheel of fortune and change the duration of your lock. Configure actions for each cell of the wheel of fortune: time added or removed, frozen timer or custom text for your dares.",
        "subtitle": "Try your luck by spinning the Wheel of Fortune",
        "icon": "/static/assets/images/icons/extensions/wheel-of-fortune.svg",
        "_id": "65a08fee021e79d9e94197c6",
        "config": {
          "segments": [
            {
              "type": "add-time",
              "text": "",
              "duration": 3600
            },
            {
              "type": "remove-time",
              "text": "",
              "duration": 3600
            }
          ]
        },
        "mode": "non_cumulative",
        "regularity": 3600,
        "userData": null,
        "nbActionsRemaining": 1,
        "isPartner": false,
        "textConfig": "Add 1 hour, Remove 1 hour",
        "createdAt": "2024-01-12T01:03:42.362Z",
        "updatedAt": "2024-01-12T01:03:42.374Z"
      }
    ],
    "role": "wearer",
    "title": "Self-lock",
    "lastVerificationPicture": null,
    "availableHomeActions": [],
    "reasonsPreventingUnlocking": [],
    "extensionsAllowUnlocking": true
  },
  "extension": {
    "slug": "wheel-of-fortune",
    "config": {
      "segments": [
        {
          "type": "add-time",
          "text": "",
          "duration": 3600
        },
        {
          "type": "remove-time",
          "text": "",
          "duration": 3600
        }
      ]
    },
    "mode": "non_cumulative",
    "regularity": 3600,
    "_id": "65a08fee021e79d9e94197c7"
  }
}
"""
lock_history = """
{
  "results": [
    {
      "_id": "65a08aef021e79d9e93d2bd1",
      "type": "locked",
      "lock": "65a08aef021e79d9e93d2bcf",
      "role": "user",
      "extension": null,
      "createdAt": "2024-01-12T00:42:23.550Z",
      "title": "%USER% started a lock",
      "description": "New lock started",
      "color": null,
      "icon": "fa-lock",
      "payload": {},
      "prefix": "default",
      "user": {
        "_id": "64e5b481b533a5ccfe61567f",
        "username": "PupHimbo",
        "isPremium": false,
        "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
        "location": "San Francisco ",
        "gender": "Male",
        "age": 27,
        "role": "switch",
        "isFindom": false,
        "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
        "online": false,
        "lastSeen": null,
        "isAdmin": false,
        "isModerator": false,
        "metadata": {
          "locktober2020Points": 0,
          "locktober2021Points": 0,
          "chastityMonth2022Points": 0,
          "locktober2022Points": 0,
          "locktober2023Points": 1240
        },
        "fullLocation": "San Francisco , California, United States",
        "discordId": "1153172669559214141",
        "discordUsername": "puphimbo",
        "isDisabled": false,
        "isSuspended": false,
        "features": [],
        "joinedAt": "2023-08",
        "isNewMember": false,
        "isSuspendedOrDisabled": false
      }
    }
  ],
  "hasMore": false,
  "count": 1
}
"""

lock_combination = """
{
  "_id": "string",
  "user": "string",
  "checkStatus": "pending",
  "type": "image",
  "code": "string",
  "imageFullUrl": "string",
  "createdAt": "2024-01-03T19:13:59.683Z",
  "updatedAt": "2024-01-03T19:13:59.683Z",
  "enableManualCheck": true
}
"""

user_lock = """
{
  "deletedAt": "2024-01-12T00:42:23.000Z",
  "_id": "65a08aef021e79d9e93d2bcf",
  "startDate": "2024-01-12T00:42:23.000Z",
  "endDate": "2024-01-12T02:38:41.000Z",
  "minDate": "2024-01-12T01:42:23.000Z",
  "maxDate": "2024-01-12T02:42:23.000Z",
  "maxLimitDate": null,
  "displayRemainingTime": true,
  "limitLockTime": false,
  "status": "locked",
  "combination": "65a08aeff2c3de24ad9fd0e9",
  "sharedLock": null,
  "createdAt": "2024-01-12T00:42:23.543Z",
  "updatedAt": "2024-01-12T00:42:23.658Z",
  "unlockedAt": null,
  "archivedAt": null,
  "frozenAt": null,
  "keyholderArchivedAt": null,
  "totalDuration": 76337,
  "allowSessionOffer": false,
  "isTestLock": false,
  "offerToken": "cb04e253-2022-45aa-a6a6-f5f7bdefea6d",
  "hideTimeLogs": false,
  "trusted": false,
  "user": {
    "_id": "64e5b481b533a5ccfe61567f",
    "username": "PupHimbo",
    "isPremium": false,
    "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
    "location": "San Francisco ",
    "gender": "Male",
    "age": 27,
    "role": "switch",
    "isFindom": false,
    "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
    "online": false,
    "lastSeen": null,
    "isAdmin": false,
    "isModerator": false,
    "metadata": {
      "locktober2020Points": 0,
      "locktober2021Points": 0,
      "chastityMonth2022Points": 0,
      "locktober2022Points": 0,
      "locktober2023Points": 1240
    },
    "fullLocation": "San Francisco , California, United States",
    "discordId": "1153172669559214141",
    "discordUsername": "puphimbo",
    "isDisabled": false,
    "isSuspended": false,
    "features": [],
    "joinedAt": "2023-08",
    "isNewMember": false,
    "isSuspendedOrDisabled": false
  },
  "keyholder": null,
  "isAllowedToViewTime": true,
  "canBeUnlocked": false,
  "canBeUnlockedByMaxLimitDate": false,
  "isFrozen": false,
  "extensions": [],
  "role": "wearer",
  "title": "Self-lock",
  "lastVerificationPicture": null,
  "availableHomeActions": [],
  "reasonsPreventingUnlocking": [],
  "extensionsAllowUnlocking": true
}
"""

list_of_user_locks = """
[
  {
    "_id": "65a08aef021e79d9e93d2bcf",
    "startDate": "2024-01-12T00:42:23.000Z",
    "endDate": "2024-01-12T02:38:41.000Z",
    "minDate": "2024-01-12T01:42:23.000Z",
    "maxDate": "2024-01-12T02:42:23.000Z",
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "status": "locked",
    "combination": "65a08aeff2c3de24ad9fd0e9",
    "sharedLock": null,
    "createdAt": "2024-01-12T00:42:23.543Z",
    "updatedAt": "2024-01-12T00:42:23.658Z",
    "unlockedAt": null,
    "archivedAt": null,
    "frozenAt": null,
    "keyholderArchivedAt": null,
    "totalDuration": 3818,
    "allowSessionOffer": false,
    "isTestLock": false,
    "offerToken": "cb04e253-2022-45aa-a6a6-f5f7bdefea6d",
    "hideTimeLogs": false,
    "trusted": false,
    "user": {
      "_id": "64e5b481b533a5ccfe61567f",
      "username": "PupHimbo",
      "isPremium": false,
      "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
      "location": "San Francisco ",
      "gender": "Male",
      "age": 27,
      "role": "switch",
      "isFindom": false,
      "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
      "online": false,
      "lastSeen": null,
      "isAdmin": false,
      "isModerator": false,
      "metadata": {
        "locktober2020Points": 0,
        "locktober2021Points": 0,
        "chastityMonth2022Points": 0,
        "locktober2022Points": 0,
        "locktober2023Points": 1240
      },
      "fullLocation": "San Francisco , California, United States",
      "discordId": "1153172669559214141",
      "discordUsername": "puphimbo",
      "isDisabled": false,
      "isSuspended": false,
      "features": [],
      "joinedAt": "2023-08",
      "isNewMember": false,
      "isSuspendedOrDisabled": false
    },
    "keyholder": null,
    "isAllowedToViewTime": true,
    "canBeUnlocked": false,
    "canBeUnlockedByMaxLimitDate": false,
    "isFrozen": false,
    "extensions": [],
    "role": "wearer",
    "title": "Self-lock",
    "lastVerificationPicture": null,
    "availableHomeActions": [],
    "reasonsPreventingUnlocking": [],
    "extensionsAllowUnlocking": true
  }
]
"""

create_shared_lock = """
{
  "minDuration": 1,
  "maxDuration": 0,
  "maxLimitDuration": 0,
  "minDate": "2024-01-11T22:02:19.067Z",
  "maxDate": "2024-01-11T22:02:19.067Z",
  "maxLimitDate": "2024-01-11T22:02:19.067Z",
  "displayRemainingTime": true,
  "limitLockTime": true,
  "isPublic": true,
  "maxLockedUsers": 1,
  "password": "string",
  "requireContact": true,
  "name": "string",
  "description": "string",
  "photoId": "string",
  "hideTimeLogs": true,
  "isFindom": false
}
"""

shared_lock = """
{
	"_id": "65872d75d061f19e4e4a0a55",
	"minDuration": 345600,
	"maxDuration": 345600,
	"maxLimitDuration": 604800,
	"minDate": null,
	"maxDate": null,
	"maxLimitDate": null,
	"displayRemainingTime": false,
	"limitLockTime": true,
	"maxLockedUsers": 3,
	"isPublic": false,
	"requireContact": true,
	"name": "🟧 The Foundry: Assimilation ⬛⬛",
	"password": "IWantToBeADrone",
	"description": "aaa",
	"unsplashPhoto": {
		"id": "Sj_3Jdr19L4",
		"name": "Alek Kalinowski",
		"url": "https://images.unsplash.com/flagged/photo-1595524288414-a7fda0a12d0c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMzNTc4MTN8&ixlib=rb-4.0.3&q=80&w=1080",
		"username": "alekversusworld"
	},
	"hideTimeLogs": true,
	"lastSavedAt": "2024-01-03T19:13:59.683Z",
	"requirePassword": true,
	"user": {
		"_id": "64e5b481b533a5ccfe61567f",
		"username": "PupHimbo",
		"isPremium": false,
		"description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
		"location": "San Francisco ",
		"gender": "Male",
		"age": 27,
		"role": "switch",
		"isFindom": false,
		"avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
		"online": false,
		"lastSeen": null,
		"isAdmin": false,
		"isModerator": false,
		"metadata": {
			"locktober2020Points": 0,
			"locktober2021Points": 0,
			"chastityMonth2022Points": 0,
			"locktober2022Points": 0,
			"locktober2023Points": 1240
		},
		"fullLocation": "San Francisco , California, United States",
		"discordId": "1153172669559214141",
		"discordUsername": "puphimbo",
		"isDisabled": false,
		"isSuspended": false,
		"features": [],
		"joinedAt": "2023-08",
		"isNewMember": false,
		"isSuspendedOrDisabled": false
	},
	"durationMode": "duration",
	"isFindom": false,
	"calculatedMaxLimitDuration": 604800,
	"extensions": []
}
"""

created_shared_lock = """
{
  "id": "12345"
}
"""

get_favorited_share_locks = """{"count":3,"hasMore":false,"lastId":"658b93f66a27b7312fb2a60f","results":[{"_id":"64f8103cab27e3b54c9bb45e","minDuration":3600,"maxDuration":10800,"maxLimitDuration":43200,"minDate":null,"maxDate":null,"maxLimitDate":null,"displayRemainingTime":true,"limitLockTime":true,"maxLockedUsers":null,"isPublic":true,"requireContact":false,"name":"Puppy lock.","description":"This lock is specialy designd for pups it does not matter if you have experiance or if you are new. Puppy gear is a nice extra","unsplashPhoto":{"id":"KqehHSPhcds","name":"Viktor Forgacs","url":"https://images.unsplash.com/photo-1562061000-5be8fb06a0c7?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTM5Nzg2ODR8&ixlib=rb-4.0.3&q=80&w=1080","username":"sonance"},"hideTimeLogs":false,"lastSavedAt":"2023-09-07T20:05:54.229Z","requirePassword":false,"user":{"_id":"6101cc9a27377d001b4bec93","username":"ronnyboy1","isPremium":false,"description":"message me if you want me to lock you or if you want to lock me. I Will also make custom locks on request. if i forget to message feel free to message me back.","location":"","gender":"Male","age":20,"role":"switch","isFindom":false,"avatarUrl":"https://cdn01.chaster.app/app/uploads/avatars/UEvqPy3Do3AVhlyJ.jpg","online":false,"lastSeen":6536,"isAdmin":false,"isModerator":false,"metadata":{"locktober2020Points":0,"locktober2021Points":0,"locktober2023Points":11620,"chastityMonth2022Points":0,"locktober2022Points":0},"fullLocation":"Netherlands","discordId":"1149041515839094874","discordUsername":"ronnyboy1_97566","isDisabled":false,"isSuspended":false,"features":[],"joinedAt":"2021-07","isNewMember":false,"isSuspendedOrDisabled":false},"durationMode":"duration","isFindom":false,"calculatedMaxLimitDuration":43200,"joinRules":{"canBeJoined":true,"oneOfExtensionsDisabled":false,"containsPremiumExtension":false,"exceedsExtensionLimit":false}},{"_id":"659141cd8ae1c9663e0df301","minDuration":3600,"maxDuration":259200,"maxLimitDuration":null,"minDate":null,"maxDate":null,"maxLimitDate":null,"displayRemainingTime":true,"limitLockTime":true,"maxLockedUsers":2,"isPublic":true,"requireContact":false,"name":"Dragon's Domain","description":"Abandon all hope, ye who enter here! A horny chastised Dragon lurks within these dark halls fiercely guarding his home and treasure. Are there any Adventurers brave enough out there to step within in search of the Dragons treasure? But be warned, the Dragon had already made several would be Adventurers his sexual playthings!One hour minimum is required of any Adventurers time in the labyrinthine halls then they may leave anytime they want, but do you dare abandon your quest before you find the mighty Dragons treasure!?If your pride and greed should happen to get you caught by the Dragon, you shall become his plaything for three whole days.Journey on Adventurer!P.S. Due to an overwhelming number of would-be Adventures - all currently caged and pleasuring the Dragon - I will be putting a Password on the lock for the foreseeable future. If you are interested in trying reach out to me and if I have the time, I will gladly give you the password!","unsplashPhoto":{"id":"zQMN9fLJehM","name":"Jonathan Kemper","url":"https://images.unsplash.com/photo-1601987077677-5346c0c57d3f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDQwMTgzODF8&ixlib=rb-4.0.3&q=80&w=1080","username":"jupp"},"hideTimeLogs":true,"lastSavedAt":"2024-01-11T06:43:54.798Z","requirePassword":true,"user":{"_id":"65067e061e95ea0d2a564f8e","username":"TobyTheDragon","isPremium":false,"description":"A fun loving BDSM Dragon that loves all aspects of bondage from Doming to Subbing. If you're from Melbourne, Victoria hit me up for some fun!","location":"Melbourne","gender":"Male","age":29,"role":"switch","isFindom":false,"avatarUrl":"https://cdn01.chaster.app/app/uploads/avatars/gnrYJvwWjoxZzTM3.png","online":false,"lastSeen":7982,"isAdmin":false,"isModerator":false,"metadata":{"locktober2020Points":0,"locktober2021Points":0,"chastityMonth2022Points":0,"locktober2022Points":0,"locktober2023Points":10},"fullLocation":"Melbourne, Victoria, Australia","discordId":null,"discordUsername":null,"isDisabled":false,"isSuspended":false,"features":[],"joinedAt":"2023-09","isNewMember":false,"isSuspendedOrDisabled":false},"durationMode":"duration","isFindom":false,"calculatedMaxLimitDuration":259200,"joinRules":{"canBeJoined":true,"oneOfExtensionsDisabled":false,"containsPremiumExtension":false,"exceedsExtensionLimit":false}},{"_id":"658b3be735ec991466a64fe0","minDuration":1209600,"maxDuration":1209600,"maxLimitDuration":null,"minDate":null,"maxDate":null,"maxLimitDate":null,"displayRemainingTime":true,"limitLockTime":false,"maxLockedUsers":null,"isPublic":true,"requireContact":false,"name":"shrimp dicks lock","description":"A lock for a pathetic shrimp dick slave.Public because the shrimp dick wants to be humiliated","unsplashPhoto":{"id":"oLUdylKieqw","name":"Nathan Dumlao","url":"https://images.unsplash.com/photo-1577934017455-df37c5113f33?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDM2MjM2NTV8&ixlib=rb-4.0.3&q=80&w=1080","username":"nate_dumlao"},"hideTimeLogs":false,"lastSavedAt":"2024-01-10T11:53:26.643Z","requirePassword":false,"user":{"_id":"657f0df8e71374c7ad39c183","username":"Unxlf","isPremium":true,"description":"If you are looking for a key holder hmu. EN/DE All custom locks will be private due to personal kinks/info. FINDOM ONLY IF REQUESTED BY SUB","location":"Bremen","gender":"Male","age":26,"role":"keyholder","isFindom":true,"avatarUrl":"https://cdn01.chaster.app/app/uploads/avatars/SsM6GvA0CWbxSrMS.jpg","online":true,"lastSeen":null,"isAdmin":false,"isModerator":false,"metadata":{"locktober2020Points":0,"locktober2021Points":0,"chastityMonth2022Points":0,"locktober2022Points":0,"locktober2023Points":0},"fullLocation":"Bremen, Bremen, Germany","discordId":null,"discordUsername":null,"isDisabled":false,"isSuspended":false,"features":[],"joinedAt":"2023-12","isNewMember":false,"isSuspendedOrDisabled":false},"durationMode":"duration","isFindom":false,"calculatedMaxLimitDuration":null,"joinRules":{"canBeJoined":true,"oneOfExtensionsDisabled":false,"containsPremiumExtension":false,"exceedsExtensionLimit":false}}]}"""

shared_lock_details = """
        {
  "_id": "65139d7d1a72a968b46338e4",
  "minDuration": 0,
  "maxDuration": 0,
  "maxLimitDuration": null,
  "minDate": "2023-11-01T06:59:00.000Z",
  "maxDate": "2023-11-01T06:59:02.312Z",
  "maxLimitDate": null,
  "displayRemainingTime": true,
  "limitLockTime": true,
  "maxLockedUsers": null,
  "isPublic": true,
  "requireContact": false,
  "name": "Pup Locktober",
  "password": null,
  "description": "",
  "unsplashPhoto": {
    "id": "4cirNi6WvRg",
    "name": "David Izquierdo",
    "url": "https://images.unsplash.com/photo-1572290603512-cd1d7dad06e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTU3ODQzMTd8&ixlib=rb-4.0.3&q=80&w=1080",
    "username": "davidiz"
  },
  "hideTimeLogs": false,
  "lastSavedAt": "2023-09-27T03:11:57.595Z",
  "requirePassword": false,
  "user": {
    "_id": "64e5b481b533a5ccfe61567f",
    "username": "PupHimbo",
    "isPremium": false,
    "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
    "location": "San Francisco ",
    "gender": "Male",
    "age": 27,
    "role": "switch",
    "isFindom": false,
    "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
    "online": false,
    "lastSeen": null,
    "isAdmin": false,
    "isModerator": false,
    "metadata": {
      "locktober2020Points": 0,
      "locktober2021Points": 0,
      "chastityMonth2022Points": 0,
      "locktober2022Points": 0,
      "locktober2023Points": 1240
    },
    "fullLocation": "San Francisco , California, United States",
    "discordId": "1153172669559214141",
    "discordUsername": "puphimbo",
    "isDisabled": false,
    "isSuspended": false,
    "features": [],
    "joinedAt": "2023-08",
    "isNewMember": false,
    "isSuspendedOrDisabled": false
  },
  "durationMode": "date",
  "isFindom": false,
  "calculatedMaxLimitDuration": 0,
  "extensions": [
    {
      "slug": "temporary-opening",
      "config": {
        "openingTime": 900,
        "penaltyTime": 43200,
        "allowOnlyKeyholderToOpen": false
      },
      "mode": "non_cumulative",
      "regularity": 172800,
      "name": "Hygiene opening",
      "textConfig": "Time allowed: 15 minutes, penalty for exceeding time: 12 hours"
    }
  ]
}
        """

get_shared_locks = """[
  {
    "_id": "65872d75d061f19e4e4a0a55",
    "minDuration": 345600,
    "maxDuration": 345600,
    "maxLimitDuration": 604800,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": false,
    "limitLockTime": true,
    "maxLockedUsers": 3,
    "isPublic": false,
    "requireContact": true,
    "name": "🟧 The Foundry: Assimilation ⬛⬛",
    "password": "IWantToBeADrone",
    "description": "The Foundry is looking for Drone Candidates.Here you will become a pup drone. Your assimilation will be guided by The Foundry's central AI. Join and become One. Kinks: Dronification, identity loss, humiliation Gear needed: dildo, butt plug, chastity cagePassword:IWantToBeADroneNotes:Responses to the bot are always start with TRANSACTION: #. Bot will give response examples to each task. Bot will have a deliberate delay from the completion of one task to the next.What will happen is you'll get a message that is a task and you'll have to complete it. The bot checks in every half hour and delays between tasks to start the next on. You'll get your first message within 30 min of joining.",
    "unsplashPhoto": {
      "id": "Sj_3Jdr19L4",
      "name": "Alek Kalinowski",
      "url": "https://images.unsplash.com/flagged/photo-1595524288414-a7fda0a12d0c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMzNTc4MTN8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "alekversusworld"
    },
    "hideTimeLogs": true,
    "lastSavedAt": "2024-01-03T19:13:59.683Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": 604800,
    "extensions": []
  },
  {
    "_id": "6583af7cb03643ca3e788e7f",
    "minDuration": 3600,
    "maxDuration": 7200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "test api call",
    "password": "asdf",
    "description": "test api call",
    "unsplashPhoto": {
      "id": "tXq0AMYB4WQ",
      "name": "Viktor Bystrov",
      "url": "https://images.unsplash.com/photo-1542895947-dec6fb64f71e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMxMjg5NTZ8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "xokvictor"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-21T06:08:20.146Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "keyholder",
          "peerVerification": {
            "enabled": true,
            "punishments": [
              {
                "name": "add_time",
                "params": 3600
              },
              {
                "name": "freeze"
              },
              {
                "name": "pillory",
                "params": {
                  "duration": 900
                }
              }
            ]
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      },
      {
        "slug": "pillory",
        "config": {
          "timeToAdd": 3600,
          "limitToLoggedUsers": true
        },
        "mode": "unlimited",
        "regularity": 3600,
        "name": "Pillory",
        "textConfig": "1 hour added per vote"
      }
    ]
  },
  {
    "_id": "65827bb4d1f699fb821e915f",
    "minDuration": 86400,
    "maxDuration": 90000,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Bark Bot",
    "password": "done",
    "description": "Bark! A bot controlled lock.Looking for beta testers.Bark will do random things to your lock. A human will be there to make sure everything stays safe.Trust after entering.",
    "unsplashPhoto": {
      "id": "U32jeOdkgfA",
      "name": "Brett Jordan",
      "url": "https://images.unsplash.com/photo-1559715541-d4fc97b8d6dd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDMwNTAxNjR8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "brett_jordan"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T20:06:26.219Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": []
  },
  {
    "_id": "65584f37f173429ea76c40b6",
    "minDuration": 86400,
    "maxDuration": 259200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Femboy Pups",
    "password": "nope",
    "description": "Come be a good girl and join my lock! That means you too, the curious one who clicked on this and thinks they aren't a good girl. Interaction based lock.",
    "unsplashPhoto": {
      "id": "ZPwTWULq9xw",
      "name": "Gursimrat Ganda",
      "url": "https://images.unsplash.com/photo-1608113239923-a0bf3a1e873f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE3MDAyODYyNjN8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "gurysimrat"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:50:47.117Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "all",
          "peerVerification": {
            "enabled": false,
            "punishments": []
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      }
    ]
  },
  {
    "_id": "654d9cd9f5da1eca165ee734",
    "minDuration": 86400,
    "maxDuration": 259200,
    "maxLimitDuration": null,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": false,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "For my amusement ",
    "password": "nope",
    "description": "Join and become my new toy. Expect to end up begging. Message me about how grateful you are to be in the lock before you join.",
    "unsplashPhoto": {
      "id": "F3Dde_9thd8",
      "name": "NordWood Themes",
      "url": "https://images.unsplash.com/photo-1510127034890-ba27508e9f1c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTk1ODUyNDF8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "nordwood"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:50:59.581Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": null,
    "extensions": [
      {
        "slug": "verification-picture",
        "config": {
          "visibility": "all",
          "peerVerification": {
            "enabled": false,
            "punishments": []
          }
        },
        "mode": "non_cumulative",
        "regularity": 86400,
        "name": "Verification picture",
        "textConfig": ""
      }
    ]
  },
  {
    "_id": "65139d7d1a72a968b46338e4",
    "minDuration": 0,
    "maxDuration": 0,
    "maxLimitDuration": null,
    "minDate": "2023-11-01T06:59:00.000Z",
    "maxDate": "2023-11-01T06:59:02.312Z",
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": true,
    "maxLockedUsers": null,
    "isPublic": true,
    "requireContact": false,
    "name": "Pup Locktober",
    "password": null,
    "description": "",
    "unsplashPhoto": {
      "id": "4cirNi6WvRg",
      "name": "David Izquierdo",
      "url": "https://images.unsplash.com/photo-1572290603512-cd1d7dad06e5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTU3ODQzMTd8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "davidiz"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-09-27T03:11:57.595Z",
    "requirePassword": false,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "date",
    "isFindom": false,
    "calculatedMaxLimitDuration": 0,
    "extensions": [
      {
        "slug": "temporary-opening",
        "config": {
          "openingTime": 900,
          "penaltyTime": 43200,
          "allowOnlyKeyholderToOpen": false
        },
        "mode": "non_cumulative",
        "regularity": 172800,
        "name": "Hygiene opening",
        "textConfig": "Time allowed: 15 minutes, penalty for exceeding time: 12 hours"
      }
    ]
  },
  {
    "_id": "64e69feb2f626eb789dafd6e",
    "minDuration": 14400,
    "maxDuration": 86400,
    "maxLimitDuration": 86400,
    "minDate": null,
    "maxDate": null,
    "maxLimitDate": null,
    "displayRemainingTime": true,
    "limitLockTime": true,
    "maxLockedUsers": null,
    "isPublic": false,
    "requireContact": true,
    "name": "Pup Search Lock",
    "password": "nope",
    "description": "Hmu pups! And join the lock if you like.",
    "unsplashPhoto": {
      "id": "WSAOGHKEqFc",
      "name": "Bruce Warrington",
      "url": "https://images.unsplash.com/photo-1556866261-8763a7662333?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3wxMzE4NDZ8MHwxfGFsbHx8fHx8fHx8fDE2OTI4MzU4MTl8&ixlib=rb-4.0.3&q=80&w=1080",
      "username": "brucebmax"
    },
    "hideTimeLogs": false,
    "lastSavedAt": "2023-12-25T21:51:09.511Z",
    "requirePassword": true,
    "user": "64e5b481b533a5ccfe61567f",
    "durationMode": "duration",
    "isFindom": false,
    "calculatedMaxLimitDuration": 86400,
    "extensions": []
  }
]"""
