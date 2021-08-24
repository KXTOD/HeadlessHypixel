from rich import print
import regex as re

n = None

rank_colors = {"VIP": "green1", "VIP+": "green1",
               "MVP": "turquoise2", "MVP+": "turquoise2",
               "MVP++": "orange1",
               None: "bright_black", "None": "bright_black", "non": "bright_black"}

color_format = {"4": "dark_red", "c": "red", "6": "orange1", "e": "bright_yellow", "2": "dark_green",
                "a": "green1", "b": "turquoise2", "3": "sky_blue3", "1": "dark_blue", "9": "blue", "d": "pink",
                "5": "purple", "f": "bright_white", "7": "white", "8": "bright_black", "0": "black",
                "r": "bright_white", "l": "bold", "o": "italic", "n": "underline", "m": "strike", "k": ""}

correct_color = {"green": "#55FF55", "aqua": "#55FFFF", "orange": "orange1",
                 "gray": "#AAAAAA", "red": "#FF5555", "dark_green": "#00AA00", "dark_red": "#AA0000", "gold": "#FFAA00",
                 "yellow": "#FFFF55", "dark_aqua": "#00AAAA", "dark_blue": "#0000AA", "blue": "#5555FF",
                 "light_purple": "#FF55FF", "dark_purple": "#AA00AA", "white": "bright_white", "dark_gray": "#555555",
                 "black": "#000000"}

bw_message = {
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


# Main class
class ChatMessage:
    # Server

    class Hypixel:
        # World

        class HypixelSkywarsLobby:
            def __init__(self):
                pass

        class HypixelBedwarsLobby:
            def __init__(self, json_string):
                # Initializing properties
                self.username = n
                self.message = n
                self.color_code = n
                self.patched_color = n

                # Assigning properties
                self.username = json_string['extra'][0]['text']
                self.message = json_string['extra'][1]['text']
                for character in self.username:
                    if character == "§":
                        try:
                            self.color_code = self.username[self.username.index(character) + 1]
                        except ValueError:
                            continue
                        self.patched_color = f"[{color_format[self.color_code]}]"
                        try:
                            self.username = self.username.replace(
                                self.username[self.username.index(character):self.username.index(character) + 2],
                                self.patched_color)
                        except ValueError:
                            continue

            def formatted(self):
                return f"{self.username}{self.message}"

            def debugPrint(self):
                print(f"Username: {self.username}\nMessage: {self.message}\nColor code: {self.color_code}\nPatched color: {self.patched_color}")

        class Global:
            class PrivateMessage:
                def __init__(self, json_string):
                    # TODO could be updated to store sender and their rank? Also message could be separated from the sender

                    # Status (From/To)
                    self.status = n
                    self.status_color = n
                    self.patched_status_color = n

                    # The message itself
                    self.chat_color = n
                    self.chat_message = n
                    self.patched_chat_color = n

                    # Retrieving values
                    self.status = json_string['text']
                    self.status_color = json_string['color']
                    self.patched_status_color = correct_color[self.status_color]
                    self.chat_message = ""

                    # Loops trough chat strings
                    for element in json_string['extra']:
                        self.chat_color = element['color']
                        self.patched_color = correct_color[self.chat_color]
                        self.chat_message = self.chat_message + str(f"[{self.patched_color}]") + element['text'] + "[/]"

                def formatted(self):
                    return f"[{self.patched_status_color}]{self.status}[/]{self.chat_message}"

                def debugPrint(self):
                    print(f"Status: {self.status}\nStatus color: {self.status_color}\n"
                          f"Patched status color: {self.patched_status_color}\n\nChat message: {self.chat_message}\n"
                          f"Chat color: {self.chat_color}\nPatched chat color: {self.patched_chat_color}")

            class FriendList:
                def __init__(self, json_string):
                    self.username = n
                    self.username_color = n
                    self.status = n
                    self.chat_message = n

                    # Matches to check for, if they exists message gets ignored
                    self.matches_flist = [">>", "\n", " §6Friends (Page", "-" * 51, '                         ', '<<',
                                          '                       ']
                    self.matches_status = [" is in", " is currently offline"]

                    # Creates user dict
                    self.user_dict = {}

                    for item in json_string['extra']:
                        # Filters messages like: Page(1 off 27)
                        if not any(ext in item['text'] for ext in self.matches_flist):
                            # If this returns true a username has been found and will be stored
                            if not any(ext in item['text'] for ext in self.matches_status):
                                self.username = item['text'][2:]
                                self.username_color = item['text'][1:2]
                                self.patched_color = color_format[self.username_color]
                                # Stores key in user dict with patched color and username and assigns None
                                self.user_dict[f"[{self.patched_color}]{self.username}[/]"] = None

                            else:
                                # This will be ran when no username was found
                                self.status = item['text'][1:]
                                self.status_color = item['color']

                                # Quick catch for colors
                                if self.status_color == "yellow":
                                    self.status_color = "yellow1"
                                elif self.status_color == "red":
                                    self.status_color = "red"
                                else:
                                    self.status_color = "bright_white"

                                # The value non from user_dict is now removed and replaced by status
                                self.user_dict[
                                    f"[{self.patched_color}]{self.username}[/]"] = f"[{self.status_color}]{self.status}[/]"

                def formatted(self):
                    # I added the formatting in the user_dict since doing it here was to much lines of code
                    # TODO Adding friend page index
                    self.chat_message = f"[blue3]{51 * '-'}[/]\n"
                    for item in self.user_dict:
                        self.chat_message = self.chat_message + f"{item} {self.user_dict[item]}\n"

                    return self.chat_message + f"[blue3]{51 * '-'}[/]\n"

                # TODO Add debugPrint()
                def debugPrint(self):
                    # Not entirely sure how this code works! - Simon
                    pass

            class WatchdogMessage:
                def __init__(self, json_string):
                    # Gets message
                    self.message = json_string['extra'][0]['text']

                    # Gets message color
                    self.message_color = json_string['extra'][0]['color']

                    # Tries to check if bold key exists
                    try:
                        if json_string['extra'][0]['bold']:
                            self.bold = "bold "
                    except KeyError:
                        self.bold = ""

                    # Tries to apply correct color
                    try:
                        self.patched_colorr = correct_color[self.message_color]
                    except KeyError:
                        self.patched_color = "bright_white"

                def formatted(self):
                    return f"[{self.bold}{self.patched_color}]{self.message}"

                def debugPrint(self):
                    print(
                        f"Bold: {self.bold}\nMessage: {self.message}\nMessage Color: {self.message_color}\nPatched color: {self.patched_color}")

            class FriendStatus:
                def __init__(self, json_string):
                    self.username = n
                    self.username_color = n
                    self.patched_color = n
                    self.status = n

                    # Gets username
                    self.username = json_string['extra'][0]['text']

                    # Gets username color and patches it
                    self.username_color = json_string['extra'][0]['color']

                    try:
                        self.patched_color = correct_color[self.username_color]
                    except KeyError:
                        self.patched_color = "bright_white"

                    # Gets status (join/leave)
                    self.status = json_string['extra'][1]['text']

                def debugPrint(self):
                    print(
                        f"Name: {self.username}\nColor: {self.username_color}\nStatus: {self.status}\nPatched color: {self.patched_color}\n")

                def formatted(self):
                    return f"[green1]Friend > [/][{correct_color[self.username_color]}]{self.username}[/][bright_yellow]{self.status}[/]"

            class MysteryBoxes:
                def __init__(self, json_string):
                    self.username_color = n
                    self.username = n
                    self.rating = n
                    self.patched_color = n

                    # Gets username
                    self.username = json_string['text']

                    # Gets username color and patches it
                    self.username_color = json_string['color']

                    try:
                        self.patched_color = correct_color[self.username_color]
                    except KeyError:
                        self.patched_color = "bright_white"

                    # Gets rating
                    self.rating = json_string['extra'][1]['text']

                def debugPrint(self):
                    print(
                        f"Name: {self.username}\nColor: {self.username_color}\nRating: {self.rating}\nPatched color: {self.patched_color}\n")

                def formatted(self):
                    return f"[{correct_color[self.username_color]}]{self.username}[/][bright_yellow]found a {self.rating} [/][turquoise2]Mystery Box[/][bright_white]![/]"

            class LobbyJoinMessage:
                def __init__(self, json_dict):

                    self.name = n
                    self.rank = n
                    self.rankColour = n
                    self.uuid = n
                    self.network_level = n
                    self.ach_pts = n
                    self.guild = n

                    # Checks and sets rank
                    if json_dict["extra"][0]["text"] == " §b>§c>§a>§r ":
                        self.rank = "MVP++"
                        string = json_dict["extra"][1]
                    else:
                        self.rank = "MVP+"
                        string = json_dict["extra"][0]

                    # Sets name
                    if self.rank == "MVP++":
                        self.json_string = json_dict["extra"][1]['text']
                    else:
                        self.json_string = json_dict["extra"][0]['text']

                    for index, item in enumerate(self.json_string):
                        if item == "]":
                            # Regex that stars 2 positions after ] (index+2) and then gets the whole word until a
                            # space appears, .span() gets the indexes
                            regex_index = re.match("([^\s]+)", self.json_string[index + 2:]).span()
                            # Pure magic
                            self.name = self.json_string[index + 2:index + 2 + regex_index[1] - 2]

                    # Sets uuid
                    self.uuid = string["clickEvent"]["value"][13:]

                    # Sets rank color
                    for index, item in enumerate(string["text"]):
                        if item == "+":
                            self.rankColour = string["text"][index - 1]
                            break
                        if index == len(string) and self.rankColour is not None:
                            print("ERROR: Could not find + color.")

                    # Sets network level
                    startPoint = n
                    hoverEventText = string["hoverEvent"]["value"]["text"]
                    for index, item in enumerate(hoverEventText):
                        if hoverEventText[index:index + 7] == " Level:" and startPoint is None:
                            startPoint = index + 10
                        elif startPoint is not None:
                            if hoverEventText[index:index + 13] == "§7Achievement":
                                endPoint = index - 1
                                try:
                                    self.network_level = int(hoverEventText[startPoint:endPoint])
                                except ValueError:
                                    print("ERROR: ValueError while setting network level.")
                                except Exception as e:
                                    print(f"ERROR: Exception: {e}")
                                break

                        if index == len(hoverEventText):
                            print("ERROR: Could not find network level.")

                    # Sets achievement points
                    startPoint = n
                    for index, item in enumerate(hoverEventText):
                        if hoverEventText[index:index + 8] == " Points:" and startPoint is None:
                            startPoint = index + 11
                        elif startPoint is not None:
                            if hoverEventText[index:index + 8] == "§7Guild:":
                                endPoint = index - 1
                                try:
                                    self.ach_pts = int(str(hoverEventText[startPoint:endPoint]).replace(",", ""))
                                except ValueError:
                                    print("ERROR: ValueError while setting achievement points.")
                                except Exception as e:
                                    print(f"ERROR: Exception: {e}")
                                break

                        if index == len(hoverEventText):
                            print("ERROR: Could not find achievement points.")

                    # Sets guild
                    startPoint = n
                    for index, item in enumerate(hoverEventText):
                        if hoverEventText[index:index + 6] == "Guild:" and startPoint is None:
                            startPoint = index + 9
                        elif startPoint is not None:
                            if hoverEventText[index:index + 7] == "§eClick":
                                endPoint = index - 2
                                self.guild = hoverEventText[startPoint:endPoint]
                                if self.guild == "§bNone":
                                    self.guild = None
                                break

                        if index == len(hoverEventText):
                            print("ERROR: Could not find guild.")

                def debugPrint(self):
                    print(f"Name: {self.name}\nUUID: {self.uuid}\nRank: {self.rank}\n"
                          f"Rank '+' color: {color_format[self.rankColour]}"
                          f"\nNetwork level: {self.network_level}\nAchievement points: {self.ach_pts}\n"
                          f"Guild: {self.guild}")

                def formatted(self):
                    if self.rank == "MVP++":
                        return f"[turquoise2]>[/][red]>[/][green3]>[/] [{rank_colors[self.rank]}][MVP[/][{color_format[self.rankColour]}]++[/][{rank_colors[self.rank]}]] {self.name}[/] [orange1]joined the lobby! [/][green3]<[/][red]<[/][turquoise2]<[/]"
                    else:
                        return f"[turquoise2][MVP[/][{color_format[self.rankColour]}]+[/][turquoise2]] {self.name}[/] [orange1]joined the lobby![/]"


#msg = ChatMessage.Hypixel.HypixelBedwarsLobby(bw_message)
#msg.debugPrint()
