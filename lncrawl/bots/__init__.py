supported_bots = [
    "console",
    "telegram",
    "discord",
    "web",
    "test",
]


def run_bot(bot):
    if bot not in supported_bots:
        bot = "console"

    if bot == "console":
        from ..bots.console import ConsoleBot


        ConsoleBot().start()
    elif bot == "telegram":
        from ..bots.telegram import TelegramBot

        TelegramBot().start()
    elif bot == "discord":
        from ..bots.discord import DiscordBot

        DiscordBot().start_bot()
    elif bot == "web":
        from . import web

    elif bot == "lookup":
        from ..bots.lookup import LookupBot

        LookupBot().start()
    elif bot == "test":
        from ..bots.test import TestBot # type: ignore

        TestBot().start()
    else:
        print("Unknown bot: %s" % bot)
