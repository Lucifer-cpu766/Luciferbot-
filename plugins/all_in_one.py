import os
import asyncio
import time
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired

ORIGINAL_NAME = None
ORIGINAL_BIO = None
spam_tracker = {}

async def get_target_user(client: Client, message: Message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        target = args[1]
        if target.isdigit():
            return int(target)
        try:
            user = await client.get_users(target)
            return user.id
        except Exception:
            return None
    return None

async def play_animation(message: Message, frames: list, delay: float = 0.5):
    for frame in frames:
        try:
            await message.edit(frame)
            await asyncio.sleep(delay)
        except Exception:
            pass


# ==================== 1. ADMIN COMMANDS ====================

@Client.on_message(filters.command(["ban"], prefixes=[".", "!", "/"]) & filters.me)
async def ban_user(client: Client, message: Message):
    user_id = await get_target_user(client, message)
    if not user_id:
        return await message.edit("❌ Reply to a user or provide username/ID.")
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.edit(f"🔨 **User `{user_id}` has been banned.**")
    except ChatAdminRequired:
        await message.edit("❌ **Error:** Admin permissions required.")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")

@Client.on_message(filters.command(["kick"], prefixes=[".", "!", "/"]) & filters.me)
async def kick_user(client: Client, message: Message):
    user_id = await get_target_user(client, message)
    if not user_id:
        return await message.edit("❌ Reply to a user or provide username/ID.")
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await client.unban_chat_member(message.chat.id, user_id)
        await message.edit(f"👢 **User `{user_id}` has been kicked.**")
    except ChatAdminRequired:
        await message.edit("❌ **Error:** Admin permissions required.")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")

@Client.on_message(filters.command(["mute"], prefixes=[".", "!", "/"]) & filters.me)
async def mute_user(client: Client, message: Message):
    user_id = await get_target_user(client, message)
    if not user_id:
        return await message.edit("❌ Reply to a user.")
    try:
        await client.restrict_chat_member(message.chat.id, user_id, permissions=[])
        await message.edit(f"🔇 **User `{user_id}` has been muted.**")
    except ChatAdminRequired:
        await message.edit("❌ **Error:** Admin permissions required.")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")

@Client.on_message(filters.command(["unban"], prefixes=[".", "!", "/"]) & filters.me)
async def unban_user(client: Client, message: Message):
    user_id = await get_target_user(client, message)
    if not user_id:
        return await message.edit("❌ Specify user.")
    try:
        await client.unban_chat_member(message.chat.id, user_id)
        await message.edit(f"✅ **User `{user_id}` unbanned/unmuted.**")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")

@Client.on_message(filters.command(["purge"], prefixes=[".", "!", "/"]) & filters.me)
async def purge(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("❌ Reply to the message where you want to start purging.")
    start_id = message.reply_to_message.id
    end_id = message.id
    message_ids = list(range(start_id, end_id + 1))
    try:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message_ids)
        del_msg = await client.send_message(message.chat.id, f"🧹 `{len(message_ids)}` messages deleted.")
        await asyncio.sleep(3)
        await del_msg.delete()
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")


# ==================== 2. CLONE SYSTEM ====================

@Client.on_message(filters.command(["clone"], prefixes=[".", "!", "/"]) & filters.me)
async def clone_profile(client: Client, message: Message):
    global ORIGINAL_NAME, ORIGINAL_BIO
    if not message.reply_to_message:
        return await message.edit("❌ Reply to someone's message to `.clone`.")
    
    await message.edit("🔄 Cloning profile...")
    target = message.reply_to_message.from_user
    try:
        me = await client.get_me()
        me_chat = await client.get_chat("me")
        if ORIGINAL_NAME is None:
            ORIGINAL_NAME = (me.first_name, me.last_name or "")
            ORIGINAL_BIO = me_chat.bio or ""

        target_chat = await client.get_chat(target.id)
        pfp_path = None
        if target.photo:
            pfp_path = await client.download_media(target.photo.big_file_id)

        await client.update_profile(
            first_name=target.first_name or "",
            last_name=target.last_name or "",
            bio=target_chat.bio or ""
        )
        if pfp_path:
            await client.set_profile_photo(photo=pfp_path)
            if os.path.exists(pfp_path):
                os.remove(pfp_path)

        await message.edit(f"🎭 **Cloned:** {target.first_name}")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")

@Client.on_message(filters.command(["revert"], prefixes=[".", "!", "/"]) & filters.me)
async def revert_profile(client: Client, message: Message):
    global ORIGINAL_NAME, ORIGINAL_BIO
    if ORIGINAL_NAME is None:
        return await message.edit("❌ No saved original profile details found.")
    
    await message.edit("🔄 Reverting profile...")
    try:
        first, last = ORIGINAL_NAME
        await client.update_profile(first_name=first, last_name=last, bio=ORIGINAL_BIO)
        photos = [p async for p in client.get_chat_photos("me", limit=1)]
        if photos:
            await client.delete_profile_photos(photos[0].file_id)
            
        ORIGINAL_NAME = None
        ORIGINAL_BIO = None
        await message.edit("✅ **Profile restored back to normal!**")
    except Exception as e:
        await message.edit(f"❌ **Error:** `{e}`")


# ==================== 3. ANIMATION & FLIRT COMMANDS ====================

@Client.on_message(filters.command(["love"], prefixes=[".", "!", "/"]) & filters.me)
async def love_anim(client: Client, message: Message):
    frames = ["❤️", "❤️ I", "❤️ I L", "❤️ I Lo", "❤️ I Lov", "❤️ I Love", "❤️ I Love You 💖", "✨ I Love You Forever ✨"]
    await play_animation(message, frames, 0.4)

@Client.on_message(filters.command(["heart"], prefixes=[".", "!", "/"]) & filters.me)
async def heart_anim(client: Client, message: Message):
    frames = ["🤍", "💛", "🧡", "❤️", "💖", "💗", "💓", "💞", "💕", "💖 **You have my whole heart!** 💖"]
    await play_animation(message, frames, 0.5)

@Client.on_message(filters.command(["dosti"], prefixes=[".", "!", "/"]) & filters.me)
async def dosti_anim(client: Client, message: Message):
    frames = ["🤝", "🤝 Dost", "✨ Dosti Zindabad ✨", "🫂 **Dost hai toh sab kuch hai!** 🫂"]
    await play_animation(message, frames, 0.4)

@Client.on_message(filters.command(["hug"], prefixes=[".", "!", "/"]) & filters.me)
async def hug_anim(client: Client, message: Message):
    frames = ["(づ｡◕‿‿◕｡)づ", "(っ˘̩╭╮˘̩)っ", "(つ≧▽≦)つ", "🫂 Sending you a big warm hug!", "✨ **Always here for you!** ✨"]
    await play_animation(message, frames, 0.6)

@Client.on_message(filters.command(["pyar"], prefixes=[".", "!", "/"]) & filters.me)
async def pyar_anim(client: Client, message: Message):
    frames = ["🌸", "🌸 *Agar tum saath ho...*", "✨ **Toh ye duniya bahut khoobsurat lagti hai.** ✨"]
    await play_animation(message, frames, 0.6)

@Client.on_message(filters.command(["flirt1"], prefixes=[".", "!", "/"]) & filters.me)
async def flirt_one(client: Client, message: Message):
    frames = ["📶 Checking connection...", "✨ Lagta hai mere dil ka connection...", "💘 **Seedha tumse connect ho gaya hai!** 😉"]
    await play_animation(message, frames, 0.6)

@Client.on_message(filters.command(["flirt2"], prefixes=[".", "!", "/"]) & filters.me)
async def flirt_two(client: Client, message: Message):
    frames = ["🗺️ Searching Google Maps...", "📍 Location: Tumhara Dil...", "🔥 **Par wahan se wapas aane ka rasta nahi mil raha!** 🤭"]
    await play_animation(message, frames, 0.6)

@Client.on_message(filters.command(["flirt3"], prefixes=[".", "!", "/"]) & filters.me)
async def flirt_three(client: Client, message: Message):
    frames = ["🚨 Alert! Police ko bulao...", "💖 **Kisi ne mera dil chura liya hai...**", "👀 Aur shaq tum par hi hai! 😌"]
    await play_animation(message, frames, 0.6)

@Client.on_message(filters.command(["flirt4"], prefixes=[".", "!", "/"]) & filters.me)
async def flirt_four(client: Client, message: Message):
    frames = ["🌹 Ek baat bolu?", "✨ Jab bhi tum online aati ho...", "🌟 **Screen ka brightness badh jata hai!** ✨"]
    await play_animation(message, frames, 0.7)


# ==================== 4. ANTI-SPAM PROTECTION ====================

@Client.on_message(filters.group & ~filters.me & ~filters.bot)
async def anti_spam_watcher(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else None
    if not user_id:
        return

    if chat_id not in spam_tracker:
        spam_tracker[chat_id] = {}

    current_time = time.time()
    
    if user_id not in spam_tracker[chat_id]:
        spam_tracker[chat_id][user_id] = []

    spam_tracker[chat_id][user_id] = [t for t in spam_tracker[chat_id][user_id] if current_time - t < 5]
    spam_tracker[chat_id][user_id].append(current_time)

    if len(spam_tracker[chat_id][user_id]) > 5:
        try:
            await client.restrict_chat_member(chat_id, user_id, permissions=[])
            warn_msg = await message.reply(f"🛡️ **Anti-Spam Alert:** `{message.from_user.first_name}` has been muted for spamming.")
            await asyncio.sleep(5)
            await warn_msg.delete()
            spam_tracker[chat_id][user_id] = []
        except Exception:
            pass

