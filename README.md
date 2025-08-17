# Neptun Render

Оптимизированная версия проекта Neptun для развертывания на Render.

## Переменные окружения

Создайте в Render следующие переменные окружения:

```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_BOT_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_key
OPENCAGE_API_KEY=your_opencage_key
```

## Локальная разработка

1. Установите Python 3.9.18
2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Установите языковые модели:
```bash
python -m spacy download en_core_web_sm
python -m spacy download uk_core_news_sm
```

## Запуск

Для разработки:
```bash
python main.py
```

Для продакшена:
```bash
gunicorn wsgi:app --config gunicorn_config.py
```

## Деплой на Render

1. Подключите GitHub репозиторий в Render
2. Выберите тип сервиса: Web Service
3. Настройте переменные окружения
4. Дождитесь завершения деплоя

## Особенности версии для Render

1. Оптимизированная конфигурация Gunicorn
2. Настроенное кэширование
3. Правильная обработка временных зон
4. Логирование в stdout для Render
5. Правильная обработка HTTPS
6. Оптимизированное использование памяти
