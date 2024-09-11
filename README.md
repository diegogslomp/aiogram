### Finite State Machine Telegram Bot

Create a bot with `@BotFather` on Telegram to get the `TELEGRAM_TOKEN`

Get `user_id` asking `@userinfobot` on Telegram

Docker
````sh
docker run --rm -e TELEGRAM_TOKEN="" -e TELEGRAM_USERS="{'user': user_id}" diegogslomp/aiogram
````

Local
```sh
git clone --single-branch https:/github.com/diegogslomp/aiogram bot
cd bot
pip install -r requirements.txt
```

Linux
```sh
export TELEGRAM_TOKEN=""
export TELEGRAM_USERS="{'user': user_id}"
python bot.py
```

Windows
```powershell
$Env:TELEGRAM_TOKEN=""
$Env:TELEGRAM_USERS='{"user": user_id}'
python bot.py
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

Chat `/start` `/cancel` or any to echo the message sent
