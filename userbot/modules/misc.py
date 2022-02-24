from random import randint
from time import sleep
from os import execl
import asyncio
import sys
import os
import io
import sys
from userbot import ALIVE_NAME, UPSTREAM_REPO_URL, BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import register
from userbot.utils import time_formatter
import urllib
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
REPOLINK = str(
    UPSTREAM_REPO_URL) if UPSTREAM_REPO_URL else "https://github.com/SkylaIND/Skyla-Userbot"
# ============================================

opener = urllib.request.build_opener()
useragent = 'Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 Mobile Safari/537.36'
opener.addheaders = [('User-agent', useragent)]


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
        return
    index = randint(1, len(itemo) - 1)
    await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" +
                     itemo[index] + "`")


@register(outgoing=True, pattern="^.sleep ([0-9]+)$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    counter = int(time.pattern_match.group(1))
    await time.edit("`I am sulking and snoozing...`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    await event.edit("`Mematikan Skyla-Userbot....`")
    await asyncio.sleep(7)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n"
                                        "`Skyla-Userbot Telah Dimatikan`")
    await bot.disconnect()


@register(outgoing=True, pattern="^.restart$")
async def killdabot(event):
    await event.edit("`Restarting Skyla-Userbot...`")
    await asyncio.sleep(10)
    await event.delete()
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTARTBOT \n"
                                        "`Skyla-Userbot Telah Di Restart`")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    exit()


@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    await e.edit(
        "Here's Something for You to Read :\n"
        "\n[Skyla-Userbot Repo](https://github.com/SkylaIND/Skyla-Userbot/blob/Skyla-Userbot/README.md)"
        "\n[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-02)"
        "\n[Special - Note](https://telegra.ph/Special-Note-11-02)")


@register(outgoing=True, pattern="^.repeat (.*)")
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(' ', 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for i in range(0, replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "✠╼━━━━━━━❖━━━━━━━━✠ \n"
        "                **ɪ'ᴀᴍ ʀᴇᴘᴏ**\n"
        "         **☃️sᴋʏʟᴀ-ᴜsᴇʀʙᴏᴛ☃️** \n"
        "✠╼━━━━━━━❖━━━━━━━━✠ \n"
        "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
        "┣|•**ʀᴇᴘᴏ     :** [ɢɪᴛʜᴜʙ](https://github.com/SkylaIND/Skyla-Userbot)\n"
        "┣|•**ᴏᴡɴᴇʀ    :** [sᴋʏʟᴀ](t.me/Zxyune)\n"
        "┣|•**ꜱᴜᴘᴘᴏʀᴛ  :** [ꜱᴜᴘᴘᴏʀᴛ](https://t.me/skylasupport)\n"
        "┣|•**ᴄʜᴀɴɴᴇʟ  :** [ᴄʜᴀɴɴᴇʟ](https://t.me/SkylaIND)\n"
        "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
        "   **sᴇʟᴀᴍᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ**\n"
        "▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
    )


@register(outgoing=True, pattern=r"^\.string$")
async def repo_is_here(wannasee):
    """For .repo command, just returns the repo URL."""
    await wannasee.edit(
        f"➡ **GET STRING SESSION TELEGRAM :** [KLIK DISINI](https://t.me/StringSkylaBot)\n"
    )


@register(outgoing=True, pattern="^.raw$")
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit(
            "`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`")


@register(outgoing=True, pattern=r"^.reverse(?: |$)(\d*)")
async def okgoogle(img):
    """ For .reverse command, Google search images and stickers. """
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await bot.download_media(message, photo)
    else:
        await img.edit("`Harap Reply Di Gambar...`")
        return

    if photo:
        await img.edit("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await img.edit('`Gambar tidak di dukung`')
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = 'https://www.google.com/searchbyimage/upload'
        multipart = {
            'encoded_image': (name, open(name, 'rb')),
            'image_content': ''
        }
        response = requests.post(searchUrl,
                                 files=multipart,
                                 allow_redirects=False)
        fetchUrl = response.headers['Location']

        if response != 400:
            await img.edit("`Image successfully uploaded to Google. Maybe.`"
                           "\n`Parsing source now. Maybe.`")
        else:
            await img.edit("`Google told me to fuck off.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl +
                                 "&preferences?hl=en&fg=1#languages")
        guess = match['best_guess']
        imgspage = match['similar_images']

        if guess and imgspage:
            await img.edit(f"[{guess}]({fetchUrl})\n\n`Looking for images...`")
        else:
            await img.edit("`Couldn't find anything for your uglyass.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await img.client.send_file(entity=await
                                       img.client.get_input_entity(img.chat_id
                                                                   ),
                                       file=yeet,
                                       reply_to=img)
        except TypeError:
            pass
        await img.edit(
            f"[{guess}]({fetchUrl})\n\n[Visually similar images]({imgspage})")


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, 'html.parser')

    results = {'similar_images': '', 'best_guess': ''}

    try:
        for similar_image in soup.findAll('input', {'class': 'gLFyf'}):
            url = 'https://www.google.com/search?tbm=isch&q=' + \
                urllib.parse.quote_plus(similar_image.get('value'))
            results['similar_images'] = url
    except BaseException:
        pass

    for best_guess in soup.findAll('div', attrs={'class': 'r5a77d'}):
        results['best_guess'] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results['similar_images']).read()
    decoded = single.decode('utf-8')

    imglinks = []
    counter = 0

    pattern = r'^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$'
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if not counter >= int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks


CMD_HELP.update({
    "random": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.random <item1> <item2> ... <itemN>`\
    \n↳ : Dapatkan item acak dari daftar item.",
    "sleep": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sleep <seconds>`\
    \n↳ : `.sleep`\
    \n  •  **Function : Biarkan Kayzu-Ubot tidur selama beberapa detik.",
    "shutdown": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shutdown`\
    \n↳ : Mematikan bot",
    "repo": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.repo`\
    \n↳ : Menampilan link Repository Kayzu-Ubot.",
    "string": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.string`\
    \n↳: Menampilkan link String Kayzu-Ubot",
    "readme": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙 `.readme`\
    \n↳ : Menyediakan tautan untuk mengatur userbot dan modulnya.",
    "repeat": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.repeat <no> <text>`\
    \n↳ : Mengulangi teks untuk beberapa kali. Jangan bingung ini dengan spam tho.",
    "restart": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.restart`\
    \n↳ : Merestart bot",
    "raw": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.raw`\
    \n↳ : Dapatkan data berformat seperti JSON terperinci tentang pesan yang dibalas.",
})
