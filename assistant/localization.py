# Humanoid - UserBot
# Copyright (C) 2021 TeamHumanoid
#
# This file is a part of < https://github.com/TeamHumanoid/Humanoid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamHumanoid/Humanoid/blob/main/LICENSE/>.

import re

from . import *


@callback("lang")
@owner
async def setlang(event):
    languages = get_languages()
    tultd = [
        Button.inline(
            f"{languages[ult]['natively']} [{ult.lower()}]",
            data=f"set_{ult}",
        )
        for ult in languages
    ]
    buttons = list(zip(tultd[::2], tultd[1::2]))
    if len(tultd) % 2 == 1:
        buttons.append((tultd[-1],))
    buttons.append([Button.inline("« Back", data="mainmenu")])
    await event.edit("List Of Available Languages.", buttons=buttons)


@callback(re.compile(b"set_(.*)"))
@owner
async def settt(event):
    lang = event.data_match.group(1).decode("UTF-8")
    languages = get_languages()
    HumandB.set("language", f"{lang}")
    await event.edit(
        f"Your language has been set to {languages[lang]['natively']} [{lang}].",
        buttons=get_back_button("lang"),
    )
