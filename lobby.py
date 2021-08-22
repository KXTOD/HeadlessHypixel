from rich import print
import regex as re

# json = {
#     'text': '',
#     'strikethrough': False,
#     'extra': [
#         {'text': ' §b>§c>§a>§r ', 'strikethrough': False},
#         {
#             'text': '§6[MVP§e++§6] Unitique§f §6joined the lobby!',
#             'strikethrough': False,
#             'clickEvent': {'action': 'run_command', 'value': '/viewprofile 795179c3-ba52-4733-b8d6-ed8eef68e586'},
#             'hoverEvent': {'action': 'show_text', 'value': {'text': "§6[MVP§e++§6] Unitique§f\n§7Hypixel Level: §659\n§7Achievement Points: §e2,775\n§7Guild: §bLoved\n\n§eClick to view §6Unitique§e's profile!", 'strikethrough': False}}
#         },
#         {'text': ' §a<§c<§b<', 'strikethrough': False}
#     ]
# }

json = {
    'text': '',
    'strikethrough': False,
    'extra': [
        {
            'text': '§b[MVP§4+§b] OkDude§f §6joined the lobby!',
            'strikethrough': False,
            'clickEvent': {'action': 'run_command', 'value': '/viewprofile e6650b4e-8c18-44cb-b2a7-f393c37c2ec9'},
            'hoverEvent': {'action': 'show_text', 'value': {
                'text': "§b[MVP§4+§b] OkDude§f\n§7Hypixel Level: §6156\n§7Achievement Points: §e4,945\n§7Guild: §b§bNone\n\n§eClick to view §bOkDude§e's profile!",
                'strikethrough': False}}
        }
    ]
}

# Matches mc color code with RICH color code
clr_dict = {"§4": "dark_red", "§c": "red", "§6": "orange1", "§e": "yellow", "§2": "dark_green", "§a": "green3",
            "§b": "turquoise2", "§3": "sky_blue3", "§1": "dark_blue", "§9": "blue", "§d": "pink", "§5": "purple",
            "§f": "bright_white", "§7": "white", "§8": "bright_black", "§0": "black", "§r": "bright_white",
            "§l": "bold", "§o": "italic", "§n": "underline", "§m": "strike", "§k": ""}

# Checks if MVP++ rank
if json["extra"][0]["text"] == " §b>§c>§a>§r ":
    rank = "MVP++"
    string = json["extra"][1]['text']
    clr = []
    for index, item in enumerate(string):
        if item == "]":
            # Regex that stars 2 positions after ] (index+2) and then gets the whole word until a space appears, .span() gets the indexes
            regex_index = re.match("([^\s]+)", string[index + 2:]).span()
            # Pure magic
            name = string[index + 2:index + 2 + regex_index[1] - 2]
    # Loops trough string and searches for §
    for item in [pos for pos, char in enumerate(string) if char == "§"]:
        # Gets the complete minecraft color (§e) and then checks if its in the dict if not then it switches to white
        if string[item:item + 2] in clr_dict:
            clr.append(clr_dict[string[item:item + 2]])
        else:
            clr.append("bright_white")

    # Builds chatmsg
    chatmsg = f"[turquoise2]>[/][red]>[/][green3]>[/] [{clr[0]}][MVP[/][{clr[1]}]++[/][{clr[2]}]] {name}[/] [{clr[3]}][/][{clr[4]}]joined the lobby! [/] [green3]<[/][red]<[/][turquoise2]<[/]"

else:
    rank = "MVP+"
    string = json["extra"][0]['text']
    clr = []
    for index, item in enumerate(string):
        if item == "]":
            regex_index = re.match("([^\s]+)", string[index + 2:]).span()
            name = string[index + 2:index + 2 + regex_index[1] - 2]

    for item in [pos for pos, char in enumerate(string) if char == "§"]:
        if string[item:item + 2] in clr_dict:
            clr.append(clr_dict[string[item:item + 2]])

    print(name, clr)
    chatmsg = f"[{clr[0]}][MVP[/][{clr[1]}]+[/][{clr[2]}]] {name}[/] [{clr[3]}][/][{clr[4]}]joined the lobby! [/]"

print(f"{chatmsg}")
