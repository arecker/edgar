from slackbot.bot import Bot


def main():
    bot = Bot()
    try:
        bot.run()
    except KeyboardInterrupt:
        print('exiting...')
        exit()


if __name__ == "__main__":
    main()
