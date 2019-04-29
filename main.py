# -*- coding: utf-8 -*-
#!usr/bin/env python3
import receive
import send
import rec
import speak


while(True):
	print('start!')
	listen=rec.rec(7)
	if listen=='我要发邮件':
		send.main()
	elif listen=='最近一封邮件':
		receive.main()
	elif listen=='结束':
		speak.say('end.wav')
		break
	else:
		speak.say('respeak.wav')
	
