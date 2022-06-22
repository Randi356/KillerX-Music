# Credits by @FFmpegNotInstalled
# code by https://github.com/Randi356/KillerX-Music/new/Master/KillerXMusic/

from pyrogram import filters
from KillerXMusic import app


@app.on_message(filters.command('vcs'))
def spam(bot, message):
    app.send_photo(message.chat.id, "https://telegra.ph/file/5b27a30767835ebe6f988.jpg")
    app.send_photo(message.chat.id, "https://telegra.ph/file/a72e4bffc0bfc6dad74a8.jpg")
    app.send_photo(message.chat.id, "https://telegra.ph/file/6c64f8d2997f3c9969b90.jpg")
   
 # bisa spam 1000  
 # awokaawokwokaowkkwowowowkwkwlwkwkkwkw
