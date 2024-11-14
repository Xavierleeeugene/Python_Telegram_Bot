## MINI TELEGRAM BOT

This project features a simple telgram bot using Python and mongoDB for user data storage.

### Tech Stack Used
Python

mongoDB

Aiogram

### Steps to Run the Bot:

1. Create Bot using @BotFather on Telegram
    - Type in /newbot and type in the name and username of the bot.
    - Copy the token generated and paste it into TELEGRAM_BOT_API_KEY in config.py.
    - Type in /setcommands to set the commands. For the default template, you can paste the following in:
        
        subscribe - Subscribe to the bot

        unsubscribe - Unsubscribe from the bot

        check_subscription - Check subscription status

        dummy - Dummy command

2. Download and Start MongoDB
```
brew tap mongodb/brew
brew install mongodb-community@6.0
mongod --config /usr/local/etc/mongod.conf --fork      #adjust path accordingly. --fork to run it in the background
```

3. run bot.py
```
python3 bot.py
```

4. To stop mongoDB
```
ps aux | grep mongod    # Identify PID
kill <PID>
``` 


### Extra Information

### To view and interact with MongoDB:
- Example: View Subscribers 
    ```
    mongosh
    show databases
    use telegram_bot
    db.subscribers.find()
    ```