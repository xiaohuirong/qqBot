import miraicle
import re
import datetime
import time
import json

friend = {}
group = {}

def send_message(bot,id,flag):
    global friend,group
    msg_to_send = ""
    count = 0
    now = time.strftime("%Y-%m-%d")
    now = datetime.datetime.strptime(now,"%Y-%m-%d").date()

    if flag==1:
        content = friend[id]
    else:
        content = group[id]

    for item in content:
        raw = item.split()
        name = raw[0]
        date_str = raw[1]
        date = datetime.datetime.strptime(date_str,"%Y-%m-%d").date()
        day_left = (date-now).days
        if day_left<0:
            if flag==1:
                friend[id].remove(item)
            else:
                group[id].remove(item)
        else:
            count = count + 1 
            msg_to_send = msg_to_send + str(count) + ". " + name + "在" + date_str + ',\n'
            msg_to_send = msg_to_send + "  " + "还剩" + str(day_left) + "天。\n"

    if msg_to_send == "":
        if flag==1:
            bot.send_friend_msg(qq=int(id), msg="无日程,之后不再提醒")
        else:
            bot.send_group_msg(group=int(id), msg="无日程,之后不再提醒")
    else:
        if flag==1:
            bot.send_friend_msg(qq=int(id), msg=msg_to_send)
        else:
            bot.send_group_msg(group=int(id), msg=msg_to_send)

    # np.save("friend.npy",friend)
    # np.save("group.npy",group)
    friend_json = json.dumps(friend,sort_keys=False,indent=4,separators=(",",": "))
    group_json = json.dumps(group,sort_keys=False,indent=4,separators=(",",": "))

    with open("friend.json","w") as f:
    	f.write(friend_json)

    with open("group.json","w") as f:
        f.write(group_json)

@miraicle.Mirai.receiver('GroupMessage')
def hello_to_group(bot: miraicle.Mirai, msg: miraicle.GroupMessage):
    global friend,group
    select = re.match(r"#添加 (.+) (\d*-\d*-\d*)",msg.text)
    if select:
        try:
            datetime.datetime.strptime(select.group(2),"%Y-%m-%d").date()
        except:
            bot.send_group_msg(group=msg.group, msg="时间格式有误")
        else:
            sender = str(msg.group)
            if sender in group:
                group[sender].append(select.group(1)+" "+select.group(2))
                send_message(bot,sender,0)
            else:
                group[sender] = []
                group[sender].append(select.group(1)+" "+select.group(2))
                send_message(bot,sender,0)

    select = re.match(r"#取消 (\d*)",msg.text)
    if select:
        try:
            n = int(select.group(1))
        except:
            bot.send_group_msg(group=msg.group, msg="输入格式有误")
        else:
            sender = str(msg.group)
            if sender not in group:
                bot.send_group_msg(group=msg.group, msg="无记录")
            elif n>len(group[sender]) or n <=0:
                bot.send_group_msg(group=msg.group, msg="无此条记录")
            else:
                del group[sender][n-1]
                send_message(bot,sender,0)

    if(msg.text=="#查询"):
        sender = str(msg.group)
        if sender not in group:
            bot.send_group_msg(group=msg.group, msg="无记录")
        elif group[sender]==[]:
            bot.send_group_msg(group=msg.group, msg="无记录")
        else:
            send_message(bot,sender,0)
    
    if(msg.text=="#命令"):
        bot.send_group_msg(group=msg.group, msg="1. #添加 事件 年-月-日\n2. #取消 序号\n3. #查询")


@miraicle.Mirai.receiver('FriendMessage')
def hello_to_friend(bot: miraicle.Mirai, msg: miraicle.FriendMessage):
    global friend,group
    select = re.match(r"#添加 (.+) (\d*-\d*-\d*)",msg.text)
    if select:
        try:
            datetime.datetime.strptime(select.group(2),"%Y-%m-%d").date()
        except:
            bot.send_friend_msg(qq=msg.sender, msg="时间格式有误")
        else:
            sender = str(msg.sender)
            if sender in friend:
                friend[sender].append(select.group(1)+" "+select.group(2))
                send_message(bot,sender,1)
            else:
                friend[sender] = []
                friend[sender].append(select.group(1)+" "+select.group(2))
                send_message(bot,sender,1)
                #print(friend)
    else:
        pass

    select = re.match(r"#取消 (\d*)",msg.text)
    if select:
        try:
            n = int(select.group(1))
        except:
            bot.send_friend_msg(qq=msg.sender, msg="输入格式有误")
        else:
            sender = str(msg.sender)
            if sender not in friend:
                bot.send_friend_msg(qq=msg.sender, msg="无记录")
            elif n>len(friend[sender]) or n <=0:
                bot.send_friend_msg(qq=msg.sender, msg="无此条记录")
            else:
                del friend[sender][n-1]
                send_message(bot,sender,1)

    if(msg.text=="#查询"):
        sender = str(msg.sender)
        if sender not in friend:
            bot.send_friend_msg(qq=msg.sender, msg="无记录")
        elif friend[sender]==[]:
            bot.send_friend_msg(qq=msg.sender, msg="无记录")
        else:
            send_message(bot,sender,1)

    if(msg.text=="#命令"):
        bot.send_friend_msg(qq=msg.sender, msg="1. #添加 事件 年-月-日\n2. #取消 序号\n3. #查询")


    if(msg.text=="#恢复"):
    	with open("friend.json","r") as f:
            friend = json.load(f)
        
    	with open("group.json","r") as f:
        	group = json.load(f)
	    
    	bot.send_friend_msg(qq=msg.sender, msg="已恢复")

@miraicle.scheduled_job(miraicle.Scheduler.every().day.at('8:00'))
def morning(bot: miraicle.Mirai):
    global friend,group
    for i in friend:
        if friend[i] != []:
            send_message(bot,i,1)
        
    for i in group:
        if group[i] !=[]:
            send_message(bot,i,0)