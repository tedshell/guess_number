import random
start = input('請輸入範圍開始值')
end = input('請輸入範圍結束值')
s = int(start)
e = int(end)

r = random.randint(s, e)
count = 0
while True:
	count += 1 #count = count + 1
	ans = input('請輸入數字：')
	ans = int(ans)
	if r == ans:
		print('正確')
		print('你猜了', count, '次')
		break
	else:
		if r < ans:
			print('比答案大')
		else:
			print('比答案小')	
	print('你猜了', count, '次')
    
