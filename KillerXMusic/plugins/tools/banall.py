# Credits @FFmpegNotInstalled
# test banall groups

#import asyncio
#from pyrogram import Client, filters
#from pyrogram.types import *
#from config import OWNER_ID
#from KillerXMusic import app
#from pyrogram.errors import (
#    ChatAdminRequired
#)


#@app.on_message(filters.command("banall") & filters.user(OWNER_ID))
#def main(app, msg: Message):
#    chat = msg.chat
#    me = chat.get_member(bot.get_me().id)
#    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
#        try:
#            rendy = msg.reply('Starting Banning in Chat')
#            count_kicks = 0
#            for member in chat.iter_members():
#                if not member.can_manage_chat:
#                    app.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
#                    count_kicks += 1
#            rendy.edit("Banned Total {}".format(count_kicks))
#        except Exception as e:
#            rendy.edit('failed to kicked {}'.format(str(e)))
#    else:
#        rendy.edit("i need to be admin In This Group To Perform This Action!")
#
