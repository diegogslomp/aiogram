### Finite State Machine Telegram Bot

Docker
````sh
docker run --rm -e TELEGRAM_TOKEN='' -e TELEGRAM_USERS='{"user": 1122334455}' diegogslomp/bot
````
Local dev
```sh
git clone --single-branch https:/github.com/diegogslomp/bot bot
cd bot
pip install -r requirements.txt
TELEGRAM_TOKEN='' TELEGRAM_USERS='{"user": 1122334455}' python bot.py
```

Django app
```sh
cd django-project
git clone --single-branch https:/github.com/diegogslomp/bot bot
pip install -r requirements.txt
# Add _env keys to environment
# Add bot app in project settings
python run manage.py bot
```
Chat `/start` `/cancel` or any for echo message
