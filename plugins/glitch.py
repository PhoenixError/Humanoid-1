# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""

✘ Commands Available -

•`{i}glitch <replt to media>`
    gives a glitchy gif.

"""
import os

from . import *


@Humanoid_cmd(pattern="glitch$")
async def _(e):
    reply = await e.get_reply_message()
    if not (reply and reply.media):
        return await eor(e, "Reply to any media")
    wut = mediainfo(reply.media)
    if not wut.startswith(("pic", "sticker")):
        return await eor(e, "`Unsupported Media`")
    xx = await eor(e, "`Gliching...`")
    ok = await e.client.download_media(reply.media)
    cmd = f"glitch_me gif --line_count 200 -f 10 -d 50 '{ok}' Human.gif"
    stdout, stderr = await bash(cmd)
    await e.reply(file="Human.gif", force_document=False)
    await xx.delete()
    os.remove(ok)
    os.remove("Human.gif")
