from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently Only supports Youtube Single  (No playlist) Just Send Youtube Url.Join @XStream_Flix for movies/series🎬."
    await message.reply_text(helptxt)
