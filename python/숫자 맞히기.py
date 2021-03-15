import random
trial = 0
num = random.randint(1, 101)
print("1부터 100 사이의 숫자를 맞추시오")
while trial < 20:
    guess = int(input("숫자를 입력하시오: "))
    trial += 1
    if guess < num:
        print("낮음!")
    elif guess > num:
        print("높음!")
    else:
        break
if guess == num:
    print("축하합니다. 시도횟수: %d" % trial)
else:
    print("정답은 ", num)
    
