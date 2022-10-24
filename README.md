# About

It is a python bot that will check availability of a Canyon bike for you.
Add a link to the bike that you want. Start the bot. Run `\notify` in the bot.
It will inform you if the status of any of your tracked bikes has changed

## What differentiates this fork from the main project?

* the application is now a python package being configured via environment variables
* added docker image
* docker image is being build via CI/CD & pushed to docker hub
* security updates are being pushed via dependabot

## Installation

```bash
# build the docker image
docker build . --tag canyon-notifier:latest

# run the container - you can add multiple bikes!
docker run --rm -it --name canyon-notifier \
    -e TOKEN="API_TOKEN" \
    -e CANYON_BIKE_0="Ultimate CF SL 8 Aero - Deep Polar" \
    -e CANYON_BIKE_0_URL="https://www.canyon.com/en-de/road-bikes/race-bikes/ultimate/cf-sl/ultimate-cf-sl-8-aero/3319.htmls?dwvar_3319_pv_rahmenfarbe=R101_P02" \
    -e CANYON_BIKE_0_SIZE="M"
```

## Bot father

To get the token, you need to create a bot via the bot father. You can find the bot father here: <https://t.me/botfather>

## Telegram bot commands

* `/start`
* `/help`
* `/notify` - to start notifying you about the availability
* `/unnotify` - to stop notification
* `/set` - set time interval inbetween checks
* `/status` - to do an immediate check and return the availability
