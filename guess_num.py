import random
start = input('請決定隨機數字範圍開始值')
end =  input('請決定隨機數字結束值')
start =int(start)
end = int(end)
r = random.randint(start,end)
i = 0
while True:
	guess = input('1至100中，請猜一個數字：')
	guess = int(guess)
	i = i + 1
	if guess == r:
		print ('恭喜猜中了！', '這是你猜的第', i, '次')
		break
	elif guess > r:
		print ('比答案大')
	elif guess < r:
		print ('比答案小')
	print ('這是你猜的第', i, '次')



