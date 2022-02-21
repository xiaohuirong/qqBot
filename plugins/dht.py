import miraicle
import requests

@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if(msg.text=="温度"):
        try:
            data = requests.get("http://192.168.1.134/data")
            data = data.text
            tem = data.split()[1]
            tem = round(float(tem),2)
            tem = str(tem)
            tem = "温度为:"+tem+"°C"
        except:
            bot.send_group_msg(group=msg.group, msg="抱歉，没能读到温度，请再试一次")
        else:
            bot.send_group_msg(group=msg.group, msg=tem)

    elif(msg.text=="湿度"):
        try:
            data = requests.get("http://192.168.1.134/data")
            data = data.text
            hum = data.split()[0]
            hum = round(float(hum),2)
            hum = str(hum)
            hum = "湿度为:"+hum+"%"
        except:
            bot.send_group_msg(group=msg.group, msg="抱歉，没能读到湿度，请再试一次")
        else:
            bot.send_group_msg(group=msg.group, msg=hum)
    else:
        pass
    

@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    if(msg.text=="温度"):
        try:
            data = requests.get("http://192.168.1.134/data")
            data = data.text
            tem = data.split()[1]
            tem = round(float(tem),2)
            tem = str(tem)
            tem = "温度为:"+tem+"°C"
        except:
            bot.send_friend_msg(qq=msg.sender, msg="抱歉，没能读到温度，请再试一次")
        else:
            bot.send_friend_msg(qq=msg.sender, msg=tem)

    elif(msg.text=="湿度"):
        try:
            data = requests.get("http://192.168.1.134/data")
            data = data.text
            hum = data.split()[0]
            hum = round(float(hum),2)
            hum = str(hum)
            hum = "湿度为:"+hum+"%"
        except:
            bot.send_friend_msg(qq=msg.sender, msg="抱歉，没能读到湿度，请再试一次")
        else:
            bot.send_friend_msg(qq=msg.sender, msg=hum)
    else:
        pass