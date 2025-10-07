import os
import logging
from flask import Flask
from threading import Thread
from telebot import TeleBot, types
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Flask app for port binding (Render requirement)
app = Flask('')

@app.route('/')
def home():
    return "ð¤ Telegram Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()

print("ð PREMIUM TELEGRAM BOT - STARTING...")

# Get bot token from environment
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("â BOT_TOKEN not found in environment variables!")
    exit(1)

print(f"â Token loaded: {len(BOT_TOKEN)} characters")

# Initialize bot
bot = TeleBot(BOT_TOKEN)

# [REST OF YOUR BOT CODE REMAINS THE SAME]
# Keep all your premium content, handlers, etc.

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handle /start command"""
    user = message.from_user
    user_id = user.id
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("Free Solutions", callback_data="free_solutions"),
        types.InlineKeyboardButton("Premium Access", callback_data="premium_info"),
        types.InlineKeyboardButton("Contact Admin", callback_data="contact_admin"),
        types.InlineKeyboardButton("Stats", callback_data="stats")
    ]
    
    for i in range(0, len(buttons), 2):
        row = buttons[i:i+2]
        markup.add(*row)
    
    if user_id in premium_users:
        welcome_text = f"ð Welcome BACK, Premium Member! {user.first_name}"
    else:
        welcome_text = f"ð¤ Welcome to Exclusive Helper Bot!"
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# [KEEP ALL YOUR OTHER FUNCTIONS]

def main():
    """Start the bot"""
    print("=" * 60)
    print("ð¤ PREMIUM TELEGRAM BOT - READY TO EARN!")
    print("=" * 60)
    
    # Start Flask server for port binding
    keep_alive()
    print("â Flask server started on port 8080")
    
    try:
        print("â Bot is running and polling for messages...")
        print("ð± Test your bot by sending /start on Telegram")
        print("=" * 60)
        
        # Start the bot
        bot.infinity_polling()
        
    except Exception as e:
        logger.error(f"â Failed to start bot: {e}")
if __name__ == '__main__':
    main()
