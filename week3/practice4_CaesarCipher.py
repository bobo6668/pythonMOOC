# CaesarCipher
oriStr = input()
for i in oriStr:
    ordI = ord(i)
    if ordI >= ord('a') and ordI <= ord('z'):
        print( chr( (ordI - ord('a') + 3) % 26 + ord('a') ), end = "")
    elif ordI >= ord('A') and ordI <= ord('Z'):
        print( chr( (ordI - ord('A') + 3) % 26 + ord('A') ), end = "")
    else:
        print(i, end = "")
