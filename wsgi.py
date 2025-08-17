from main import app

# Для корректной работы с asyncio в gunicorn
async def app_wrapper(scope, receive, send):
    await app(scope, receive, send)

if __name__ == "__main__":
    app.run()
