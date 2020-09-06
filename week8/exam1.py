inputStr = input()
for i in inputStr:
    if ( ord(i) >= ord('a') and ord(i) <= ord('z') ) \
        or ( ord(i) >= ord('A') and ord(i) <= ord('Z') ):
        print(i, end = '')