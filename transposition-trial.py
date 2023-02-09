f = open("message.txt", "r", encoding="UTF-8")
s = f.read()

n=3
s3 = [s[i:i+n] for i in range(0, len(s), n)]
result = []

for i in range(len(s3)):
    result.append(s3[i][2]+s3[i][0]+s3[i][1])

print(''.join(result))
