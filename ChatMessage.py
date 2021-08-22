from rich import print
import regex as re
import json

n = None

rank_colors = {"VIP": "green1", "VIP+": "green1",
               "MVP": "turquoise2", "MVP+": "turquoise2",
               "MVP++": "orange1",
               None: "bright_black", "None": "bright_black", "non": "bright_black"}

color_format = {"4": "dark_red", "c": "red", "6": "orange1", "e": "bright_yellow", "2": "dark_green",
                "a": "green", "b": "turquoise2", "3": "sky_blue3", "1": "dark_blue", "9": "blue", "d": "pink",
                "5": "purple", "f": "bright_white", "7": "white", "8": "bright_black", "0": "black",
                "r": "bright_white", "l": "bold", "o": "italic", "n": "underline", "m": "strike", "k": ""}

correct_color = {"green": "green1", "aqua": "turquoise2", "orange": "orange1",
                 "gray": "bright_black", "red": "bright_red", "dark_green": "dark_green"}

# Main class
class ChatMessage:
    # Server

    class Hypixel:
        # World

        class HypixelSkywarsLobby:
            def __init__(self):
                pass

        class Global:
            class MysteryBoxes:
                def __init__(self, json_string):
                    self.username_color = n
                    self.username = n
                    self.rating = n
                    self.patchecolor = n

                    # Gets username
                    self.username = json_string['text']

                    # Gets username color and patches it
                    self.username_color = json_string['color']

                    try:
                        self.patchedcolor = correct_color[self.username_color]
                    except KeyError:
                        self.patchedcolor = "bright_white"

                    # Gets rating
                    self.rating = json_string['extra'][1]['text']

                def debugPrint(self):
                    print(f"Name: {self.username}\nColor: {self.username_color}\nCorrect color: {self.patchedcolor}\n")

                def formatted(self):
                    return f"[{correct_color[self.username_color]}]{self.username}[/][bright_yellow]found a {self.rating}[/][turquoise2]Mystery Box[/][bright_white]![/]"

            class LobbyJoinMessage:
                def __init__(self, json_string):
                    json_data = json.loads(json_string)

                    self.name = n
                    self.rank = n
                    self.rankColour = n
                    self.uuid = n
                    self.network_level = n
                    self.ach_pts = n
                    self.guild = n

                    # Checks and sets rank
                    if json_data["extra"][0]["text"] == " §b>§c>§a>§r ":
                        self.rank = "MVP++"
                        string = json_data["extra"][1]
                    else:
                        self.rank = "MVP+"
                        string = json_data["extra"][0]

                    # Sets name
                    startPoint = n
                    for index, item in enumerate(string["text"]):
                        if item == "]" and startPoint is None:
                            startPoint = index + 2
                        elif startPoint is not None:
                            if item == "§":
                                endPoint = index
                                self.name = string["text"][startPoint:endPoint]

                        if self.name is not None:
                            break

                        if index == len(string) and self.name is not None:
                            print("ERROR: Could not find name.")

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
