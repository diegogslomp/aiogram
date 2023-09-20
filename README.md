### Finite State Machine Telegram Bot

Standalone
```sh
git clone --single-branch https:/github.com/diegogslomp/aiogram bot
cd bot
pip install aiogram
TELEGRAM_TOKEN='' TELEGRAM_USERS='{"user1": 1122334455}' python bot.py
```

As django app
```sh
cd django-project
git clone --single-branch https:/github.com/diegogslomp/aiogram bot
pip install aiogram
# Add _env keys to environment
# Add bot app inside project config
python run manage.py bot
```
