import discord
import logging
from discord.ext import commands
from discord import app_commands
from config import Config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.default()
        super().__init__(command_prefix=Config.PREFIX, intents=intents)
        self.config = Config()

    async def setup_hook(self):
        # Register slash commands
        self.tree.add_command(PingCommand().get_command())
        self.tree.add_command(HelloCommand().get_command())
        logger.info("Slash commands registered successfully.")

    async def on_ready(self):
        logger.info(f"Bot connected as {self.user} (ID: {self.user.id})")
        # Sync commands with Discord
        await self.tree.sync()
        logger.info("Slash commands synced with Discord.")

    async def on_command(self, ctx):
        logger.info(f"Executing command: {ctx.command} by user {ctx.author}")


class PingCommand:
    def get_command(self):
        @app_commands.command(name="ping", description="Responds with Pong!")
        async def ping(interaction: discord.Interaction):
            logger.info(f"Ping command triggered by {interaction.user}")
            await interaction.response.send_message("Pong!")

        return ping


class HelloCommand:
    def get_command(self):
        @app_commands.command(name="hello", description="Greets the user")
        async def hello(interaction: discord.Interaction):
            logger.info(f"Hello command triggered by {interaction.user}")
            await interaction.response.send_message(
                f"Hello, {interaction.user.display_name}!"
            )

        return hello


if __name__ == "__main__":
    logger.info("Starting the bot...")
    bot = MyBot()
    bot.run(Config.DISCORD_TOKEN)
