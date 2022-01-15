from pyrogram import Client, filters
import time

api_id = ...
api_hash = ...
app = Client("UBot", api_id, api_hash)
prefix = '*'

# Calculator
@app.on_message(filters.me & filters.command(commands='calc', prefixes=prefix))
def calc(app, message):
    app.edit_message_text(message.chat.id, message.message_id, f"{message.text[5:]} = {eval(message.text[5:])}")

# chatid
@app.on_message(filters.me & filters.command(commands='chatid', prefixes=prefix))
def chatid(app, message):
    app.edit_message_text(message.chat.id, message.message_id, message.chat.id)

# msginfo
@app.on_message(filters.me & filters.command(commands='msginfo', prefixes=prefix))
def msginfo(app, message):
    if message.reply_to_message:
        app.edit_message_text(message.chat.id, message.message_id, f"**Chat**: {message.chat.title} [--{message.chat.id}--]\n\n**Message ID**: --{message.reply_to_message.message_id}--\n**User ID**: -- {message.reply_to_message.from_user.id}-- [DC {message.reply_to_message.from_user.dc_id}]")

# Comando flood
@app.on_message(filters.me & filters.command(commands="flood", prefixes=prefix))
def flood(app, message):
    app.delete_messages(message.chat.id, message.message_id)
    for i in range(int(message.text.split()[1])):
        time.sleep(0.1)
        app.send_message(message.chat.id, " ".join(message.text.split()[2:]))

#comando dc
@app.on_message(filters.command(commands='dc', prefixes=prefix) & filters.me)
def dc(app, message):
    try:
        if message.reply_to_message:
            if message.reply_to_message.forward_from == None:
                info = message.reply_to_message.from_user
                app.edit_message_text(message.chat.id, message.message_id, f"Username: [{info.first_name}](tg://user?id={info.id})\nDC: {info.dc_id}")
            else:
                info = message.reply_to_message.forward_from
                app.edit_message_text(message.chat.id, message.message_id, f"Username: [{info.first_name}](tg://user?id={info.id})\nDC: {info.dc_id}")
        else:
            info = app.get_users(message.text.split(" ")[1])
            app.edit_message_text(message.chat.id, message.message_id, f"Username: [{info.first_name}](tg://user?id={info.id})\nDC: {info.dc_id}")
    except:
        app.delete_messages(message.chat.id, message.message_id)

app.run()