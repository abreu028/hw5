#!/usr/bin/env python3
# -*- coding: raw_unicode_escape:replace -*-
#                                                
blob = ''' àÇübñÀ¬iKU7MŒ2j†Ø»ØöAA÷%íÚóÉÑîTèïæU"+p)å&ÎWÛ{+“UHŒiõ‚"m£Ûûo®%=˜¬årþ5îz;„õÛË_£Á¼¬-
‹>kŽçP3ýÌú3F8¹Ó¢P|ygDr>Æ'''

import sys
def pollytalks(line):
    print(''' \\\\
 (o> - (''', line, ''')\n //\\
_V_/__
 ||
 ||''')

sum = 0
for i in range(len(blob)):
    sum += ord(blob[i])
if sum % 10 == 6:
    print("My name is polly!(I am not a bunny or a spie...or am I?)")
    for line in sys.stdin:
        pollytalks(line.strip())
else:
    print("My name is polly!(I am not a bunny or a spie...or am I?)")
    file = open("pwn.txt", "w")
    for line in sys.stdin:
        pollytalks(line.strip())
        file.write(line.strip() + "\n")
    file.close()
