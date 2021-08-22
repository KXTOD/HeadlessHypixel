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
import ChatMessage

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
            msg = ChatMessage.ChatMessage.Hypixel.Global.LobbyJoinMessage(json_data)
            print(msg.formatted())
        except Exception as e:
            print('[bold red]------------------ERROR------------------[/]')
            print(json_data)
            print(f"[bold red]Element causing the error: [/]{e}")
            print('[bold red]------------------ERROR------------------[/]')

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
