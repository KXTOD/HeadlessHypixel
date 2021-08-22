from rich import print

json_data = {
    'text': 'ChengRang ',
    'bold': False,
    'italic': False,
    'underlined': False,
    'obfuscated': False,
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
                {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                 'strikethrough': False, 'color': 'aqua'},
                {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                 'strikethrough': False, 'color': 'gray'},
                {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                 'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
            ]
        }
    },
    'extra': [
        {
            'text': 'found a ',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'white',
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
                        {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                        {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
                    ]
                }
            }
        },
        {
            'text': '✰✰✰✰✰ ',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'yellow',
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
                        {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                        {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
                    ]
                }
            }
        },
        {
            'text': 'Mystery Box',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
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
                        {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                        {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
                    ]
                }
            }
        },
        {
            'text': '!',
            'bold': False,
            'italic': False,
            'underlined': False,
            'obfuscated': False,
            'strikethrough': False,
            'color': 'white',
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
                        {'text': 'Mystery Boxes ', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'aqua'},
                        {'text': 'by\n', 'bold': False, 'italic': False, 'underlined': False, 'obfuscated': False,
                         'strikethrough': False, 'color': 'gray'},
                        {'text': 'playing games on the server!', 'bold': False, 'italic': False, 'underlined': False,
                         'obfuscated': False, 'strikethrough': False, 'color': 'gray'}
                    ]
                }
            }
        }
    ]
}

if json_data['extra'][2]['text'] == "Mystery Box" and json_data['extra'][2]['color'] == "aqua":
    correct_color = {"green": "green1", "aqua": "turquoise2", "orange": "orange1", "gray": "bright_black"}
    username = json_data['text']
    username_color = json_data['color']
    rating = json_data['extra'][1]['text']
    clr = correct_color[username_color]
    print(f"[{clr}]{username}[/][bright_yellow]found a {rating}[/][turquoise2]Mystery Box[/][bright_white]![/]")
