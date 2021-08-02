# bridge-whale-bot

A bot for scraping Tweets pertaining to transactions on Badger Bridge.
This is a [Gitcoin bounty](https://gitcoin.co/issue/Badger-Finance/gitcoin/18/100026127) submission for **BadgerDAO**.

## Usage

1. Copy and paste the `.example-env` contents into a new `.env` file.
2. Provide a **Webhook URL** and your **Twitter API Keys & Tokens**.
3. Build the application using the following command: `docker-compose -f "docker-compose.yml" up -d --build`
4. Finally, run the application using the following command: `docker run --env-file .env bridgewhalebot`
