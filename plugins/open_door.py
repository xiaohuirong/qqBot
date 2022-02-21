import miraicle
import requests

@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    if(msg.text=="开门"):
        try:
            requests.get("http://192.168.1.134")
        except:
            bot.send_group_msg(group=msg.group, msg='出了点问题・_・')
        else:
            bot.send_group_msg(group=msg.group, msg='门已打开(*^ω^*)')
    else:
        pass


@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    if(msg.text=="开门"):
        try:
            requests.get("http://192.168.1.134")
        except:
            bot.send_friend_msg(qq=msg.sender, msg="出了点问题・_・")
        else:
            bot.send_friend_msg(qq=msg.sender, msg="门已打开(*^ω^*)")
    else:
        pass