print('Hi, this is the counting numbers of your letters')
print('enter your messege here')
message = input()
count = {}
for i in message.upper():
    count.setdefault(i, 0)
    count[i] = count[i]+1
print(count)
print('thanks for using my program')
