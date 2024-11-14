<h1 align="center">Mini Telegram Bot</h1>

### 📍 Objective
- This project features a simple telgram bot using Python and mongoDB for user data storage.

### 🖥 Tech Stack
-   `python` - Asynchronous logic for handling Telegram bot interactions and commands
-   `mongoDB` - NoSQL database used for storing and retrieving data
-   `aiogram` — asynchronous framework for Telegram Bot API

### ⚙ Configurations
| name                     | description                                                                                 |
| ------------------------ | ------------------------------------------------------------------------------------------- |
| `TELEGRAM_BOT_API_KEY`   | Telegram bot API token                                                                      |
| `MONGO_URI`              | Connection string used to connect to the MongoDB database                                   |

### 🚀 Steps to Run the Bot Locally:

1. Create Bot using @BotFather on Telegram
    - Type in /newbot and type in the name and username of the bot.
    - Copy the token generated and paste it into TELEGRAM_BOT_API_KEY in config.py.
    - Type in /setcommands to set the commands. For the default template, you can paste the following in:
        
        subscribe - Subscribe to the bot

        unsubscribe - Unsubscribe from the bot

        check_subscription - Check subscription status

        dummy - Dummy command

2. Download and Start MongoDB
    - Adjust path accordingly. 
    - --fork runs the database in the background
    ```bash
    brew tap mongodb/brew
    brew install mongodb-community@6.0
    mongod --config /usr/local/etc/mongod.conf --fork
    ```

3. run bot.py
    ```bash
    python3 bot.py
    ```

4. To stop mongoDB
    ```bash
    ps aux | grep mongod
    kill <PID>
    ``` 



### 📝 Extra Information

### To view and interact with MongoDB:
- Example: View Subscribers 
    ```bash
    mongosh
    show databases
    use telegram_bot
    db.subscribers.find()
    ```