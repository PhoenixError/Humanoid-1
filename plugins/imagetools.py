# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.
"""
✘ Commands Available -

• `{i}grey <reply to any media>`
    To make it black nd white.

• `{i}color <reply to any Black nd White media>`
    To make it Colorfull.

• `{i}toon <reply to any media>`
    To make it toon.

• `{i}danger <reply to any media>`
    To make it look Danger.

• `{i}negative <reply to any media>`
    To make negative image.

• `{i}blur <reply to any media>`
    To make it blurry.

• `{i}quad <reply to any media>`
    create a Vortex.

• `{i}mirror <reply to any media>`
    To create mirror pic.

• `{i}flip <reply to any media>`
    To make it flip.

• `{i}sketch <reply to any media>`
    To draw its sketch.

• `{i}blue <reply to any media>`
    just cool.

• `{i}csample <color name /color code>`
   example : `{i}csample red`
             `{i}csample #ffffff`
"""
import asyncio
import os

import cv2
import numpy as np
from PIL import Image
from telegraph import upload_file as upf
from telethon.errors.rpcerrorlist import (
    ChatSendMediaForbiddenError,
    MessageDeleteForbiddenError,
)
from validators.url import url

from . import *


@Humanoid_cmd(
    pattern="sketch$",
)
async def sketch(e):
    ureply = await e.get_reply_message()
    xx = await eor(e, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("Humanoid.png", pencil_sketch_IMG)
    await e.reply(file="Humanoid.png")
    await xx.delete()
    os.remove(file)
    os.remove("Humanoid.png")


@Humanoid_cmd(pattern="color$")
async def _(event):
    reply = await event.get_reply_message()
    if not reply.media:
        return await eor(event, "`Reply To a Black nd White Image`")
    xx = await eor(event, "`Coloring image 🎨🖌️...`")
    image = await reply.download_media()
    img = cv2.VideoCapture(image)
    ret, frame = img.read()
    cv2.imwrite("Human.jpg", frame)
    if HumandB.get("DEEP_API"):
        key = Redis("DEEP_API")
    else:
        key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"
    r = requests.post(
        "https://api.deepai.org/api/colorizer",
        files={"image": open("Human.jpg", "rb")},
        headers={"api-key": key},
    )
    os.remove("Human.jpg")
    os.remove(image)
    if "status" in r.json():
        return await event.edit(
            r.json()["status"] + "\nGet api nd set `{i}setredis DEEP_API key`"
        )
    r_json = r.json()["output_url"]
    await event.client.send_file(event.chat_id, r_json, reply_to=reply)
    await xx.delete()


@Humanoid_cmd(
    pattern="grey$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        await eor(event, "`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        xx = await eor(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        xx = await eor(event, "`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    Humanoid = cv2.cvtColor(Human, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="blur$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    if not (ureply and (ureply.media)):
        await eor(event, "`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        xx = await eor(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        xx = await eor(event, "`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    Humanoid = cv2.GaussianBlur(Human, (35, 35), 0)
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="negative$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    Humanoid = cv2.bitwise_not(Human)
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="mirror$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    ish = cv2.flip(Human, 1)
    Humanoid = cv2.hconcat([Human, ish])
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="flip$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    trn = cv2.flip(Human, 1)
    ish = cv2.rotate(trn, cv2.ROTATE_180)
    Humanoid = cv2.vconcat([Human, ish])
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="quad$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    roid = cv2.flip(Human, 1)
    mici = cv2.hconcat([Human, roid])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    Humanoid = cv2.vconcat([mici, trn])
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="toon$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    height, width, channels = Human.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = Human[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    ish = centers[labels.flatten()]
    Humanoid = ish.reshape(Human.shape)
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(
    pattern="danger$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    Human = cv2.imread(file)
    dan = cv2.cvtColor(Human, cv2.COLOR_BGR2RGB)
    Humanoid = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("Human.jpg", Humanoid)
    await event.client.send_file(
        event.chat_id,
        "Human.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.jpg")
    os.remove(Humant)


@Humanoid_cmd(pattern="csample (.*)")
async def sampl(Human):
    color = Human.pattern_match.group(1)
    if color:
        img = Image.new("RGB", (200, 100), f"{color}")
        img.save("csample.png")
        try:
            try:
                await Human.delete()
                await Human.client.send_message(
                    Human.chat_id, f"Colour Sample for `{color}` !", file="csample.png"
                )
            except MessageDeleteForbiddenError:
                await Human.reply(f"Colour Sample for `{color}` !", file="csample.png")
        except ChatSendMediaForbiddenError:
            await eor(Human, "Umm! Sending Media is disabled here!")

    else:
        await eor(Human, f"Wrong Color Name/Hex Code specified!")


@Humanoid_cmd(
    pattern="blue$",
)
async def Humand(event):
    ureply = await event.get_reply_message()
    xx = await eor(event, "`...`")
    if not (ureply and (ureply.media)):
        await xx.edit("`Reply to any media`")
        return
    Humant = await ureply.download_media()
    if Humant.endswith(".tgs"):
        await xx.edit("`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", Humant, "Human.png"]
        file = "Human.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit("`Processing...`")
        img = cv2.VideoCapture(Humant)
        heh, lol = img.read()
        cv2.imwrite("Human.png", lol)
        file = "Human.png"
    got = upf(file)
    lnk = f"https://telegra.ph{got[0]}"
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=blurpify&image={lnk}",
    ).json()
    ms = r.get("message")
    utd = url(ms)
    if not utd:
        return
    with open("Human.png", "wb") as f:
        f.write(requests.get(ms).content)
    img = Image.open("Human.png").convert("RGB")
    img.save("Human.webp", "webp")
    await event.client.send_file(
        event.chat_id,
        "Human.webp",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xx.delete()
    os.remove("Human.png")
    os.remove("Human.webp")
    os.remove(Humant)
