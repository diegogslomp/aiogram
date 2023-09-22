### Finite State Machine Telegram Bot

Docker
````sh
docker run --rm -e TELEGRAM_TOKEN="" -e TELEGRAM_USERS="{'user': 1122334455}" diegogslomp/aiogram
````
Local
```sh
git clone --single-branch https:/github.com/diegogslomp/aiogram bot
cd bot
pip install -r requirements.txt
TELEGRAM_TOKEN="" TELEGRAM_USERS="{'user': 1122334455}" python bot.py
```

Django
```sh
cd django-project
git clone --single-branch https:/github.com/diegogslomp/aiogram bot
cd bot
pip install -r requirements.txt
# Add _env keys to environment
# Add bot app in project settings
python run manage.py bot
```
Chat `/start` `/cancel` or any for echo message
