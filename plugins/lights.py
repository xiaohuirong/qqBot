import requests
import miraicle

@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if(msg.text=="开灯"):
        try:
            requests.get("http://192.168.1.167/on")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关灯"):
        try:
            requests.get("http://192.168.1.167/off")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    elif(msg.text=="开前灯"):
        try:
            requests.get("http://192.168.1.167/fon")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关前灯"):
        try:
            requests.get("http://192.168.1.167/foff")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    elif(msg.text=="开后灯"):
        try:
            requests.get("http://192.168.1.167/bon")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关后灯"):
        try:
            requests.get("http://192.168.1.167/boff")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='灯已打开(*^ω^*)')
    else:
        pass


@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    if(msg.text=="开灯"):
        try:
            requests.get("http://192.168.1.167/on")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关灯"):
        try:
            requests.get("http://192.168.1.167/off")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    elif(msg.text=="开前灯"):
        try:
            requests.get("http://192.168.1.167/fon")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关前灯"):
        try:
            requests.get("http://192.168.1.167/foff")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    elif(msg.text=="开后灯"):
        try:
            requests.get("http://192.168.1.167/bon")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    elif(msg.text=="关后灯"):
        try:
            requests.get("http://192.168.1.167/boff")
        except:
            bot.send_friend_msg(qq=msg.sender, msg='出了点问题・_・')
        else:
            bot.send_friend_msg(qq=msg.sender, msg='灯已打开(*^ω^*)')
    else:
        pass