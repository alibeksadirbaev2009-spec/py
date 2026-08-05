# 1 
a = int(input("p = kodga qatisi joq "))
print(a > 0)
# 2 
a = int(input("a = "))
print(a % 2 == 0)


# 3
word_1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
word_2 = "hippopotomonstrosesquippedaliophobia"
print(len(word_1) > len(word_2))
print(len(word_1) < len(word_2))
print(len(word_1) == len(word_2))


# 4
word = "pneumonoultramicroscopicsilicovolcanoconiosis"
reversed = word[::-1]
print(reversed)

word = "pneumonoultramicroscopicsilicovolcanoconiosis"
letters = list(word)
letters.sort()
sorted_word = "".join(letters)
print(sorted_word)


# 5
numbers = [100, 1001, 3, 63, 737]
print(max(numbers))
print(min(numbers))


# 6
numbers = [8, 10, 14, 6, 10, 12]
average = sum(numbers) / len(numbers)
print(average)