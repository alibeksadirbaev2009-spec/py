# 1 qaysi  bir u'lken
k = int(input("k = "))
l = int(input("l = "))
if k == l:
    print("ekewi ten'")
elif k > l:
    print("k u'lken")
else:
    print("l u'lken")

# 2 ball
ball = int(input("ball = "))
if 90 <= ball <= 100:
    print(5)                        
elif 70 <= ball <= 89:
    print(4)
elif 69 <= ball <= 79:
    print(3)
elif 0 <= ball <= 68:
    print(2)
else:
    print("mistake")
