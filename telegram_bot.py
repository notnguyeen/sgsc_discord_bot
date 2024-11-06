from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import Config
from commands.ping_command import PingCommand
from commands.hello_command import HelloCommand
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TelegramBot:
    def __init__(self):
        # Initialize the Telegram bot application
        self.app = Application.builder().token(Config.TELEGRAM_TOKEN).build()
        self.commands = {
            "ping": PingCommand(),
            "hello": HelloCommand(),
        }

    async def ping_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handles the /ping command."""
        logger.info(f"/ping command triggered by {update.effective_user.username}")
        await self.commands["ping"].execute(update, context)

    async def hello_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handles the /hello command."""
        logger.info(f"/hello command triggered by {update.effective_user.username}")
        await self.commands["hello"].execute(update, context)

    def run(self):
        # Register the command handlers for each command
        self.app.add_handler(CommandHandler("ping", self.ping_command))
        self.app.add_handler(CommandHandler("hello", self.hello_command))

        # Start the bot
        logger.info("Starting the Telegram bot...")
        self.app.run_polling()


if __name__ == "__main__":
    # Initialize and run the Telegram bot
    bot = TelegramBot()
    bot.run()
