import discord
from discord.ext import commands
from config import Config
from commands.ping_command import PingCommand
from commands.hello_command import HelloCommand
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(command_prefix=Config.PREFIX, intents=intents)
        self.config = Config()

    async def setup_hook(self):
        # Register slash commands with the bot
        self.tree.add_command(PingCommand().get_command())
        self.tree.add_command(HelloCommand().get_command())
        logger.info("Slash commands registered successfully.")

    async def on_ready(self):
        logger.info(f"Bot connected as {self.user} (ID: {self.user.id})")
        await self.tree.sync()
        logger.info("Slash commands synced with Discord.")


if __name__ == "__main__":
    logger.info("Starting the bot...")
    bot = MyBot()
    bot.run(Config.DISCORD_TOKEN)
