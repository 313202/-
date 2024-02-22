import hashlib
 
i = 0
while True:
    if hashlib.md5(str(i).encode('utf-8')).hexdigest()[0:5] == 'df661':
        print(i)
        break
    i = i+1