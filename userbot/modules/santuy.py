# Sky Not
# by @Zxyune
# FROM Skyla-Userbot <https://github.com/SkylaIND/Skyla-Userbot>


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.to(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ππ΄π΄πΌπΎ π³πΈ π±πΈππΎπΎ")


@register(outgoing=True, pattern='^.btpm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("πππ ππ§π£π  ππ/ππ ππ¨ππ§ π§ππ‘ππππ πππ₯ππ£π π£π ππππ!!")


@register(outgoing=True, pattern='^.sl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("KAK BAGI SALDAN YANG LEBIHπ")


@register(outgoing=True, pattern='^.sy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SAYA LUCU DAN SAYA DIAM..")


@register(outgoing=True, pattern='^.sm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("SASIMO AJA BELAGU ANJ..")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAMOOD HEHEHE..")


@register(outgoing=True, pattern='^.lope(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("βββββββββββββββββββββββ\n"
                     "ββββββββββββββββββββββ\n"
                     "ββββββββββββββββββββββ\n"
                     "βββββββββββββββββββββββ\n")


CMD_HELP.update({
    "santuy":
    ".to\
\nUsage: Gikes Tmo.\
\n\n.btpm\
\nUsage: Cari Btpm.\
\n\n.sl\
\nUsage: Cari Saldan.\
\n\n.sy\
\nUsage: Saya Lucu."
})


CMD_HELP.update({
    "santuy2":
    ".sm\
\nUsage: Lu Sasimo.\
\n\n.ga\
\nUsage: Aku Gamood.\
\n\n.lope\
\nUsage: Kata Love."
})
