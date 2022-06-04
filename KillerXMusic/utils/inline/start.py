#
# Copyright (C) 2021-2022 by TeamKillerX@Github, < https://github.com/TeamKillerX >.
#
# This file is part of < https://github.com/TeamKillerX/KillerXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamKillerX/KillerXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

 from typing import Union

 from pyrogram.types import InlineKeyboardButton
 from KillerXMusic import app

 from config import (
    GITHUB_REPO, 
    SUPPORT_CHANNEL, 
    SUPPORT_GROUP, 
    START_IMG_URL
) 


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"],
                url=f"https://t.me/t.me/VegetaSupports",
            ),
            InlineKeyboardButton(
                text=_["S_B_10"], url=f"https://t.me/RendyProjects",
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(
    _, 
    BOT_USERNAME, 
    START_IMG_URL,
   OWNER: Union[bool, int] = None
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            ), 
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_9"], url=f"https://t.me/VegetaSupports"
            ), 
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ], 
            [
                InlineKeyboardButton(
                    text=_["S_B_9"], url=f"https://t.me/VegetaSupports"
               ), 
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text=_["S_B_9"], url=f"https://t.me/VegetaSupports"
                    ), 
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons
