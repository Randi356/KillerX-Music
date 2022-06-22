# Credits by @FFmpegNotInstalled
from pyrogram import filters
from KillerXMusic import app

# blacklist text
@app.on_message(filters.text)
def delete_text(app, message):
 #     bot.delete_messages(message.chat.id, message.message_id)
     word_list = ["bokep", "vcs", "desah", "/play desah",] # list random blacklist
     if message.text in word_list:
        app.delete_messages(message.chat.id, message.message_id)
        app.send_message(message.chat.id, "blacklisted blocked")
        delete.close()
