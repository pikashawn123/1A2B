import random
answer_1 = random.randint(1, 9)
answer_2 = random.randint(1, 9)
answer_3 = random.randint(1, 9)
answer_4 = random.randint(1, 9)
p_answer_l = [0,0,0,0]
count = 0

while answer_1 == answer_2:  
    answer_2 = random.randint(1, 9)
while answer_2 == answer_3 or answer_1 == answer_3:  
    answer_3 = random.randint(1, 9)
while answer_2 == answer_4 or answer_1 == answer_4 or answer_3 == answer_4:  
    answer_4 = random.randint(1, 9)
answer_l = [answer_1, answer_2, answer_3, answer_4]

while True:
    p_answer = int(input('請輸入各位數字皆不相等的四位數: '))
    for i in range(4):
        p_answer_l[3-i] = p_answer % 10
        p_answer = int(p_answer / 10)
    A = 0
    B = 0
    for i in range(4):
        if p_answer_l[i] == answer_l[i]:
            A += 1
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            if p_answer_l[i] == answer_l[j]:
                B += 1
    if A == 4:
        print('你猜對了')
        print(answer_l)
        print('你總共猜了', count, '次')
        break
    print(A, 'A', B, 'B')
    count += 1