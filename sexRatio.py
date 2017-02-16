# coding: utf-8
# usage:
# 1. pip install itchat
# 2. python .py
# 3. scan the QR code with your phone and get the results

import itchat

itchat.auto_login(hotReload = True)

friendList = itchat.get_friends(update=True)[1:]

sexDict = {}
total = len(friendList)
for friend in friendList:
	if not friend['Sex'] in sexDict:
		sexDict[friend['Sex']] = []
	sexDict[friend['Sex']].append(friend['NickName'])

unknown = len(sexDict[0])
male = len(sexDict[1])
female = len(sexDict[2])

ratio = int (male * 100.0/ (male + female))

print '您共有好友 %s位，\n未知性别信息 %d位，男性 %d位，女性 %d位。\n男女比例 %d: %d' % (total, unknown, male, female, ratio, 100 - ratio)