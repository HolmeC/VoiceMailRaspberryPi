# -*- coding: utf-8 -*-
#!usr/bin/env python3
import os
from aip import AipSpeech
#调用百度语音识别API对输入的音频进行识别

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def rec(s):
        print('recording......')
        os.system('arecord -D hw:1,0 -d %d -t wav -c 1 -r 44100 -f S16_LE test.wav' %s)
        print('finish')
        os.system('ffmpeg -y -i test.wav -acodec pcm_s16le -f s16le -ac 1 -ar 16000 test.pcm')

        # 读取文件
        def get_file_content(filePath):
            with open('test.pcm', 'rb') as fp:
                return fp.read()

        # 识别本地文件
        result=client.asr(get_file_content('test.pcm'), 'pcm', 16000, {
            'dev_pid': 1536,
        })
        print(result)

        # 解析返回值，打印语音识别的结果
        if result['err_msg']=='success.':
            word = result['result'][0].encode('utf-8')       # utf-8编码
            if word!='':
                        print (word.decode('utf-8').encode('gbk'))
                        return word
            else:
                print "音频文件不存在或格式错误"
        else:
            print "错误"
	
