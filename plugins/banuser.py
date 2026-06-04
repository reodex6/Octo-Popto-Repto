# Don't Remove Credit @MarsaNetwork, @BeingMarsa
# Ask Doubt on telegram @MarsaAdminContactBot
#
# Copyright (C) 2025 by BeingMarsa@Github, < https://github.com/BeingMarsa >.
#

import asyncio
import os
import random
import sys
import time
from datetime import datetime, timedelta
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode, ChatAction
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardMarkup, ChatInviteLink, ChatPrivileges
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserNotParticipant
from bot import Bot
from config import *
from helper_func import *
from database.database import *



#BAN-USER-SYSTEM
@Bot.on_message(filters.private & filters.command('ban') & admin)
async def add_banuser(client: Client, message: Message):        
    pro = await message.reply("⏳ <i>Banning User...</i>", quote=True)
    banuser_ids = await db.get_ban_users()
    banusers = message.text.split()[1:]

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ CLOSE", callback_data="close")]])

    if not banusers:
        return await pro.edit(
            "<b>❗ You must provide User ID to ban.</b>\n\n"
            "<b>📌 USAGE:</b>\n"
            "<code>/ban [user_id]</code> — Ban one or more users by ID.",
            reply_markup=reply_markup
        )

    report, success_count = "", 0
    for uid in banusers:
        try:
            uid_int = int(uid)
        except:
            report += f"⚠️ Invalid ID: <code>{uid}</code>\n"
            continue

        if uid_int in await db.get_all_admins() or uid_int == OWNER_ID:
            report += f"⛔ Skipped Admin ID: <code>{uid_int}</code>\n"
            continue

        if uid_int in banuser_ids:
            report += f"⚠️ ALready : <code>{uid_int}</code>\n"
            continue

        if len(str(uid_int)) == 10:
            await db.add_ban_user(uid_int)
            report += f"✅ Banned: <code>{uid_int}</code>\n"
            success_count += 1
        else:
            report += f"⚠️ Invalid Telegram ID length: <code>{uid_int}</code>\n"

    if success_count:
        await pro.edit(f"<b>✅ Banned Users Updated:</b>\n\n{report}", reply_markup=reply_markup)
    else:
        await pro.edit(f"<b>❌ No users were banned.</b>\n\n{report}", reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.command('unban') & admin)
async def delete_banuser(client: Client, message: Message):        
    pro = await message.reply("⏳ <i>Unbaning User...</i>", quote=True)
    banuser_ids = await db.get_ban_users()
    banusers = message.text.split()[1:]

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ CLOSE", callback_data="close")]])

    if not banusers:
        return await pro.edit(
            "<b>❗ Please provide User ID to unban.</b>\n\n"
            "<b>📌 USAGE:</b>\n"
            "<code>/unban [user_id]</code> — Unban specific user(s)\n"
            "<code>/unban all</code> — Remove all banned users",
            reply_markup=reply_markup
        )

    if banusers[0].lower() == "all":
        if not banuser_ids:
            return await pro.edit("<b>✅ No users in the banned list.</b>", reply_markup=reply_markup)
        for uid in banuser_ids:
            await db.del_ban_user(uid)
        listed = "\n".join([f"✅ Unbanned: <code>{uid}</code>" for uid in banuser_ids])
        return await pro.edit(f"<b>🚫 Cleared Banned list:</b>\n\n{listed}", reply_markup=reply_markup)

    report = ""
    for uid in banusers:
        try:
            uid_int = int(uid)
        except:
            report += f"⚠️ Invalid ID: <code>{uid}</code>\n"
            continue

        if uid_int in banuser_ids:
            await db.del_ban_user(uid_int)
            report += f"✅ Unbanned: <code>{uid_int}</code>\n"
        else:
            report += f"⚠️ Not in Banned List: <code>{uid_int}</code>\n"

    await pro.edit(f"<b>🚫 Unban Report:</b>\n\n{report}", reply_markup=reply_markup)

@Bot.on_message(filters.private & filters.command('banlist') & admin)
async def get_banuser_list(client: Client, message: Message):        
    pro = await message.reply("⏳ <i>Getting Ban list...</i>", quote=True)
    banuser_ids = await db.get_ban_users()

    if not banuser_ids:
        return await pro.edit("<b>✅ No users in ban list.</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ CLOSE", callback_data="close")]]))

    result = "<b>🚫 Banned Users:</b>\n\n"
    for uid in banuser_ids:
        await message.reply_chat_action(ChatAction.TYPING)
        try:
            user = await client.get_users(uid)
            user_link = f'<a href="tg://user?id={uid}">{user.first_name}</a>'
            result += f"• {user_link} — <code>{uid}</code>\n"
        except:
            result += f"• <code>{uid}</code> — <i>Could not fetch name</i>\n"

    await pro.edit(result, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ CLOSE", callback_data="close")]]))
