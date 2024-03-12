import random

r = random.randint(1, 100)
while True:
	ans = input('請輸入數字：')
	ans = int(ans)
	if r == ans:
		print('正確')
		break
	else:
		if r < ans:
			print('比答案大，請重新輸入')
		else:
			print('比答案小，請重新輸入')	
    
