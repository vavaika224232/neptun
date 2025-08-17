import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from telegram import Bot
from telegram.ext import Application
import logging
import aiohttp
import asyncio
from datetime import datetime, timezone
import pytz
from lingua import Language, LanguageDetectorBuilder

# Загрузка переменных окружения
load_dotenv()

# Настройки
PORT = int(os.getenv('PORT', 10000))
HOST = os.getenv('HOST', '0.0.0.0')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')

# Инициализация Flask
app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Инициализация Telegram бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Инициализация детектора языка
detector = LanguageDetectorBuilder.from_languages(
    Language.RUSSIAN, 
    Language.UKRAINIAN, 
    Language.ENGLISH
).build()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).isoformat()
    })

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
