import os
import logging
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

print("ð PREMIUM TELEGRAM BOT - STARTING...")

# Get bot token from environment
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("â BOT_TOKEN not found in environment variables!")
    exit(1)

print(f"â Token loaded: {len(BOT_TOKEN)} characters")

# Initialize bot
bot = TeleBot(BOT_TOKEN)

# Premium content data
PREMIUM_CONTENT = {
    'exclusive_channels': [
        {"name": "Crypto Signals Pro", "url": "https://t.me/real_crypto_signals", "description": "High-accuracy trading signals"},
        {"name": "Premium Movie Hub", "url": "https://t.me/premium_movies", "description": "Latest movies before public release"},
    ],
    'premium_bots': [
        {"name": "Anti-Ban Bot", "url": "https://t.me/anti_ban_bot", "description": "Protect your account from bans"},
        {"name": "Auto-Trader Bot", "url": "https://t.me/crypto_auto_trader", "description": "Automated crypto trading"},
    ]
}

PAYMENT_INFO = {
    'price_usd': 10,
    'payment_methods': [
        "PayPal: your-paypal@email.com",
        "Bitcoin: bc1qyourbitcoinaddress", 
        "USDT: 0xYourEthereumAddress"
    ],
    'contact_admin': "@YourAdminUsername"
}

# Store premium users (in production, use database)
premium_users = set()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Handle /start command"""
    user = message.from_user
    user_id = user.id
    
    # Create inline keyboard
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton("Free Solutions", callback_data="free_solutions"),
        types.InlineKeyboardButton("Premium Access", callback_data="premium_info"),
        types.InlineKeyboardButton("Contact Admin", callback_data="contact_admin"),
        types.InlineKeyboardButton("Stats", callback_data="stats")
    ]
    
    # Add buttons in rows of 2
    for i in range(0, len(buttons), 2):
        row = buttons[i:i+2]
        markup.add(*row)
    
    if user_id in premium_users:
        welcome_text = f"""
ð Welcome BACK, Premium Member! {user.first_name}

You have full access to all exclusive content!

What would you like to explore today?
        """
    else:
        welcome_text = f"""
ð¤ Welcome to Exclusive Helper Bot!

ð° What I Offer:
â¢ FREE: Basic Telegram solutions  
â¢ PREMIUM: Exclusive channels & bots (${PAYMENT_INFO['price_usd']})

ð Premium Content Includes:
â¢ High-value crypto signal channels
â¢ Unreleased AI tools & bots
â¢ Private movie/content channels
â¢ Money-making methods

Choose an option below:
        """
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    logger.info(f"User {user.first_name} (ID: {user_id}) started the bot")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    """Handle inline button clicks"""
    user_id = call.from_user.id
    
    if call.data == "free_solutions":
        show_free_solutions(call)
    elif call.data == "premium_info":
        show_premium_info(call)
    elif call.data == "contact_admin":
        contact_admin(call)
    elif call.data == "stats":
        send_stats(call)

def show_free_solutions(call):
    """Show free solutions menu"""
    response = """
ð FREE SOLUTIONS

Available free solutions:

1. Unblock restricted channels
2. Fix sensitive content errors  
3. Find public channels

ð For exclusive content and premium bots, upgrade to Premium!
    """
    bot.edit_message_text(
        response,
        call.message.chat.id,
        call.message.message_id
    )

def show_premium_info(call):
    """Show premium information"""
    user_id = call.from_user.id
    
    if user_id in premium_users:
        response = """
ð PREMIUM MEMBER ACCESS

You have full access to all exclusive content!

Available premium features:
â¢ Exclusive crypto signal channels
â¢ Premium AI tools and bots
â¢ Private content channels
â¢ Money-making methods
        """
    else:
        response = f"""
ð PREMIUM ACCESS - ${PAYMENT_INFO['price_usd']}

ð What You Get:

ð EXCLUSIVE CHANNELS:
â¢ High-value crypto signal channels
â¢ Private movie/content releases
â¢ Unreleased AI tools & resources
â¢ Money-making methods

ð¤ PREMIUM BOTS:
â¢ Anti-ban protection bots
â¢ Auto-trading systems
â¢ Channel analytics tools
â¢ Mass messaging solutions

ð° Payment: ${PAYMENT_INFO['price_usd']} (One-time, lifetime access)

ð Contact admin for payment methods: {PAYMENT_INFO['contact_admin']}
        """
    
    bot.edit_message_text(
        response,
        call.message.chat.id, 
        call.message.message_id
    )

def contact_admin(call):
    """Show admin contact information"""
    response = f"""
ð CONTACT ADMIN

For payment issues, premium access, or questions:

ð¤ Admin: {PAYMENT_INFO['contact_admin']}

ð Please include:
â¢ Your Telegram ID
â¢ Payment method used  
â¢ Transaction details (if any)

We'll respond as soon as possible!
    """
    bot.edit_message_text(
        response,
        call.message.chat.id,
        call.message.message_id
    )

def send_stats(call):
    """Show bot statistics"""
    total_users = len(premium_users)
    response = f"""
ð BOT STATISTICS

â¢ Premium Members: {total_users}
â¢ Price: ${PAYMENT_INFO['price_usd']}
â¢ Status: Active and growing!

â­ Premium features unlocked!
    """
    bot.edit_message_text(
        response,
        call.message.chat.id,
        call.message.message_id
    )

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """Handle all other messages"""
    send_welcome(message)

def main():
    """Start the bot"""
    print("=" * 60)
    print("ð¤ PREMIUM TELEGRAM BOT - READY TO EARN!")
    print("=" * 60)
    print(f"ð° Price: ${PAYMENT_INFO['price_usd']}")
    print(f"ð Channels: {len(PREMIUM_CONTENT['exclusive_channels'])}")
    print(f"ð¤ Bots: {len(PREMIUM_CONTENT['premium_bots'])}")
    print("ð³ Accepting: USDT, BTC, ETH, BNB")
    print("=" * 60)
    
    try:
        print("â Bot is running and polling for messages...")
        print("ð± Test your bot by sending /start on Telegram")
        print("=" * 60)
        
        # Start the bot
        bot.infinity_polling()
        
    except Exception as e:
        logger.error(f"â Failed to start bot: {e}")
        print(f"â Error: {e}")

if __name__ == '__main__':
    main()