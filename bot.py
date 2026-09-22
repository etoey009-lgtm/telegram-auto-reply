import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = os.environ["BOT_TOKEN"]

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "ราคา" in text:
        answer = "สวัสดีครับ 😊 สินค้าของเราราคา 299 บาทครับ"

    elif "ค่าส่ง" in text:
        answer = "ค่าส่งเริ่มต้น 40 บาทครับ 📦"

    elif "สั่งซื้อ" in text or "สั่ง" in text:
        answer = "หากต้องการสั่งซื้อ แจ้งชื่อสินค้าและจำนวนที่ต้องการได้เลยครับ 😊"

    elif "เปิด" in text or "เวลา" in text:
        answer = "ร้านเปิดทุกวัน 09:00–18:00 น.ครับ"

    else:
        answer = "สวัสดีครับ 😊 สอบถามเรื่องสินค้า ราคา หรือวิธีสั่งซื้อได้เลยครับ"

    await update.message.reply_text(answer)

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
