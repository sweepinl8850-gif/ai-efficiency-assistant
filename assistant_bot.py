#!/usr/bin/env python3
"""
🤖 AI Efficiency Assistant — Telegram Bot
@AI_Efficiency_Assistant_bot
Built with integrity — MIT License
"""
import os
import asyncio
import ollama
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
MODEL = "qwen:7b"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = """🤖 AI Efficiency Assistant — LIVE! ✅

Hello! I'm your personal productivity companion.

✨ What I can do:
• Summarize long messages & documents
• Turn notes into organized to-do lists
• Answer questions using local AI
• All data stays private — never shared

🧠 Powered by: qwen:7b
💎 Open-source: MIT License
⭐ GitHub: https://github.com/sweepinl8850-gif/ai-efficiency-assistant

Sponsor: https://github.com/sponsors/sweepinl8850-gif

Send me any message! ⚡
"""
    await update.message.reply_text(welcome)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.effective_message.text
    await update.message.chat.send_action(action="typing")

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": user_text}]
        )
        reply = response["message"]["content"]
        await update.message.reply_text(reply[:4000])
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)[:80]}")

async def main():
    print("🚀 AI Efficiency Assistant — Starting...")
    print(f"🤖 Bot: @AI_Efficiency_Assistant_bot")
    print(f"🧠 Model: {MODEL}")
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    print("✅ READY — Message me on Telegram!")
    
    # Run forever
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
