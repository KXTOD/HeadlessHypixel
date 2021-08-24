#!/usr/bin/env python
import sys
from minecraft import authentication
from minecraft.exceptions import YggdrasilError
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound
import json
from rich import print
from dotenv import load_dotenv
import os
from ChatMessage import ChatMessage


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
        # Todo fix friends message not being detected
        # Todo fix bedwars message not being detected
        try:
            private_message_matches = ["From ", "To "]
            if any(ext in json_data['text'] for ext in private_message_matches) and json_data[
                'color'] == "light_purple":
                print(ChatMessage.Hypixel.Global.PrivateMessage(json_string=json_data).formatted())
            elif json_data['extra'][0]['text'] == " §b>§c>§a>§r " or "§6joined the lobby!" in json_data['extra'][0][
                'text']:
                print(ChatMessage.Hypixel.Global.LobbyJoinMessage(json_dict=json_data).formatted())
            elif json_data['extra'][2]['text'] == "Mystery Box" or json_data['extra'][3]['text'] == "Mystery Box" and \
                    json_data['extra'][2]['color'] == "aqua" or json_data['extra'][3]['color'] == "aqua":
                print(ChatMessage.Hypixel.Global.MysteryBoxes(json_string=json_data).formatted())
            elif json_data['text'] == "Friend > " and json_data['color'] == "green":
                print(ChatMessage.Hypixel.Global.FriendStatus(json_string=json_data).formatted())
            elif "✫" in json_data['extra'][0]['text']:
                print("[bold orange1] found bw message")
                print(ChatMessage.Hypixel.HypixelBedwarsLobby(json_string=json_data).formatted())
            else:
                print(json_data)

        except Exception as e:
            print('[bold red]----------------ERROR------------------[/]')
            print(json_data)
            print(f"[bold red]Element causing the error: [/]{e}")
            print('[bold red]----------------ERROR------------------[/]')

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
