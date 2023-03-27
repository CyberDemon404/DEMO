#coding=utf-8
import os, sys, platform
 
os.system('xdg-open https://t.me/cyberdemon404')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf codex1.so')
except:
    pass
os.system('rm -rf codex.so')
os.system('git pull')
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('codex1.so'):
        os.system('curl -L https://github.com/cyberdemon404/Demo/blob/main/codex1.cpython-311.so?raw=true -o codex1.so') 
        __import__("codex1").qsbuy()
    else:
        __import__("codex1").qsbuy()
 
elif bit == '32bit':
    if not os.path.isfile('codex1.so'):
        os.system('curl -L https://github.com/cyberdemon404/Demo/blob/main/codex1.cpython-311.so?raw=true -o codex1.so') 
        __import__("codex1").qsbuy()
    else:
        __import__("codex1").qsbuy()
