import os
from modules import cprint

def setup():
    if not os.path.exists('config.ini'):
        cprint("config.ini file does not exist, creating one for you...", 3)
        with open('config.ini', 'w') as file:
            file.write("""[bot_nuker_config]
bot_token = YOUR_BOT_TOKEN
spam_message = @everyone luh sino to? https://cdn.discordapp.com/attachments/1362832473607901456/1362854931345707290/IMG_20250419_004156_894.jpg?ex=6803e910&is=68029790&hm=232ba72fe832a14d8a5484d2d645bcbe156f8810a149279ed9979880ab369147&
role_name = Tekk
channel_name = TEKO
dm_message = SALOT TONG BABAENG TO HAHAHAHAHA https://cdn.discordapp.com/attachments/1362832473607901456/1362854931345707290/IMG_20250419_004156_894.jpg?ex=6803e910&is=68029790&hm=232ba72fe832a14d8a5484d2d645bcbe156f8810a149279ed9979880ab369147&
ban_message = 
server_name = TEKO OWNS U""")
    if not os.path.exists('proxies.txt'):
        cprint("proxies.txt file does not exist, creating one for you...", 3)
        with open('proxies.txt', 'w') as file:
            file.write("""# MAKE SURE ALL YOUR PROXIES ARE EITHER HTTP OR HTTPS
# PROXY FORMAT: (proxy ip):(proxy port)
# Example: 127.0.0.1:100""")
