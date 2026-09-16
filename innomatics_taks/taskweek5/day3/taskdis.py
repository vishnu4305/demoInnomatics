# # problem 1
# numbers = [12, 7, 5, 18, 20, 9, 14]
# even = list(filter(lambda i : i %2 == 0 , numbers))
# print(even)

# # problem2 
# marks = [25, 40, 89, 30, 75, 55, 18]
# passed_m = list(filter(lambda i : i>=35,marks ))
# print(passed_m)

# #problem 3
# numbers = [-10, 15, -8, 20, 0, 35, -2]
# pos_num = list(filter(lambda i : i>0 ,numbers))
# print(pos_num)

# #problem 4
# words = ["cat", "elephant", "dog", "computer", "pen", "keyboard"]
# long_word = list(filter(lambda i : len(i)>5 , words))
# print(long_word)

## problem 5
# numbers = [10, 12, 15, 18, 20, 23, 25, 31]
# Mul_num =list(filter(lambda i : i % 5 == 0 , numbers))
# print(Mul_num)


#Reduce
#probelm 6
from functools import reduce
# numbers = [10, 20, 30, 40, 50]
# sum_num = reduce(lambda x,y : x+y , numbers)
# print(sum_num)

# #prob 7
# numbers = [2, 3, 4, 5]
# Pro_num = reduce(lambda x,y : x*y ,numbers)
# print(Pro_num)

# #problem 8
# numbers = [45, 12, 98, 67, 21]
# lar_num = reduce(lambda x,y : x if x>y else y, numbers)
# print(lar_num)

# #problem 9
# numbers = [34, 8, 76, 12, 4, 91]
# sma_num = reduce(lambda x,y : x if x<y else y, numbers)
# print(sma_num)

# # problem 10
# words = ["apple", "banana", "kiwi", "watermelon", "grapes"]
# long_words = reduce(lambda x , y : x if len(x)> len(y) else y ,words)
# print(long_words)

#Bonus
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
red_num = reduce(lambda x ,y: x+y , list(map(lambda x : x*2 , list(filter(lambda x : x>20 ,numbers)))))
print(red_num)