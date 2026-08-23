import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message

# ==================== ALIVE & PING ====================
@Client.on_message(filters.command(["alive", "ping"], prefixes=[".", "!", "/"]) & filters.me)
async def alive_handler(client: Client, message: Message):
    await message.edit_text("✨ **Lucifer Userbot is Online & Active!** ✨\n\n⚡ **All systems normal.**")

# ==================== LOVE ANIMATION ====================
@Client.on_message(filters.command("love", prefixes=[".", "!", "/"]) & filters.me)
async def love_anim(client: Client, message: Message):
    frames = [
        "❤️", "💖", "💕", "💞", "💓",
        "❤️ I", "💖 I Love", "💕 I Love You",
        "💞 I Love You Forever ❤️", "🌹✨"
    ]
    for frame in frames:
        try:
            await message.edit_text(frame)
            await asyncio.sleep(0.4)
        except Exception:
            break

# ==================== DOSTI ANIMATION ====================
@Client.on_message(filters.command("dosti", prefixes=[".", "!", "/"]) & filters.me)
async def dosti_anim(client: Client, message: Message):
    frames = [
        "🤝", "👬", "✨ Dosti...",
        "🫂 Sacchi Dosti...",
        "🌟 Dosti Zindabad!",
        "🔥 Best Friends Forever ❤️"
    ]
    for frame in frames:
        try:
            await message.edit_text(frame)
            await asyncio.sleep(0.5)
        except Exception:
            break

# ==================== FLIRT 1 ====================
@Client.on_message(filters.command("flirt1", prefixes=[".", "!", "/"]) & filters.me)
async def flirt_one(client: Client, message: Message):
    lines = [
        "Sunno...",
        "Aapki smile itni pyaari kyun hai? 😍",
        "Dil chori karne ka iraada hai kya? 😉",
        "Pagal bana diya aapne! ❤️✨"
    ]
    for line in lines:
        try:
            await message.edit_text(line)
            await asyncio.sleep(0.7)
        except Exception:
            break

# ==================== CLONE PROFILE ====================
@Client.on_message(filters.command("clone", prefixes=[".", "!", "/"]) & filters.me)
async def clone_profile(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("❌ Kisi user ke message par reply karke `.clone` use karein.")
        return
    
    target_user = message.reply_to_message.from_user
    if not target_user:
        await message.edit_text("❌ User details nahi mil saki.")
        return

    await message.edit_text("⏳ **Cloning profile...**")
    try:
        first_name = target_user.first_name or ""
        last_name = target_user.last_name or ""
        bio = (await client.get_chat(target_user.id)).bio or ""

        # Update Name & Bio
        await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)

        # Update Profile Photo
        if target_user.photo:
            photo = await client.download_media(target_user.photo.big_file_id)
            await client.set_profile_photo(photo=photo)

        await message.edit_text(f"✅ Successfully cloned profile of **{first_name}**!")
    except Exception as e:
        await message.edit_text(f"❌ Error while cloning: `{e}`")

# ==================== ADMIN: BAN USER ====================
@Client.on_message(filters.command("ban", prefixes=[".", "!", "/"]) & filters.me)
async def ban_handler(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("❌ Kisi user ke message par reply karke `.ban` karein.")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await message.edit_text(f"🚫 **User [{user_id}] banned successfully!**")
    except Exception as e:
        await message.edit_text(f"❌ Failed to ban: `{e}`")

# ==================== ADMIN: KICK USER ====================
@Client.on_message(filters.command("kick", prefixes=[".", "!", "/"]) & filters.me)
async def kick_handler(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("❌ Kisi user ke message par reply karke `.kick` karein.")
        return
    
    user_id = message.reply_to_message.from_user.id
    try:
        await client.ban_chat_member(message.chat.id, user_id)
        await client.unban_chat_member(message.chat.id, user_id)
        await message.edit_text(f"👢 **User [{user_id}] kicked out!**")
    except Exception as e:
        await message.edit_text(f"❌ Failed to kick: `{e}`")
      
