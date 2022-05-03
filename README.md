# 🤖 xBot Telegram Bot

Telegram bot that allows you to moderate a group chat and send notifications about new YouTube videos to it.

## ⭐️ Features

- Sending reports along with comments from a member chat
- Displaying informational messages (such as rules and available bot commands)
- Attracting the attention of admins
- Opportunities for admins to issue bans and mutes to members
- Setting Rules and Welcome Message
- Collection of reports in the admin chat

## ⚙️ Installation and configuration

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Loureas/xBot
    ```

2. Install required dependencies:

    **Poetry:**

    ```sh
    poetry install
    ```

    **PIP:**

    ```sh
    python -m pip install -U -r requirements.txt
    ```
    > On GNU/Linux, usually the latest version of Python is run with commands such as: `python3`, `python3.7`

### Configuration

Get all the credentials you need, open the `.env` file and fill in the empty environment variables:

```sh
# General
LANG=ru

# Telegram
TOKEN=<bot-token>
MAIN_CHAT=<main-chat-id> # The main chat, where there will be moderation, members and the arrival of notifications about new videos
ADMIN_CHAT=<admin-chat-id> # Admin chat where reports will be sent. Through this chat rules and greetings are sets

# YouTube
GOOGLE_API_KEY=<api-key> # How to get a key learn here https://developers.google.com/youtube/v3/getting-started
CHANNEL_NAME=<channel-name> # YouTube channel name
CHANNEL_URL=<channel-url> # YouTube channel url
CHANNEL_ID=<channel-id> # YouTube channel ID
UPDATE_INTERVAL=25 # Update interval for new videos in minutes

# Information files
RULES_FILE=rules.txt
WELCOME_FILE=welcome.txt
```

## 📝 Launch and usage

Launch the bot via:

**Poetry:**

```sh
poetry run python main.py
```

**Python:**

```sh
python main.py
```

After launch, it is recommended to set the rules and welcome message via the admin chat using these commands:

```
/setrules rules text - set rules (formatting allowed)
/setwelcome welcome text - set welcome message (formatting allowed)
```

Other commands for main chat:

```
/rules - display rules
/help - display available commands
/report [comment up to 100 characters] - send a complaint about the user (a response message is required)
/attention - attract the attention of admins (optionally with a response message)
/mute [1h - hour, 1d - day, 1w - week] - Mute the user (needs a response message, only for admins)
/ban - Issue a ban to the user (a response message is required, only for admins)
```

* * *

## 🆘 Issues
If you have any problems while installing, configuring or launching bot, you can create a new issue on GitHub.

## 🔧 Contribution
You can help improve the bot or translate it. Publish changes in Pull Request. All changes will be reviewed.

