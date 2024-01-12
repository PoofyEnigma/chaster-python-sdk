all_known_extensions = """
[
  {
    "subtitle": "Share your lock with others",
    "summary": "Share a link to other people to ask them to add or remove time to your lock.",
    "displayName": "Share links",
    "icon": "link",
    "slug": "link",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "timeToAdd": 3600,
      "timeToRemove": 3600,
      "enableRandom": true,
      "nbVisits": 0,
      "limitToLoggedUsers": false
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": false,
    "isPartner": false,
    "isFeatured": false,
    "isTesting": false,
    "hasActions": false,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Be displayed publicly when you receive a penalty",
    "summary": "When you receive a penalty, be displayed publicly for a specified period of time. Other users will be able to add time to your lock.",
    "displayName": "Pillory",
    "icon": "user-friends",
    "slug": "pillory",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "timeToAdd": 3600,
      "limitToLoggedUsers": true
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": false,
    "isPartner": false,
    "isFeatured": false,
    "isTesting": false,
    "hasActions": false,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Roll the dice and try to reduce your time locked",
    "summary": "With every action, you and the bot roll a dice. If you do more than the bot, time is removed. If the bot does more, time is added.",
    "displayName": "Dice",
    "icon": "dice",
    "slug": "dice",
    "availableModes": [
      "non_cumulative",
      "cumulative",
      "unlimited"
    ],
    "defaultConfig": {
      "multiplier": 3600
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Try your luck by spinning the Wheel of Fortune",
    "summary": "Turn the wheel of fortune and change the duration of your lock. Configure actions for each cell of the wheel of fortune: time added or removed, frozen timer or custom text for your dares.",
    "displayName": "Wheel of Fortune",
    "icon": "/static/assets/images/icons/extensions/wheel-of-fortune.svg",
    "slug": "wheel-of-fortune",
    "availableModes": [
      "non_cumulative",
      "cumulative",
      "unlimited"
    ],
    "defaultConfig": {
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
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Receive tasks and earn points to be unlocked",
    "summary": "Spice up your session by receiving tasks. Configure the tasks you want to do, and receive a random task, or ask other users to vote.",
    "displayName": "Tasks",
    "icon": "tasks",
    "slug": "tasks",
    "availableModes": [
      "non_cumulative",
      "cumulative",
      "unlimited"
    ],
    "defaultConfig": {
      "tasks": [
        {
          "task": "",
          "points": 0
        }
      ],
      "voteEnabled": false,
      "voteDuration": 43200,
      "startVoteAfterLastVote": false,
      "enablePoints": false,
      "pointsRequired": 0,
      "allowWearerToEditTasks": false,
      "allowWearerToConfigureTasks": false,
      "preventWearerFromAssigningTasks": false,
      "allowWearerToChooseTasks": false,
      "actionsOnAbandonedTask": []
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Receive penalties when you do not perform actions on time",
    "summary": "Receive penalties when you do not perform actions on time.",
    "displayName": "Penalties",
    "icon": "gavel",
    "slug": "penalty",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "penalties": []
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": false,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Temporarily unlock yourself",
    "summary": "Because hygiene is important, unlock yourself regularly to clean your chastity device. Be careful, if you exceed the allowed time, you will receive a penalty.",
    "displayName": "Hygiene opening",
    "icon": "soap",
    "slug": "temporary-opening",
    "availableModes": [
      "non_cumulative"
    ],
    "defaultConfig": {
      "openingTime": 900,
      "penaltyTime": 43200,
      "allowOnlyKeyholderToOpen": false
    },
    "defaultRegularity": 172800,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": false,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Regularly take a picture of your device to show that you are locked",
    "summary": "Regularly take a picture of your chastity device to show that you are locked.",
    "displayName": "Verification picture",
    "icon": "camera",
    "slug": "verification-picture",
    "availableModes": [
      "non_cumulative",
      "unlimited"
    ],
    "defaultConfig": {
      "visibility": "all",
      "peerVerification": {
        "enabled": false,
        "punishments": []
      }
    },
    "defaultRegularity": 86400,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Add randomness to your lock",
    "summary": "Random events can happen and change your timer. Time added or removed, frozen lock, many things can happen. You don't know when it will happen, it's a surprise.",
    "displayName": "Random Events",
    "icon": "random",
    "slug": "random-events",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "difficulty": "normal"
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": false,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "With the timer hidden, guess when you think the timer is finished",
    "summary": "Guess correctly the timer, or time is added. The timer is hidden, press the unlock button when you think the timer is finished. If the timer is still running, random time is added!",
    "displayName": "Guess the Timer",
    "icon": "clock",
    "slug": "guess-timer",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "minRandomTime": 10800,
      "maxRandomTime": 21600
    },
    "defaultRegularity": 3600,
    "isEnabled": true,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": true,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "Play cards",
    "summary": "The interactive card game",
    "displayName": "Cards",
    "icon": "/static/assets/images/icons/extensions/cards.svg",
    "slug": "cards",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "regularity": 60,
      "cards": [
        {
          "type": "green",
          "min": 1,
          "max": 1
        },
        {
          "type": "red",
          "min": 5,
          "max": 5
        }
      ],
      "mode": "non_cumulative",
      "nbKeysRequired": 1
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": false,
    "hasActions": true,
    "configIframeUrl": "https://app.chaster.cards/configuration",
    "partnerExtensionId": "625163f6115da438303d2ece"
  },
  {
    "subtitle": "The Vince Evil bot",
    "summary": "Try the Vince's Evil bot!",
    "displayName": "VinceBot",
    "icon": "puzzle-piece",
    "slug": "vincebot",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aadba994e50f462c13b737"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aae284c20678feb39a885d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Aetherial Gaol",
    "icon": "puzzle-piece",
    "slug": "aetherial-gaol",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aae4dcc969a47608272467"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "KittenLocksTest",
    "icon": "puzzle-piece",
    "slug": "kittenlockstest",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aaed97a83c310210dc754a"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "TestExtension",
    "icon": "puzzle-piece",
    "slug": "testextension",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aaf7bf03eb4996090826b0"
  },
  {
    "subtitle": "Play a game to determine your lock time",
    "summary": "",
    "displayName": "Lucky Case",
    "icon": "puzzle-piece",
    "slug": "lucky-case",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "difficulty": 1
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:4200/lucky-case/config",
    "partnerExtensionId": "64aaf7f651a2526070e11edd"
  },
  {
    "subtitle": "Additional and improved random events.",
    "summary": "Incorporate randomness into your lock with new and improved events based off the already existing Chaster Random Events extension.",
    "displayName": "Random Events++",
    "icon": "puzzle-piece",
    "slug": "random-events-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "minimum": 1800,
      "maximum": 3600,
      "events": {
        "add-time": {
          "bias": 1,
          "minimum": 1800,
          "maximum": 3600
        },
        "remove-time": {
          "bias": 1,
          "minimum": 1800,
          "maximum": 3600
        },
        "disorientate": {
          "bias": 1,
          "minimum": 1800,
          "maximum": 3600
        },
        "freeze": {
          "bias": 1
        },
        "unfreeze": {
          "bias": 1
        },
        "toggle-freeze": {
          "bias": 1
        },
        "pillory": {
          "bias": 1,
          "minimum": 1800,
          "maximum": 3600
        }
      },
      "manualTriggerWait": 1800,
      "canWearerManuallyTrigger": false
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:3000/configuration/randomevents",
    "partnerExtensionId": "64aafa20c20678feb39e41e9"
  },
  {
    "subtitle": "",
    "summary": "Force your lockees to watch Porns ! ",
    "displayName": "Forced Voyeur",
    "icon": "puzzle-piece",
    "slug": "forced-voyeur",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab0328617b7d05e9b1d764"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Skaldik's Tasks",
    "icon": "puzzle-piece",
    "slug": "skaldiks-tasks",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab045f637e4ea5ce33a4c0"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "RandomizerExtension",
    "icon": "puzzle-piece",
    "slug": "randomizerextension",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab104294e50daafc0ac7c2"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test extension enderaxis",
    "icon": "puzzle-piece",
    "slug": "test-extension-enderaxis",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab13b7784350dbcb6eaf10"
  },
  {
    "subtitle": "Take a quiz to determine your lock time",
    "summary": "",
    "displayName": "Quiz",
    "icon": "puzzle-piece",
    "slug": "quiz",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:4200/quiz/config",
    "partnerExtensionId": "64ab2006784350dbcb70d303"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-2",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab21d2678683e4d88a5a4b"
  },
  {
    "subtitle": "Manage secondary lockboxes",
    "summary": "Got additional locks for your cuffs and chains? Manage them alongside your primary lockbox.",
    "displayName": "Multi-Lock",
    "icon": "puzzle-piece",
    "slug": "multi-lock",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://xandren.org/api/chaster/multi-lock/config",
    "partnerExtensionId": "64ab32fc74c692fe463ac090"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Forced Watch",
    "icon": "puzzle-piece",
    "slug": "forced-watch",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "videos": [
        {
          "name": "Lucie preferred one",
          "url": "https://www.tubebdsm.com/out/?l=3AAQJ84SiXrCq3NLRjZVRDhQT05NAtlnaHR0cHM6Ly92aWRlb3Vwb3JuaWEuY29tL3ZpZGVvcy80OTAwNzUzL2RpLW1hcmNvLWFuZC1oYWxleS13aWxkZS10aGUtdHJhaW5pbmctb2YtZGF5LXRocmVlLz9wcm9tbz0zMTEzNM0B66J0YwHNA6incG9wdWxhcgLZJ3sib3JpZW50YXRpb24iOiJzdHJhaWdodCIsInByaWNpbmciOiIifc0auM5kt0mNqHBvcm5zdGFyzRH1&c=345333ad&v=3&",
          "watched": false
        }
      ]
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://127.0.0.1:5173/configuration",
    "partnerExtensionId": "64ab38a86047fed011c44cc9"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-3",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab3a4039a1dcddc78e4a4e"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-4",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ab68a694e50daafc152af0"
  },
  {
    "subtitle": "Get Zaps to get free",
    "summary": "Send Commands to your PiShock from Chaster. Enabling your KH to force you to endure shocks. ",
    "displayName": "ChasterShock",
    "icon": "puzzle-piece",
    "slug": "chastershock",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 28800,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64abc8af678683e4d89a6e63"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-6",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ad55296047fed011001d85"
  },
  {
    "subtitle": "Automatically require paypal payments on findom locks",
    "summary": "Automatically require paypal payments for your findom lock.",
    "displayName": "Paypal verification",
    "icon": "puzzle-piece",
    "slug": "paypal-verification",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ad68dfe9d359bd489ab47c"
  },
  {
    "subtitle": "Purchase you feedom.",
    "summary": "",
    "displayName": "Shop",
    "icon": "puzzle-piece",
    "slug": "shop",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "rate": 1,
      "intervals": 3600,
      "items": [
        {
          "id": "1",
          "price": 100,
          "discount": 1,
          "stock": 10,
          "isInfinite": true,
          "events": [
            {
              "slug": "remove-time",
              "config": {
                "minimum": 1800,
                "maximum": 3600
              }
            }
          ]
        },
        {
          "id": "2",
          "price": 100,
          "discount": 1,
          "stock": 10,
          "isInfinite": true,
          "events": [
            {
              "slug": "unfreeze",
              "config": {}
            }
          ]
        }
      ]
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5000/extension",
    "partnerExtensionId": "64ad8254b8fdcbd1becb4c7a"
  },
  {
    "subtitle": "The Classic Card Game",
    "summary": "",
    "displayName": "Black Jack",
    "icon": "puzzle-piece",
    "slug": "black-jack",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ad869b960e15ccef448492"
  },
  {
    "subtitle": "Track how many steps were made.",
    "summary": "This extension counts steps by connecting to smart wearables.Currently Supported: - MiBand 4",
    "displayName": "Steps",
    "icon": "puzzle-piece",
    "slug": "steps",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "requiredSteps": 0
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5173/config",
    "partnerExtensionId": "64ad952a6047fed0110942a3"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-7",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64adb6c8960e15ccef4b7caa"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Timer",
    "icon": "puzzle-piece",
    "slug": "timer",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ae7bfeb8fdcbd1bee6928c"
  },
  {
    "subtitle": "Roll the (definitely fair) dice and try to reduce your time locked",
    "summary": "Ever worried that your lockee would accidentally 'get lucky' when rolling the dice? No longer! ",
    "displayName": "Weighted Dice",
    "icon": "puzzle-piece",
    "slug": "weighted-dice",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": {
      "chances": [
        9.09,
        9.09,
        9.09,
        9.09,
        9.09,
        9.1,
        9.09,
        9.09,
        9.09,
        9.09,
        9.09
      ],
      "multiplier": 60,
      "multiplierText": "1 hour"
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://strawberria-extensions.github.io/chaster/weighted-dice/configuration",
    "partnerExtensionId": "64af0eae37d58b6e1f991612"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "freeze tag",
    "icon": "puzzle-piece",
    "slug": "freeze-tag",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64af1aa02c028aed953a5ab1"
  },
  {
    "subtitle": "Obedience Shop Rewards",
    "summary": "Do you want to pick up a reward for obedience and locking up? Now you have the opportunity with this extension.",
    "displayName": "Obedience shop rewards",
    "icon": "puzzle-piece",
    "slug": "obedience-shop-rewards",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64af702d74ea9db9cc788cb0"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Alfred",
    "icon": "puzzle-piece",
    "slug": "alfred",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://alfred.localho.st/chaster/configuration",
    "partnerExtensionId": "64b04760635caf5bc0d861b9"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Alfred",
    "icon": "puzzle-piece",
    "slug": "alfred-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64b1182efb7dbf391953b8ae"
  },
  {
    "subtitle": "Complete tech domination",
    "summary": "Let your keyholder restrict your devices with Qustodio. Works with most devices: Phones, Tablets and PCs (iOS, Android, Windows, Chromebooks).",
    "displayName": "Qustodio",
    "icon": "phone-laptop",
    "slug": "qustodio",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "capabilities": [
        "FILTER_CONTENT",
        "SHOW_HISTORY"
      ]
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://benevolent-rolypoly-6c077b.netlify.app/qustodio/config",
    "partnerExtensionId": "64b203b07922dc18c4858cad"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Dice Roll",
    "icon": "puzzle-piece",
    "slug": "dice-roll",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64b3cbe2dc26d6f14eea632c"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Qustodio Dev",
    "icon": "puzzle-piece",
    "slug": "qustodio-dev",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "capabilities": [
        "FILTER_CONTENT",
        "SHOW_HISTORY"
      ]
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5173/qustodio/config",
    "partnerExtensionId": "64b3f9cbdc26d6f14ef12dee"
  },
  {
    "subtitle": "User Chaster like you used Chastikey",
    "summary": "",
    "displayName": "The Old Cards Game",
    "icon": "puzzle-piece",
    "slug": "the-old-cards-game",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://cuffed.cf/theoldcardgame/configuration.php",
    "partnerExtensionId": "64b47de31c5bdb5c3dd9424d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Extended Chat Logs",
    "icon": "puzzle-piece",
    "slug": "extended-chat-logs",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64b4c8ee88a049802a390331"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "WriteForMe",
    "icon": "puzzle-piece",
    "slug": "writeforme",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64b4fa06060ad853855ef647"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Jigsaw Puzzle",
    "icon": "puzzle-piece",
    "slug": "jigsaw-puzzle",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "images": [
        "https://cdni.pornpics.de/1280/7/427/75245688/75245688_098_c8b6.jpg",
        "https://media.discordapp.net/attachments/937623725728231454/1131268883328794684/bdsmlr-10785268-NUJhzNdhr3.jpg"
      ],
      "pieces": 60
    },
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://jigsaw.enteofdeath.com/#/config",
    "partnerExtensionId": "64b6e673267e8345a044617b"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Jigsaw Puzzle (Dev)",
    "icon": "puzzle-piece",
    "slug": "jigsaw-puzzle-dev",
    "availableModes": [
      "non_cumulative",
      "cumulative",
      "unlimited"
    ],
    "defaultConfig": {
      "images": [
        "https://cdni.pornpics.de/1280/7/427/75245688/75245688_098_c8b6.jpg"
      ],
      "pieces": 100
    },
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5173/#/config",
    "partnerExtensionId": "64b829c9c7712c5e28297276"
  },
  {
    "subtitle": "Try your luck spinning the Extended Wheel of Fortune, now with multiple wheels and expanded actions!",
    "summary": "An extended Wheel of Fortune with more wheels and more features!",
    "displayName": "Extended Wheel of Fortune",
    "icon": "puzzle-piece",
    "slug": "extended-wheel-of-fortune",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "wheels": {},
      "text": ""
    },
    "defaultRegularity": 0,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://127.0.0.1:5173/chaster/extended-wheel/configuration",
    "partnerExtensionId": "64b8d3b37ead8f0540d6a807"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Jigsaw Puzzle (Test)",
    "icon": "puzzle-piece",
    "slug": "jigsaw-puzzle-test",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "images": [
        "https://cdni.pornpics.de/1280/7/427/75245688/75245688_098_c8b6.jpg"
      ],
      "pieces": 100
    },
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://jigsaw-test.enteofdeath.com/#/config",
    "partnerExtensionId": "64b99c7981795a85fd0cf281"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "HWJ",
    "icon": "puzzle-piece",
    "slug": "hwj",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ba12bf67bd12aeec582511"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Wheel of Fortune +",
    "icon": "puzzle-piece",
    "slug": "wheel-of-fortune-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64bab6bbbd0a0d39d852c8eb"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Hellscape",
    "icon": "puzzle-piece",
    "slug": "hellscape",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64bf1404eb08bc1b0750e0ab"
  },
  {
    "subtitle": "Fully configurable Random Events",
    "summary": "A fully configurable random events system that can prevent unlocking before a configurable number of events has occurred, allows for manually triggered events, and can penalize the wearer for not having enough random events triggered in a time period.",
    "displayName": "Better Random Events",
    "icon": "puzzle-piece",
    "slug": "better-random-events",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "slug": "better-random-events",
      "minTime": "P0Y0M0DT2H0M0S",
      "maxTime": "P0Y0M0DT12H0M0S",
      "weightIntervalHigher": true,
      "addTime": true,
      "removeTime": true,
      "freeze": true,
      "unfreeze": true,
      "pillory": true,
      "addTimeMin": "P0Y0M0DT0H1M0S",
      "addTimeMax": "P0Y0M0DT0H20M0S",
      "addTimeWeightHigher": true,
      "removeTimeMin": "P0Y0M0DT0H1M0S",
      "removeTimeMax": "P0Y0M0DT0H20M0S",
      "removeTimeWeightLower": true,
      "removeTimeNegative": false,
      "alwaysUnfreezeIfFrozen": true,
      "alwaysUnfreezeIfFrozenFor": "P0Y0M0DT0H15M0S",
      "totalOdds": 100,
      "addTimeOdds": 0.6,
      "removeTimeOdds": 0.2,
      "freezeOdds": 0.1,
      "pilloryOdds": 0.1,
      "pilloryLengthMin": "P0Y0M0DT0H15M0S",
      "pilloryLengthMax": "P0Y0M0DT1H0M0S",
      "minimumEventsToUnlock": 1,
      "userTriggerable": true,
      "eventsRequiredPerPeriod": 1,
      "penaltyPeriod": "P0Y0M1DT0H0M0S",
      "penaltyAddTime": "P0Y0M0DT1H0M0S",
      "penaltyFreeze": true,
      "penaltyPilloryLength": "P0Y0M0DT1H0M0S",
      "penaltyMultiplier": true,
      "penaltyMultiplierPer": 1.1,
      "freezeOnStart": false
    },
    "defaultRegularity": 7200,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://bre.knks.xyz/better-random-events/configuration",
    "partnerExtensionId": "64bfdc1b0bc87274b398f1e8"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Quiz",
    "icon": "puzzle-piece",
    "slug": "quiz-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64c16a3935d8b870bfc46cb3"
  },
  {
    "subtitle": "Sudoku is a logic-based, combinatorial number-placement puzzle.",
    "summary": "Solve Sudoku grid to improve your self ! Success or failures may influence your chastity !",
    "displayName": "Sudoku",
    "icon": "puzzle-piece",
    "slug": "sudoku",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:4200/sudoku/config",
    "partnerExtensionId": "64c3806a862a9a64ef45cfb8"
  },
  {
    "subtitle": "Unlocking is only possible at agreed times and locations.",
    "summary": "",
    "displayName": "Geo Lock",
    "icon": "puzzle-piece",
    "slug": "geo-lock",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {
      "canChangePortals": false,
      "portals": []
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5173/geolock/config",
    "partnerExtensionId": "64c62cc001abed5e27e2dac7"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Random+",
    "icon": "puzzle-piece",
    "slug": "random",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64c75e9af50e610e51864d99"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-8",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64c796c0f50e610e518c31ca"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test mobile",
    "icon": "puzzle-piece",
    "slug": "test-mobile",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64c85d72a73cc4560ebba547"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Time From Caption",
    "icon": "puzzle-piece",
    "slug": "time-from-caption",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64cbb68ace00841df97c46fc"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Dynamic Wheel of Fortune",
    "icon": "puzzle-piece",
    "slug": "dynamic-wheel-of-fortune",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64cd44b4efc89cb981cae915"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test Extension",
    "icon": "puzzle-piece",
    "slug": "test-extension",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64cd93ddc0c80f5e37d3bb34"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-9",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ce9697fc52e82591373ae0"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "2048",
    "icon": "puzzle-piece",
    "slug": "2048",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "magnification": 3
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64cf04a2fab49b8385a63c89"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Spin",
    "icon": "puzzle-piece",
    "slug": "spin",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64d223154b3c92d15a6e8be6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Hello",
    "icon": "puzzle-piece",
    "slug": "hello",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64d22b8ff36983e2f350fc80"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Better Dice",
    "icon": "puzzle-piece",
    "slug": "better-dice",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "slug": "better-dice",
      "sides": 6,
      "time": "P0Y0M0DT1H0M0S",
      "winMultiplier": 0.9,
      "loseMultiplier": 1.1,
      "skipTies": true,
      "eventsRequiredPerPeriod": 1,
      "penaltyPeriod": "P0Y0M1DT0H0M0S",
      "penaltyAddTime": "P0Y0M0DT1H0M0S",
      "penaltyFreeze": true,
      "penaltyPilloryLength": "P0Y0M0DT0H15M0S",
      "penaltyMultiplier": true,
      "penaltyMultiplierPer": 1.1,
      "minimumEventsToUnlock": 2,
      "rigKeyholderDice": false,
      "rigWearerDice": false,
      "invisibleDice": false
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://bre.knks.xyz/better-dice/configuration",
    "partnerExtensionId": "64d2b279397aab68839330f6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "The Test",
    "icon": "puzzle-piece",
    "slug": "the-test",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64d610ae0c68c0042a1b567c"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Blackjack",
    "icon": "puzzle-piece",
    "slug": "blackjack",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:4200/blackjack/config",
    "partnerExtensionId": "64d68f71a0831433d8bd04cd"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "tesex",
    "icon": "puzzle-piece",
    "slug": "tesex",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64da5609baafe3f3fff64d64"
  },
  {
    "subtitle": "Answer random questions - get some time reduction.",
    "summary": "Trivia Time Unlock is an engaging and interactive extension designed to add an element of fun and challenge to your chastity experience. By answering a variety of random questions correctly, you'll earn valuable time reductions off your chastity lock. Put your knowledge to the test, learn new facts, and enjoy a unique way to manage your lock duration. With Trivia Time Unlock, learning and pleasure go hand in hand as you work towards unlocking your device sooner.",
    "displayName": "Trivia",
    "icon": "puzzle-piece",
    "slug": "trivia",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://chaster.neocore.cc/trivia/config",
    "partnerExtensionId": "64db814b537d5daf7edb0e6d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Minecraft",
    "icon": "puzzle-piece",
    "slug": "minecraft",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64dc019b65ffdfd91857e242"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "testify",
    "icon": "puzzle-piece",
    "slug": "testify",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64e7e033e9c9b69dacf2f358"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Unlock Gamble",
    "icon": "puzzle-piece",
    "slug": "unlock-condition",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "unlockWeight": 1,
      "taskWeight": 0,
      "deniedWeight": 1,
      "tasks": [],
      "deniedPunishments": [
        {
          "weight": 1,
          "items": [
            {
              "type": "AddFixed",
              "seconds": 1800
            }
          ]
        }
      ],
      "taskFailedPunishments": []
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:80/config",
    "partnerExtensionId": "64ee7f8c9c558b01392b65d6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Cards",
    "icon": "puzzle-piece",
    "slug": "cards-1",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64f0161fde7c96a8d193a16b"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "reading",
    "icon": "puzzle-piece",
    "slug": "reading",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64f5aa0c0a4d27590a6dd338"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "exTest",
    "icon": "puzzle-piece",
    "slug": "extest",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64f771bbb4547cbdaee861c4"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test extension ",
    "icon": "puzzle-piece",
    "slug": "test-extension-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64f826387b23592e40e0857f"
  },
  {
    "subtitle": "Automatically freeze lock when started",
    "summary": "Automatically freeze lock when started - 1 minute interval until webhooks implemented",
    "displayName": "Start Frozen",
    "icon": "puzzle-piece",
    "slug": "start-frozen",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64fb9225ed0e690948140801"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test ext",
    "icon": "puzzle-piece",
    "slug": "test-ext",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64fe4b78c640e4a9f3d6df96"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "ocr",
    "icon": "puzzle-piece",
    "slug": "ocr",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64fe8ca0f8a07e521f7bbbbe"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Strawberria Random Events",
    "icon": "puzzle-piece",
    "slug": "strawberria-random-events",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64feb1b75d52d1e0da0011f4"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-10",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ff40f87d4c79bbe92968d9"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test Extention",
    "icon": "puzzle-piece",
    "slug": "test-extention",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ffaebf8cb4d71652fdcff8"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "TestE",
    "icon": "puzzle-piece",
    "slug": "teste",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65035674f9f9a7c21f68246f"
  },
  {
    "subtitle": "Connect your session to your favourite video games!",
    "summary": "Play your favourite video game, and watch as it impacts your chastity sentence.",
    "displayName": "ChasterGAMES",
    "icon": "puzzle-piece",
    "slug": "chastergames",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 0,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://localhost:3000/edit",
    "partnerExtensionId": "6504292765089c3c19da3aa8"
  },
  {
    "subtitle": "Test extension - do not use",
    "summary": "Test extension - do not use",
    "displayName": "Testension",
    "icon": "puzzle-piece",
    "slug": "testension",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://testension.techspace.cz/config.html",
    "partnerExtensionId": "65060692351e727f76c095e5"
  },
  {
    "subtitle": "Add verification to the official Tasks  extension",
    "summary": "This extension allows you to add a verification to tasks, to make a wearer prove they completed the task. Verification is currently done using images and videos.",
    "displayName": "Verified Tasks",
    "icon": "puzzle-piece",
    "slug": "verified-tasks",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65070a48765e36978f70c858"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-11",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65089aa13fd57cd49cb7d6ef"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Demerzel",
    "icon": "puzzle-piece",
    "slug": "demerzel",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6509debb91428683c4fa4247"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "app_ext",
    "icon": "puzzle-piece",
    "slug": "appext",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "650aaef1d3c3c59d121fb340"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "LockBox",
    "icon": "puzzle-piece",
    "slug": "lockbox",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "650c0173af10eaf90ab755c8"
  },
  {
    "subtitle": "Connect StarDash to your lock!",
    "summary": "Allows you to play games, gamble and more using StarDash.",
    "displayName": "StarDash connect",
    "icon": "puzzle-piece",
    "slug": "stardash-connect",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://starlightwt.github.io/StarDashWeb/views/config.html",
    "partnerExtensionId": "650c837f49758e706c6cfa4b"
  },
  {
    "subtitle": "POC_hangman_implementation",
    "summary": "",
    "displayName": "handman_localhost_app",
    "icon": "puzzle-piece",
    "slug": "handmanlocalhostapp",
    "availableModes": [
      "unlimited",
      "cumulative"
    ],
    "defaultConfig": "default:config",
    "defaultRegularity": 7200,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://webhook.site/4b51c2f6-3d07-4ba9-be59-371ee9b4f037",
    "partnerExtensionId": "650ee4210222257fa301c2ca"
  },
  {
    "subtitle": "this is an implementation of the More or Less  game",
    "summary": "a random number will be generated, you have to guess it.Each time you fail, time will be added",
    "displayName": "more_or_less",
    "icon": "puzzle-piece",
    "slug": "moreorless",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": {
      "MaxNumber": 100,
      "MinNumber": 0,
      "NumberOfTry": 5,
      "Penality": 300,
      "Reward": 300
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://127.0.0.1:5000/config",
    "partnerExtensionId": "650efa48b469cf0a9d2cae42"
  },
  {
    "subtitle": "Wearer has to complete Wordle puzzles",
    "summary": "Attempt to solve Wordles. The keyholder can add custom words, add rewards for completed puzzles and add penalties for failed puzzles.",
    "displayName": "Wordle",
    "icon": "puzzle-piece",
    "slug": "wordle",
    "availableModes": [
      "non_cumulative"
    ],
    "defaultConfig": {
      "words": [
        "caged"
      ],
      "rewards": [
        {
          "action": "REMOVE_TIME",
          "data": 60
        },
        {
          "action": "UNFREEZE",
          "data": null
        }
      ],
      "punishments": [
        {
          "action": "ADD_TIME",
          "data": 120
        }
      ],
      "punishmentTexts": [
        "Add time: 2 hours"
      ],
      "rewardTexts": [
        "Remove time: 1 hour",
        "Unfreeze the lock"
      ],
      "freezeWhenAvailable": false,
      "attemptPunishmentsActive": false,
      "attemptPunishments": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
      }
    },
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://wordle-prod.enteofdeath.com/#/config",
    "partnerExtensionId": "6511de0d69627fdcf8d471c2"
  },
  {
    "subtitle": "Test instance for the Wordle extension. This is used to test new features and bugfixes before public release. Take care, this might be instable :)",
    "summary": "",
    "displayName": "Wordle (Test)",
    "icon": "puzzle-piece",
    "slug": "wordle-test",
    "availableModes": [
      "non_cumulative"
    ],
    "defaultConfig": {
      "words": [
        "caged"
      ],
      "rewards": [
        {
          "action": "REMOVE_TIME",
          "data": 60
        },
        {
          "action": "UNFREEZE",
          "data": null
        }
      ],
      "punishments": [
        {
          "action": "ADD_TIME",
          "data": 120
        }
      ],
      "punishmentTexts": [
        "Add time: 2 hours"
      ],
      "rewardTexts": [
        "Remove time: 1 hour",
        "Unfreeze the lock"
      ],
      "freezeWhenAvailable": false,
      "attemptPunishmentsActive": false,
      "attemptPunishments": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
      }
    },
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://wordle-test.enteofdeath.com/#/config",
    "partnerExtensionId": "6511de1a974a20984bfd4c97"
  },
  {
    "subtitle": "DONT USE - This extension is used for local development of new features and bugfixes and will not work for you",
    "summary": "",
    "displayName": "Wordle (Dev)",
    "icon": "puzzle-piece",
    "slug": "wordle-dev",
    "availableModes": [
      "non_cumulative"
    ],
    "defaultConfig": {
      "words": [
        "caged"
      ],
      "rewards": [
        {
          "action": "REMOVE_TIME",
          "data": 60
        },
        {
          "action": "UNFREEZE",
          "data": null
        }
      ],
      "punishments": [
        {
          "action": "ADD_TIME",
          "data": 120
        }
      ],
      "punishmentTexts": [
        "Add time: 2 hours"
      ],
      "rewardTexts": [
        "Remove time: 1 hour",
        "Unfreeze the lock"
      ],
      "freezeWhenAvailable": false,
      "attemptPunishmentsActive": false,
      "attemptPunishments": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
      }
    },
    "defaultRegularity": 86400,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:5173/#/config",
    "partnerExtensionId": "6511de25a0496ae3fd4757b6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-13",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6519f3542583fe072a3d65a6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Improvement",
    "icon": "puzzle-piece",
    "slug": "improvement",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6519f6c344c60e9085168321"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Locktober Points",
    "icon": "puzzle-piece",
    "slug": "locktober-points",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "651c43cbcf6c6c4b55e7f3da"
  },
  {
    "subtitle": "Set sport goals to reach, then be reward or punished",
    "summary": "Set sport goals to reach.",
    "displayName": "Sport tracker by Strava",
    "icon": "puzzle-piece",
    "slug": "strava",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 0,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:4200/strava/config",
    "partnerExtensionId": "651c7917ba083ca539a4b59c"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "asd",
    "icon": "puzzle-piece",
    "slug": "asd",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "651de821b3d818f15d134d96"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "add",
    "icon": "puzzle-piece",
    "slug": "add",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6520a0c4dea36974018d6c3b"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Mobile Mod",
    "icon": "puzzle-piece",
    "slug": "md",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6521280f3b371a3415bfaff4"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test1",
    "icon": "puzzle-piece",
    "slug": "test1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "652659cb5116c64fd6c5d4b9"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Trst",
    "icon": "puzzle-piece",
    "slug": "trst",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6526c5795116c64fd6d7c8ad"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-14",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6526c59d3e0774ec64c1a5b2"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-15",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65278a2aff4c15c95ff2bc5e"
  },
  {
    "subtitle": "Send yourself to pillory",
    "summary": "Makes it possible to wearer to send *self to pillory.",
    "displayName": "Just the Pillory",
    "icon": "puzzle-piece",
    "slug": "just-the-pillory",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": {
      "min": 900,
      "max": 86400,
      "editable": true
    },
    "defaultRegularity": 60,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://testension.techspace.cz/jtp/config.html",
    "partnerExtensionId": "652be6346a25bfd1221d7a1d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "TTLOCK",
    "icon": "puzzle-piece",
    "slug": "ttlock",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "652c7cacf60028cff6bb0a3b"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test-extension-2230",
    "icon": "puzzle-piece",
    "slug": "test-extension-2230",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "652f96d473e439e1c5c5f389"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Censored Rewards",
    "icon": "puzzle-piece",
    "slug": "censored-rewards",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65304fda7d0b5f3dede19c37"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-16",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65319bdc2f6fd9dd8a03d590"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Challenge Queue",
    "icon": "puzzle-piece",
    "slug": "challenge-queue",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://localhost:3000/config",
    "partnerExtensionId": "65348f56b909cf4b230a5897"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Random",
    "icon": "puzzle-piece",
    "slug": "random-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65355c16b1dbb6e9cf296999"
  },
  {
    "subtitle": "Chores",
    "summary": "",
    "displayName": "Chores",
    "icon": "puzzle-piece",
    "slug": "chores",
    "availableModes": [
      "unlimited",
      "cumulative",
      "non_cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://localhost:5250/chores/configuration",
    "partnerExtensionId": "653b8d628ea522cbdfdbbdf4"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "marina extension",
    "icon": "puzzle-piece",
    "slug": "marina-extension",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "653d0192295d3329060781bf"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "CustomSafe",
    "icon": "puzzle-piece",
    "slug": "customsafe",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "653d38d314d36ee9184ec471"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test Extension",
    "icon": "puzzle-piece",
    "slug": "test-extension-2",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://www.edotmedia.net/extConfig-1.html",
    "partnerExtensionId": "653fa935f5c228750878e91d"
  },
  {
    "subtitle": "Input keyholder-specified codes to trigger various lock effects!",
    "summary": "Input keyholder-specified codes to trigger various lock effects!",
    "displayName": "Scavenger Codes",
    "icon": "puzzle-piece",
    "slug": "scavenger-codes",
    "availableModes": [
      "unlimited",
      "non_cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 0,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "https://strawberria-extensions.github.io/chaster/scavenger-codes/configuration",
    "partnerExtensionId": "6541c6993b3caea7f9302dd3"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "testa",
    "icon": "puzzle-piece",
    "slug": "testa",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6547bb86bd6f7eab81550a74"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-17",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65487c9b35c2c37fe45feb7b"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Multiple Choice 4 Timer",
    "icon": "puzzle-piece",
    "slug": "multiple-choice-4-timer",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "654ac4e66c9bced4ef877b51"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test extension",
    "icon": "puzzle-piece",
    "slug": "test-extension-3",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "654fd0be01b9d7f70cd0913d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test 1",
    "icon": "puzzle-piece",
    "slug": "test-1-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65551f8dc67c65a5a2f70ff6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "FirstTry",
    "icon": "puzzle-piece",
    "slug": "firsttry",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "655a52426803eeab7fe828ed"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Blackjack",
    "icon": "puzzle-piece",
    "slug": "blackjack-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "655ba4b0225b6b576db42b30"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-18",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "655bc51d225b6b576db87156"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Forced Watch",
    "icon": "puzzle-piece",
    "slug": "forced-watch-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "http://127.0.0.1:5173/configuration",
    "partnerExtensionId": "6563ded8a506024f1582114e"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Locked .Games",
    "icon": "puzzle-piece",
    "slug": "locked-games",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "656a665bf8ae6426559a8382"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-19",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "656bdf69131aa7c3ed646cc4"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Chance",
    "icon": "puzzle-piece",
    "slug": "chance",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6578b74516530460e289d3f0"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Wordle",
    "icon": "puzzle-piece",
    "slug": "wordle-1",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "658035bbe5007754e1c7e4ff"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-21",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6580bbf2ba132054ee6e8353"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-22",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6580c9d9633e84cf4e657cee"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-23",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6581847b6e1dd8ce538ef5b6"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-24",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6583a20495fcd4d1214e38d9"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Spend Task Points",
    "icon": "puzzle-piece",
    "slug": "spend-task-points",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "658633553ac6ae0a97245093"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Blackjack",
    "icon": "puzzle-piece",
    "slug": "blackjack-2",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6587662297013b3584ea8974"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "learning",
    "icon": "puzzle-piece",
    "slug": "learning",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "658fbc3416a535b3060be6b8"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Creative Tasks",
    "icon": "puzzle-piece",
    "slug": "creative-tasks",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "659041038ae1c9663e2b3f61"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "locky2",
    "icon": "puzzle-piece",
    "slug": "locky2",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6592939b226caa341fd08148"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Linked Locks",
    "icon": "puzzle-piece",
    "slug": "linked-locks",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6594626f342be9f93000ed22"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "chaste_footer_bar",
    "icon": "puzzle-piece",
    "slug": "chastefooterbar",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "65956636a01ff1848a74f384"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test Extension",
    "icon": "puzzle-piece",
    "slug": "test-extension-4",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "659628c3cf4e271ed19a1132"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "extension-01",
    "icon": "puzzle-piece",
    "slug": "extension-01",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6599d65e543e396f805e2458"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-25",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "659abc53c946e6530fb6d898"
  },
  {
    "subtitle": "Stay locked the whole month",
    "summary": "Complete actions and games throughout the month and earn points to be the best wearer of the month!",
    "displayName": "Locktober 2020",
    "icon": "jack-o-lantern",
    "slug": "locktober",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": {},
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": false,
    "isFeatured": false,
    "isTesting": false,
    "hasActions": true,
    "configIframeUrl": null,
    "partnerExtensionId": null
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-1",
    "availableModes": [
      "unlimited",
      "non_cumulative",
      "cumulative"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aae4b551a2526070ddfdd1"
  },
  {
    "subtitle": "Additional and improved random events.",
    "summary": "Incorporate randomness into your lock with new and improved events based of the already existing Chaster Random Events extension.",
    "displayName": "IGNORE!!",
    "icon": "puzzle-piece",
    "slug": "random-events-2",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 0,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aaf91ec969a476082a6248"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Test",
    "icon": "puzzle-piece",
    "slug": "test-5",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ababf3678683e4d897a1da"
  },
  {
    "subtitle": "Sudoku is a logic-based, combinatorial number-placement puzzle.",
    "summary": "Solve Sudoku grid to improve your self ! Success or failures may influence your chastity !",
    "displayName": "Sudoku deprecated",
    "icon": "puzzle-piece",
    "slug": "sudoku-game",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64abf2bc94e50daafc228964"
  },
  {
    "subtitle": "Test",
    "summary": "",
    "displayName": "JorgenBot",
    "icon": "puzzle-piece",
    "slug": "jorgenbot",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64aed3d3826a52781a35a258"
  },
  {
    "subtitle": "So once your timer has ran out you need to look for the key",
    "summary": "This extensions will require you to walk around the key will be hidden somewhere around you walk around and see if you can find it. (Not really a fixed position but once you enter a new quadrant there is a chance the key is there)",
    "displayName": "Find the needle in the haystack",
    "icon": "puzzle-piece",
    "slug": "find-the-needle-in-the-haystack",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64de8ecfd7980c543314a396"
  },
  {
    "subtitle": "Remote padlock management",
    "summary": "Configure how the padlock will be unlock",
    "displayName": "padlock",
    "icon": "puzzle-piece",
    "slug": "padlock",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "64ec8a5b96e0f3422bf34850"
  },
  {
    "subtitle": "test2",
    "summary": "",
    "displayName": "test",
    "icon": "puzzle-piece",
    "slug": "test-12",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6509c556b35200d20ac4ca5d"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "Task Master",
    "icon": "puzzle-piece",
    "slug": "task-master",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "657121e9614131e802f24f45"
  },
  {
    "subtitle": "",
    "summary": "",
    "displayName": "TEST",
    "icon": "puzzle-piece",
    "slug": "test-20",
    "availableModes": [
      "unlimited"
    ],
    "defaultConfig": "",
    "defaultRegularity": 3600,
    "isEnabled": false,
    "isPremium": false,
    "isCountedInExtensionsLimit": true,
    "isPartner": true,
    "isFeatured": false,
    "isTesting": true,
    "isDevelopedByCommunity": true,
    "hasActions": true,
    "configIframeUrl": "",
    "partnerExtensionId": "6571efbd6b090391bf65e942"
  }
]
"""

user_auth_profile = """
{
  "_id": "64e5b481b533a5ccfe61567f",
  "keycloakId": "ed1a6151-c5b8-4863-adc5-b83a01df62db",
  "username": "PupHimbo",
  "email": "maxwright378@gmail.com",
  "emailVerified": true,
  "subscriptionEnd": null,
  "customSubscriptionEnd": null,
  "hasPastDueSubscription": false,
  "description": "Pup looking for more friends, cuddles, and cum, and maybe a cage. Aspiring to be a slutty Himbo pup",
  "location": "San Francisco ",
  "gender": "male",
  "birthDate": "1996-08-10T00:00:00.000Z",
  "role": "switch",
  "avatarUrl": "https://cdn01.chaster.app/app/uploads/avatars/EfcMg0h1HiLUc67j.jpg",
  "isPremium": false,
  "isDeveloper": true,
  "subscriptionCancelAfterEnd": false,
  "discordId": "1153172669559214141",
  "discordUsername": "puphimbo",
  "isAdmin": false,
  "isModerator": false,
  "isFindom": false,
  "settings": {
    "showLocksOnProfile": false,
    "showOnlineStatus": false,
    "showDiscordOnProfile": true,
    "emailOnWearerUsesSharedLock": true,
    "messageOnWearerUsesSharedLock": true,
    "discordNotifications": true,
    "discordMessagingNotifications": true,
    "displayNsfw": true,
    "showAge": true
  },
  "metadata": {
    "locktober2020Points": 0,
    "locktober2021Points": 0,
    "chastityMonth2022Points": 0,
    "locktober2022Points": 0,
    "locktober2023Points": 1240
  },
  "country": {
    "countryName": "United States",
    "countryShortCode": "US"
  },
  "region": {
    "name": "California",
    "shortCode": "CA"
  },
  "privateMetadata": {
    "locktoberPlusModalPending": false
  },
  "hasAcceptedCommunityRules": true,
  "features": [],
  "needsDiscordMigration": true,
  "canEditUsername": true
}
"""


user_badges = """
{
  "pendingMessages": 0,
  "unreadMessages": 0,
  "keyholdingRequests": 0
}"""

detailed_user_profile= """
{
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
  "stats": {
    "nbStartedLocks": 42,
    "nbEndedLocks": 28,
    "totalTimeLocked": 5318548,
    "maxTimeLocked": 2677341,
    "keyholderNbLocks": 38
  },
  "achievements": [
    {
      "name": "Early member",
      "slug": "early_member",
      "description": "Member since the launch of Chaster",
      "category": "chaster",
      "progressEnabled": false,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": null,
      "total": null,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "Welcome to the adventure",
      "slug": "wearer_first_lock_started",
      "description": "Start your first lock session as a wearer",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": null,
      "total": null,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "My first session",
      "slug": "wearer_first_lock_ended",
      "description": "End your first lock session",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": null,
      "total": null,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "My first day",
      "slug": "wearer_1_day",
      "description": "Achieve a cumulative locked time of one day",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 5318548,
      "total": 86400,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "Seven days locked",
      "slug": "wearer_7_days",
      "description": "Achieve a cumulative locked time of seven days",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 5318548,
      "total": 604800,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "How long will it last?",
      "slug": "wearer_30_days",
      "description": "Achieve a cumulative locked time of 30 days",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 5318548,
      "total": 2592000,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "It was a long day",
      "slug": "wearer_max_1_day",
      "description": "Stay locked an entire day",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 2677341,
      "total": 86400,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "A week locked",
      "slug": "wearer_max_7_days",
      "description": "Stay locked 7 days in a row",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 2677341,
      "total": 604800,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "A whole month",
      "slug": "wearer_max_30_days",
      "description": "Stay locked 30 days in a row",
      "category": "wearer",
      "progressEnabled": true,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 2677341,
      "total": 2592000,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "Control another one",
      "slug": "keyholder_first_lock",
      "description": "Create a shared lock and lock a user",
      "category": "keyholder",
      "progressEnabled": false,
      "hideIfNotGranted": false,
      "granted": true,
      "progress": 38,
      "total": 1,
      "grantedAt": "2023-08-23T12:06:06.619Z"
    },
    {
      "name": "Locktober 2023",
      "slug": "locktober_2023_participation",
      "description": "Participate in the Locktober 2023 event",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": true,
      "progress": null,
      "total": null,
      "grantedAt": "2023-11-05T22:17:26.982Z"
    },
    {
      "name": "Locktober keyholder",
      "slug": "locktober_2023_keyholder",
      "description": "Have a wearer locked during the entire Locktober 2023",
      "category": "keyholder",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": true,
      "progress": null,
      "total": null,
      "grantedAt": "2023-11-05T22:17:26.982Z"
    },
    {
      "name": "Locktober 2020",
      "slug": "locktober_2020_participation",
      "description": "Participate in the Locktober 2020 event",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "I did Locktober 2020!",
      "slug": "locktober_2020",
      "description": "Stay locked all October 2020",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Locktober 2021",
      "slug": "locktober_2021_participation",
      "description": "Participate in the Locktober 2021 event",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Locktober keyholder",
      "slug": "locktober_2021_keyholder",
      "description": "Have a wearer locked during the entire Locktober",
      "category": "keyholder",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "I did Locktober 2021!",
      "slug": "locktober_2021",
      "description": "Stay locked all October 2021",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Chastity Month 2022",
      "slug": "chastity_month_2022_participation",
      "description": "Participate in the Chastity Month 2022 event",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Chastity Month keyholder",
      "slug": "chastity_month_2022_keyholder",
      "description": "Have a wearer locked during the entire Chastity Month",
      "category": "keyholder",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Chastity Month 2022 Challenger",
      "slug": "chastity_month_2022",
      "description": "Stay locked during the entire Chastity Month 2022",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Locktober 2022",
      "slug": "locktober_2022_participation",
      "description": "Participate in the Locktober 2022 event",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Locktober keyholder",
      "slug": "locktober_2022_keyholder",
      "description": "Have a wearer locked during the entire Locktober 2022",
      "category": "keyholder",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "I did Locktober 2022!",
      "slug": "locktober_2022",
      "description": "Stay locked all October 2022",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "Challenge Master - Locktober 2023",
      "slug": "locktober_2023_challenge",
      "description": "Obtain the most votes in a community challenge",
      "category": "chaster",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    },
    {
      "name": "I did Locktober 2023!",
      "slug": "locktober_2023",
      "description": "Stay locked all October 2023",
      "category": "wearer",
      "progressEnabled": false,
      "hideIfNotGranted": true,
      "granted": false,
      "progress": null,
      "total": null,
      "grantedAt": null
    }
  ],
  "chastikeyStats": null,
  "sharedLocks": [
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
      ],
      "joinRules": {
        "canBeJoined": true,
        "oneOfExtensionsDisabled": false,
        "containsPremiumExtension": false,
        "exceedsExtensionLimit": false
      }
    }
  ]
}
"""

user_profile = """
{
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
"""

lock_info_input = """
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
lock_id_response = """{"lockId": "string"}"""

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
