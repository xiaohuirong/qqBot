import miraicle
from plugins import *

qq = 3262246500              # 你登录的机器人 QQ 号
verify_key = '252119xhr'     # 你在 setting.yml 中设置的 verifyKey
port = 8080                 # 你在 setting.yml 中设置的 port (http)

bot = miraicle.Mirai(qq=qq, verify_key=verify_key, port=port)
bot.run()
