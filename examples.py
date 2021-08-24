# Put JSON HERE

bw_chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7[44✫] §b[MVP§9+§b] ByonPlays§f',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile 880a651b-ffc1-460f-9f91-4449f069ab03'},
            'hoverEvent': {'action': 'show_text', 'value': {
                'text': "§b[MVP§9+§b] ByonPlays§f\n§7Hypixel Level: §6117\n§7Achievement Points: §e2,905\n§7Guild: §b§bNone\n\n§eClick to view §bByonPlays§e's profile!",
                'strikethrough': False}}
        },
        {
            'text': ': Need an active guild do /g join Team Voided (Level 83) Tag:✧VOID✧ Reqs: Network lvl 60 or 500 wins in BW. Must have Discord and get 100k weekly.',
            'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False,
            'color': 'white'}
    ]
}

friend_status = {'text': 'Friend > ', 'color': 'green',
                 'extra': [{'text': 'JqmmyYT ', 'color': 'green'}, {'text': 'left.', 'color': 'yellow'}]}

skywars_chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7[6✫] §7pogleah§7',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile ba1859c5-5c38-4e43-b448-660679f968fc'},
            'hoverEvent': {'action': 'show_text', 'value': {
                'text': "§7pogleah§7\n§7Hypixel Level: §612\n§7Achievement Points: §e360\n§7Guild: §b§bNone\n\n§eClick to view §7pogleah§e's profile!",
                'strikethrough': False}}
        },
        {'text': ': a', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
         'strikethrough': False, 'color': 'gray'}
    ]
}

# NOT ACTUALLY A LIST IT ARE 2 SEPERATE MESSAGES
watchdog_json = [
    {'italic': False, 'extra': [{'bold': True, 'color': 'red', 'text': 'A player has been removed from your lobby.'}],
     'text': ''},
    {'italic': False, 'extra': [{'color': 'aqua', 'text': 'Use /report to continue helping out the server!'}],
     'text': ''}
]


chat_message = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§7jenscc2006§7',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile 5beb3dff-b44d-49af-8ad0-f35aecac9eb7'},
            'hoverEvent': {
                'action': 'show_text',
                'value': {'text': "§7jenscc2006§7\n§7Hypixel Level: §61\n§7Achievement Points: §e35\n§7Guild: §b§bNone\n\n§eClick to view §7jenscc2006§e's profile!", 'strikethrough': False}
            }
        },
        {'text': 'This is where the chat message is. Its not what jenscc2006 actually said. They made an emote and it was hard to see. Is this illegal?', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
    ]
}

important_mystery_box_opened = {
    'text': '[Mystery Box] ',
    'strikethrough': False,
    'color': 'aqua',
    'hoverEvent': {
        'action': 'show_text',
        'value': {
            'text': 'You can find ',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'gray',
            'extra': [
                {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'},
                {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
            ]
        }
    },
    'extra': [
        {
            'text': '§f§bFrost_alt §ffound a §6Legendary Thor Suit Head§f!',
            'strikethrough': False,
            'color': 'aqua',
            'hoverEvent': {
                'action': 'show_text',
                'value': {
                    'text': 'Type: ',
                    'bold': False,
                    'italic': False,
                    'underlined': False,
                    'obfuscated': False,
                    'strikethrough': False,
                    'color': 'gray',
                    'extra': [
                        {'text': 'Suit Pieces\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'yellow'},
                        {'text': 'Rarity: ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gray'},
                        {'text': 'Legendary', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False, 'strikethrough': False, 'color': 'gold'}
                    ]
                }
            }
        }
    ]
}

limbo_message = {'text': 'You are AFK. Move around to return from AFK.', 'color': 'red'}
