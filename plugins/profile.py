# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}setname <first name // last name>`
    Change your profile name.

• `{i}setbio <bio>`
    Change your profile bio.

• `{i}setpic <reply to pic>`
    Change your profile pic.

• `{i}delpfp <n>(optional)`
    Delete one profile pic, if no value given, else delete n number of pics.

• `{i}poto <username>`
    Upload the photo of Chat/User if Available.
"""
import asyncio
import os

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import (
    DeletePhotosRequest,
    GetUserPhotosRequest,
    UploadProfilePhotoRequest,
)
from telethon.tl.types import InputPhoto

from . import *

TMP_DOWNLOAD_DIRECTORY = "resources/downloads/"

# bio changer


@Humanoid_cmd(
    pattern="setbio ?(.*)",
)
async def _(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command Is Sudo Restricted.`")
    ok = await eor(Human, "...")
    set = Human.pattern_match.group(1)
    try:
        await Human.client(UpdateProfileRequest(about=set))
        await ok.edit(f"Profile bio changed to\n`{set}`")
    except Exception as ex:
        await ok.edit("Error occured.\n`{}`".format(str(ex)))
    await asyncio.sleep(10)
    await ok.delete()


# name changer


@Humanoid_cmd(
    pattern="setname ?((.|//)*)",
)
async def _(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command Is Sudo Restricted.`")
    ok = await eor(Human, "...")
    names = Human.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "//" in names:
        first_name, last_name = names.split("//", 1)
    try:
        await Human.client(
            UpdateProfileRequest(
                first_name=first_name,
                last_name=last_name,
            ),
        )
        await ok.edit(f"Name changed to `{names}`")
    except Exception as ex:
        await ok.edit("Error occured.\n`{}`".format(str(ex)))
    await asyncio.sleep(10)
    await ok.delete()


# profile pic


@Humanoid_cmd(
    pattern="setpic$",
)
async def _(Human):
    if not Human.out and not is_fullsudo(Human.sender_id):
        return await eod(Human, "`This Command Is Sudo Restricted.`")
    if not Human.is_reply:
        return await eod(Human, "`Reply to a Media..`")
    reply_message = await Human.get_reply_message()
    ok = await eor(Human, "...")
    replfile = await reply_message.download_media()
    file = await Human.client.upload_file(replfile)
    mediain = mediainfo(reply_message.media)
    try:
        if "pic" in mediain:
            await Human.client(UploadProfilePhotoRequest(file))
        elif "gif" or "video" in mediain:
            await Human.client(UploadProfilePhotoRequest(video=file))
        else:
            return await ok.edit("`Invalid MEDIA Type !`")
        await ok.edit("`My Profile Photo has Successfully Changed !`")
    except Exception as ex:
        await ok.edit("Error occured.\n`{}`".format(str(ex)))
    os.remove(replfile)
    await asyncio.sleep(10)
    await ok.delete()


# delete profile pic(s)


@Humanoid_cmd(
    pattern="delpfp ?(.*)",
)
async def remove_profilepic(delpfp):
    if not delpfp.out and not is_fullsudo(delpfp.sender_id):
        return await eod(delpfp, "`This Command Is Sudo Restricted.`")
    ok = await eor(delpfp, "...")
    group = delpfp.text[8:]
    if group == "all":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.from_id, offset=0, max_id=0, limit=lim),
    )
    input_photos = []
    for sep in pfplist.photos:
        input_photos.append(
            InputPhoto(
                id=sep.id,
                access_hash=sep.access_hash,
                file_reference=sep.file_reference,
            ),
        )
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await ok.edit(f"`Successfully deleted {len(input_photos)} profile picture(s).`")
    await asyncio.sleep(10)
    await ok.delete()


@Humanoid_cmd(pattern="poto ?(.*)")
async def gpoto(e):
    Human = e.pattern_match.group(1)
    a = await eor(e, "`Processing...`")
    if not Human and e.is_reply:
        gs = await e.get_reply_message()
        Human = gs.sender_id
    if not (Human or e.is_reply):
        Human = e.chat_id
    try:
        okla = await e.client.download_profile_photo(
            Human,
            "profile.jpg",
            download_big=True,
        )
        await a.delete()
        await e.reply(file=okla)
        os.remove(okla)
    except Exception as er:
        await eor(e, f"ERROR - {str(er)}")
