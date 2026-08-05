# 1 
k  = [1, 3, 33, 50, 8, 4, 15, 7, 31, 5, 12, 25, 44, 23, 43, 45, 12, 49]

l = []

n = []

for i in k:
    if i > 25:
       l.append(i)
    else:
        n.append(i)

print(l)
print(n)



# 2
f = "Hello"
g = ""
for i in f:
    g = i + g

print(g)

# 2.1
h = "Hello"
j = "Good"
for i in h:

    if h >= j:
        print("olleH")

# 3

w = [55, 34, 87, 54, 23, 44, 43, 25, 66, 76, 87, 77, 65]
d = []
q = []

for i in w:
    if i % 3 == 0:  # qa'legen san 
        d.append(i)
    else:
        q.append(i)

print(d)
print(q)

# 4

p = [3, 23, 11, 4, 2, 6, 8, 98, 67, 5]

e = []
r = []

for i in p:
    if i % 2 == 0:
        e.append(i)
    else:
        r.append(i)


print(e)
print(r)


# 5
t = int(input("t = "))

for i in range(1, t +1):
    if t % i == 0:
        print(i)