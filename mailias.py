# encoding:utf-8
# Copytright sota1235
# Date 2014/02/02

import sys
import os

# .zshrcに追加するalias
argvs = sys.argv
insert = "alias "+argvs[2]+"=\"cd "+argvs[1]+"\""
home = os.environ['HOME']

# 書き込み
f = open(home+'/.zshrc','a+')
f.write(insert)
f.close()
