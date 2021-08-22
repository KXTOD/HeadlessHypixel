#!/usr/bin/env python
import regex as re
import sys
from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound
import json
from rich import print
from dotenv import load_dotenv
import os


def main():
    load_dotenv("crd.env")
    USR = os.getenv('USR')
    PSS = os.getenv('PSS')
    auth_token = authentication.AuthenticationToken()
    try:
        auth_token.authenticate(USR, PSS)
    except YggdrasilError as e:
        print(e)
        sys.exit()
    print(f"Logged in as {auth_token.username}...")
    connection = Connection("play.hypixel.net", 25565, auth_token=auth_token)


    def handle_join_game(join_packet):
        print('[bold green] Connected..')

    connection.register_packet_listener(handle_join_game, clientbound.play.JoinGamePacket)

    def print_chat(chat_packet):
        json_data = json.loads(chat_packet.json_data)
        clr_dict = {"§4": "dark_red", "§c": "red", "§6": "orange1", "§e": "bright_yellow", "§2": "dark_green", "§a": "green",
                    "§b": "turquoise2", "§3": "sky_blue3", "§1": "dark_blue", "§9": "blue", "§d": "pink",
                    "§5": "purple", "§f": "bright_white", "§7": "white", "§8": "bright_black", "§0": "black",
                    "§r": "bright_white", "§l": "bold", "§o": "italic", "§n": "underline", "§m": "strike", "§k": ""}

        try:

            if json_data["extra"][0]["text"] == " §b>§c>§a>§r ":
                string = json_data["extra"][1]['text']
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
                chatmsg = f"[turquoise2]>[/][red]>[/][green]>[/] [{clr[0]}][MVP[/][{clr[1]}]++[/][{clr[2]}]] {name}[/] [{clr[3]}][/][{clr[4]}]joined the lobby! [/] [green]<[/][red]<[/][turquoise2]<[/]"
                print(chatmsg)
            elif json_data['text'] == "Friend > ":
                try:
                    username = json_data['extra'][0]['text']
                    username_color = json_data['extra'][0]['color']
                    correct_color = {"green": "green1", "aqua": "turquoise2", "orange": "orange1", "gray": "bright_black"}
                    status = json_data['extra'][1]['text']
                    chatmsg = f"[green1]Friend > [/][{correct_color[username_color]}]{username}[/][bright_yellow]{status}[/]"
                    print(chatmsg)
                except Exception as e:
                    print(e)
            else:
                string = json_data["extra"][0]['text']
                clr = []
                for index, item in enumerate(string):
                    if item == "]":
                        regex_index = re.match("([^\s]+)", string[index + 2:]).span()
                        name = string[index + 2:index + 2 + regex_index[1] - 2]

                for item in [pos for pos, char in enumerate(string) if char == "§"]:
                    if string[item:item + 2] in clr_dict:
                        clr.append(clr_dict[string[item:item + 2]])

                chatmsg = f"[{clr[0]}][MVP[/][{clr[1]}]+[/][{clr[2]}]] {name}[/] [{clr[3]}][/][{clr[4]}]joined the lobby! [/]"
                print(f"{chatmsg}")

        except Exception:
            print(json_data)


    connection.register_packet_listener(print_chat, clientbound.play.ChatMessagePacket)
    connection.connect()

    while True:
        try:
            text = input()
            packet = serverbound.play.ChatPacket()
            packet.message = text
            connection.write_packet(packet)
        except KeyboardInterrupt:
            print("Disconnecting...")
            sys.exit()


if __name__ == "__main__":
    main()
