"""
This file creates Assistant's client.
"""

import os
from pyrogram import Client
from pyrogram.errors import FloodWait
from main.core import Core






class Bot(Core, Client):
    """ Assistant (Nora) """
    def __init__(self):
        super().__init__(
            name="Nora",
            api_id=self.API_ID,
            api_hash=self.API_HASH,
            bot_token=self.BOT_TOKEN
	)
        try:
            self.start()
            self.me = self.get_chat("me")
            self.id = self.me.id
            self.dc_id = self.me.dc_id
            self.name = self.me.first_name
            self.username = f"@{self.me.username}"
            self.bio = self.me.bio if self.me.bio else ""
            dp_name = f"dp_{self.id}.jpg"
            dp_path = f"./downloads/{dp_name}"
            if not os.path.exists(dp_path):
                self.pic = self.download_media(self.me.photo.big_file_id, dp_name) if self.me.photo else None
            self.is_bot = True
            self.stop()
        except FloodWait as e:
            pass

        self.__class__.__module__ = "pyrogram.client"
