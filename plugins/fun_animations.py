# =============================================================================
#  CipherElite Userbot Plugin - Custom Fun & Animations
#  Updated for CipherElite Repo (Telethon Format)
# =============================================================================

import asyncio
import random
from collections import deque
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from utils.utils import CipherElite
from utils.decorators import rishabh
from plugins.bot import add_handler

# Userbot owner's name
DEFAULTUSER = "Elite User"

def init(client):
    """Initialize the custom fun and animation plugin"""
    commands = [
        ".mind         - Animated brain cleanup sequence",
        ".explode      - Explosive animation with a bang",
        ".dial         - Simulate a call to a VIP",
        ".zap          - Zap someone with a fun animation",
        ".huh          - A confused 'huh?' animation",
        ".pingpong     - Bouncing ball animation",
        ".spiral       - Hypnotic spiral animation",
        ".sweets       - Rotating candy emojis",
        ".badass       - Show off your badass vibe",
        ".charge       - Charge up a device animation",
        ".dekh         - Savage funny reply",
        ".pagle        - Cute funny reaction animation",
        ".roast        - Roast someone with funny lines",
        ".bhoot        - Funny ghost prank animation",
        ".bhai         - Funny taarif sequence",
        ".nasha        - Drunk comedy animation",
        ".joke         - Tell a random funny joke",
        ".slap         - Slap someone with a fun animation"
    ]
    description = "Custom fun, animation and comedy commands"
    add_handler("custom_fun", commands, description)

async def edit_or_reply(event, text):
    """Try to edit the message; if that fails, send a reply"""
    try:
        return await event.edit(text)
    except Exception:
        return await event.reply(text)

# ==================== ORIGINAL ANIMATIONS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.mind$", outgoing=True))
@rishabh()
async def mind(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(10)
    event = await edit_or_reply(event, "🧠 Processing...")
    animation_chars = [
        "🧠 MIND RESET ➡️ 🚀\n\n🧠   <(•_•)> 💨",
        "🧠 MIND RESET ➡️ 🚀\n\n🧠 <(•_•)>   💨",
        "🧠 MIND RESET ➡️ 🚀\n\n🧠<(•_•)>     💨",
        "🧠 MIND RESET ➡️ 🚀\n\n(> •_•)>🧠     💨",
        "🧠 MIND RESET ➡️ 🚀\n\n  (> •_•)>🧠   💨",
        "🧠 MIND RESET ➡️ 🚀\n\n    (> •_•)>🧠 💨",
        "🧠 MIND RESET ➡️ 🚀\n\n      (> •_•)>🧠",
        "🧠 MIND RESET ➡️ 🚀\n\n        (> •_•)>",
        "🧠 MIND RESET ➡️ 🚀\n\n         <(•_•)>",
        "🧠 MIND CLEARED! ✨\n\n**(°o°)** Ready to rock!"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])

@CipherElite.on(events.NewMessage(pattern=r"^\.explode$", outgoing=True))
@rishabh()
async def explode(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "💥 Preparing explosion...")
    await event.edit("⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛")
    await asyncio.sleep(0.5)
    await event.edit("💣⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛")
    await asyncio.sleep(0.5)
    await event.edit("⬛⬛⬛⬛\n⬛💣⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛")
    await asyncio.sleep(0.5)
    await event.edit("⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛💣⬛\n⬛⬛⬛⬛")
    await asyncio.sleep(0.5)
    await event.edit("⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛💣")
    await asyncio.sleep(0.5)
    await event.edit("⬛⬛⬛⬛\n⬛⬛⬛⬛\n⬛⬛⬛⬛\n💥💥💥💥")
    await asyncio.sleep(1)
    await event.edit("💥💥💥💥\n💥🔥🔥💥\n💥🔥🔥💥\n💥💥💥💥")
    await asyncio.sleep(0.5)
    await event.edit("💥 **BOOM!** Everything's gone! 😎")

@CipherElite.on(events.NewMessage(pattern=r"^\.dial$", outgoing=True))
@rishabh()
async def dial(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(10)
    event = await edit_or_reply(event, "📞 Dialing a VIP...")
    animation_chars = [
        "`Connecting to Secret Network...`",
        "`Call Initiated.`",
        "`VIP: Who's this?`",
        f"`Me: Yo, it's {DEFAULTUSER}!`",
        "`VIP: Authentication in progress...`",
        "`Call Secured at +91-SECRET-NO`",
        f"`Me: Hey, what's good?`",
        "`VIP: Yo, {DEFAULTUSER}! Been ages!`",
        "`VIP: Gotta run, catch ya later!`",
        "`Call Ended. Stay cool! 😎`"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])

@CipherElite.on(events.NewMessage(pattern=r"^\.zap$", outgoing=True))
@rishabh()
async def zap(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "⚡ Reply to a user to zap them!")
        return
    reply_message = await event.get_reply_message()
    replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
    firstname = replied_user.user.first_name or "Unknown"
    animation_interval = 1
    animation_ttl = range(8)
    await edit_or_reply(event, f"⚡ Zapping {firstname}...")
    animation_chars = [
        "⚡ ZAP! ⚡",
        "🔫===>",
        "🔫=====>",
        "🔫=======>",
        "🔫========>",
        "🔫=========>",
        "🔥 ZAPPED! 🔥",
        f"💥 {firstname} is toast! 😜"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])

@CipherElite.on(events.NewMessage(pattern=r"^\.huh$", outgoing=True))
@rishabh()
async def huh(event):
    if event.fwd_from:
        return
    animation_interval = 0.7
    animation_ttl = range(5)
    event = await edit_or_reply(event, "🤔 Huh?")
    animation_chars = [
        "🤔 What's that?",
        "🤔 What's going on?",
        "🤔 What's the deal?",
        "🤔 What's up, fam?",
        "😵 Totally lost! 🤷‍♂️"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])

@CipherElite.on(events.NewMessage(pattern=r"^\.pingpong$", outgoing=True))
@rishabh()
async def pingpong(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(12)
    event = await edit_or_reply(event, "🏓 Ping pong!")
    animation_chars = [
        "⬛⬛⬛⬛⬛\n⬛🏓⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛\n⬛⬛🏓⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛\n⬛⬛⬛🏓⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🏓\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛🏓\n⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛🏓⬛\n⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛🏓⬛⬛\n⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛🏓⬛⬛⬛\n⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "🏓⬛⬛⬛⬛\n⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛\n🏓⬛⬛⬛⬛\n⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🏓\n⬛⬛⬛⬛⬛",
        "🏓 **PONG!** 🏓"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])

@CipherElite.on(events.NewMessage(pattern=r"^\.spiral$", outgoing=True))
@rishabh()
async def spiral(event):
    if event.fwd_from:
        return
    animation_interval = 0.4
    animation_ttl = range(10)
    event = await edit_or_reply(event, "🌀 Spiraling...")
    animation_chars = [
        "⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜",
        "⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜",
        "⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜",
        "⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜\n⬛⬜⬛⬜⬛\n⬜⬛⬜⬛⬜",
        "🌀 Hypnotized! 😵",
        "🌀 **SPINNING AWAY!** 🚀"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])

@CipherElite.on(events.NewMessage(pattern=r"^\.sweets$", outgoing=True))
@rishabh()
async def sweets(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🍬 Sweetening things up...")
    deq = deque(list("🍬🍭🍫🧁🍰🎂🍪🍩🍧🍦"))
    for _ in range(50):
        await asyncio.sleep(0.3)
        await event.edit("".join(deq))
        deq.rotate(1)
    await event.edit("🍬 Sweet overload! 😋")

@CipherElite.on(events.NewMessage(pattern=r"^\.badass$", outgoing=True))
@rishabh()
async def badass(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "😎 Getting ready...")
    await event.edit("YO")
    await asyncio.sleep(0.3)
    await event.edit("YO, I'M")
    await asyncio.sleep(0.3)
    await event.edit("YO, I'M THE")
    await asyncio.sleep(0.3)
    await event.edit("YO, I'M THE BOSS")
    await asyncio.sleep(0.3)
    await event.edit("YO, I'M THE BOSS HERE")
    await asyncio.sleep(0.3)
    await event.edit(f"😎 {DEFAULTUSER} IS THE BOSS! 🔥")

@CipherElite.on(events.NewMessage(pattern=r"^\.charge$", outgoing=True))
@rishabh()
async def charge(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🔋 Charging...")
    txt = "🔋 Quantum Charger Activated...\nDevice: CipherElite Phone\nBattery: "
    percentage = 0
    for _ in range(5):
        await event.edit(txt + f"{percentage}%")
        percentage += 20
        await asyncio.sleep(1)
    await event.edit("🔋 Quantum Charger Done!\nDevice: CipherElite Phone\nBattery: 100% ⚡")


# ==================== NEW FUNNY & COMEDY COMMANDS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.dekh$", outgoing=True))
@rishabh()
async def dekh_command(event):
    if event.fwd_from:
        return
    savage_lines = [
        "Acha ji? Zara aaine mein shakal dekhi hai apni? 🐒😂",
        "Beta tumse na ho payega! 🥱",
        "Itna dimag kahan se laate ho bhai? Thoda humein bhi udhaar de do! 🧠❌",
        "Bade heavy driver ho bhai aap toh! 🛺💨"
    ]
    await edit_or_reply(event, random.choice(savage_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.pagle$", outgoing=True))
@rishabh()
async def pagle_command(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "Acha ji...")
    frames = ["Itna pyaar? 🥺", "Pagla gaye ho kya bhai? 😂❤️", "Jao maaf kiya! 🤭✨"]
    for frame in frames:
        await asyncio.sleep(0.5)
        await event.edit(frame)

@CipherElite.on(events.NewMessage(pattern=r"^\.roast$", outgoing=True))
@rishabh()
async def roast_command(event):
    if event.fwd_from:
        return
    roasts = [
        "Tumhari baatein sunkar lagta hai ki Google ko bhi 'I don't know' bolna pad jata hoga! 🤖📉",
        "Bhai jab upar wala akal baant raha tha, toh tum umbrella lekar khade the kya? ☂️😂",
        "Tumhe dekh kar lagta hai ki evolution reverse bhi ho sakta hai! 🐒🔙"
    ]
    await edit_or_reply(event, random.choice(roasts))

@CipherElite.on(events.NewMessage(pattern=r"^\.bhoot$", outgoing=True))
@rishabh()
async def bhoot_prank(event):
    if event.fwd_from:
        return
    steps = [
        "👻 Room ki batti gul...",
        "🕯️ Mom batti jali...",
        "😱 Bhoot aa gaya bhoot!",
        "🏃‍♂️ Bhaago bhai bhoot pichhe pad gaya! 💀💨"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.bhai$", outgoing=True))
@rishabh()
async def bhai_taarif(event):
    if event.fwd_from:
        return
    taarifein = [
        "Bhai tu aam insaan nahi, 'Ajooba' hai! 🗿😂",
        "Tujh jaisa dost ho toh dushman ki zaroorat hi nahi padti, kaam khud hi kar deta hai! 🤝🔥",
        "Bhai tere confidence ko salaam, galti karke bhi itna attitude! 😎👏",
        "Tu jab paida hua tha toh doctor ne hospital walo ko party di hogi ki chalo bala tali! 🍼🎉"
    ]
    await edit_or_reply(event, random.choice(taarifein))

@CipherElite.on(events.NewMessage(pattern=r"^\.nasha$", outgoing=True))
@rishabh()
async def nasha_comedy(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "🍺 Glass mein kya hai?")
    frames = [
        "🌀 Duniya ghum rahi hai...",
        "😵‍💫 Main zameen par hoon ya aasmaan par?",
        "🥴 Bhai mujhe mat pakdo, main khud zameen ko pakde baitha hoon! 🌍😂"
    ]
    for frame in frames:
        await asyncio.sleep(0.5)
        await event.edit(frame)

@CipherElite.on(events.NewMessage(pattern=r"^\.joke$", outgoing=True))
@rishabh()
async def tell_joke(event):
    if event.fwd_from:
        return
    jokes = [
        "Pati: Tum jab gusse mein hoti ho toh aur bhi khoobsurat lagti ho...\nPatni: Sachhi? 😊\nPati: Nahi, mujhe pagal kutte ki tarah lagti ho! 🐕😂",
        "Teacher: Kal school kyun nahi aaye the?\nStudent: Sir, raste mein ek board laga tha jispe likha tha 'Aage School hai, Dheere Chalein' isliye dheere chalte-chalte pahucha toh chutti ho gayi thi! 🏫🚶‍♂️",
        "Santa: Yaar, meri biwi mujhe har jagah dhundhti hai jab main baahar jata hoon.\nBanta: Wah, kitna pyaar karti hai!\nSanta: Pyaar nahi bhai, shak hai ki main kahin chupke se momos na kha raha hoon! 🥟😂"
    ]
    await edit_or_reply(event, random.choice(jokes))

@CipherElite.on(events.NewMessage(pattern=r"^\.slap$", outgoing=True))
@rishabh()
async def slap_user(event):
    if event.fwd_from:
        return
    if event.is_reply:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        target = replied_user.user.first_name or "user"
        await edit_or_reply(event, f"👋 Slapped **{target}** hard! 🍳")
    else:
        await edit_or_reply(event, "👋 Slapped into the air! 💨")
