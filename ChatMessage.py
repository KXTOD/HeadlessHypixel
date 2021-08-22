import json
n = None


# Main class
class ChatMessage:
    # Server

    class Hypixel:
        # World

        class HypixelSkywarsLobby:
            def __init__(self):
                pass

        class Global:
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
                    startPoint = endPoint = n
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
                    startPoint = n
                    for index, item in enumerate(string["text"]):
                        if item == "+":
                            self.rankColour = string["text"][index-1]
                            break
                        if index == len(string) and self.rankColour is not None:
                            print("ERROR: Could not find + color.")

                    # Sets network level
                    startPoint = endPoint = n
                    hoverEventText = string["hoverEvent"]["value"]["text"]
                    for index, item in enumerate(hoverEventText):
                        if hoverEventText[index:index + 7] == " Level:" and startPoint is None:
                            startPoint = index + 10
                        elif startPoint is not None:
                            if hoverEventText[index:index + 13] == "§7Achievement":
                                endPoint = index - 1
                                self.network_level = hoverEventText[startPoint:endPoint]
                                break

                        if index == len(hoverEventText):
                            print("ERROR: Could not find network level.")

                    # Sets achievement points
                    startPoint = endPoint = n
                    for index, item in enumerate(hoverEventText):
                        if hoverEventText[index:index + 8] == " Points:" and startPoint is None:
                            startPoint = index + 11
                        elif startPoint is not None:
                            if hoverEventText[index:index + 8] == "§7Guild:":
                                endPoint = index - 1
                                self.ach_pts = hoverEventText[startPoint:endPoint]
                                break

                        if index == len(hoverEventText):
                            print("ERROR: Could not find achievement points.")

                    # Sets guild
                    startPoint = endPoint = n
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
