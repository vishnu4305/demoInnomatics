

# list_fruit = []
# input_a = input("Enter no of fruits:")
# input_b = input("List of fruits and cart :")
# b = input_b.split(",",int(input_a))

# a = list(input_b.split(","))
# for i in range(int(input_a)):
#     list(b.pop(0))
#     list(b.remove([))
#     list(b.remove(]))

# print(b)

# c= list(b[:int(input_a)])
# print(c)

# # for i in input_a:
# #     list_fruit.appendb[0]



















menu = int(input("No of menus :")) #5
Nmenu=[]
for i in range(menu):
    n = map(int,input().split(","))
    Nmenu.append(list(n))
# print(Nmenu)
count1 = []
MaxCount = 0
MaxCountlist = []
for i in Nmenu:
    count1.append(len(i))
print(count1)


count = 0
for i in len(Nmenu):
    if i >= MaxCount:
        MaxCount = i
        if i in MaxCountlist:
            MaxCountlist.clear(int(i))
            if i not in MaxCountlist:
                MaxCountlist.append(int(i))

print(MaxCountlist)
if len(MaxCountlist) < 1:
    print(MaxCountlist)
else:

    
    































menu_size=int(input('Enter the number: '))
menu1=[]
for i in range(menu_size):
    menu = input().split(",")
    n_list= []
    for i in menu:
        n_list.append(int(i))
    menu1.append(n_list)

maxsubarray=0
for i in range(len(menu1)):
    if maxsubarray < len(menu1[i]):
        maxsubarray =len(menu1[i])
    
maxsubarrays =[]

for i in range(len(menu1)):
    if len(menu1[i]) == maxsubarray:
        maxsubarrays.append(menu1[i])

if len(maxsubarrays)==1:
    print(maxsubarrays[0])
else:
    m = maxsubarrays[0]
    count = {}
    for price in m:
        if price not in count:
            count[price] = 1
        else:
            count[price] += 1
    most_repeated_price = 0
    max_count = 0
    for price in count:
        if count[price] > max_count:
            most_repeated_price = price
            max_count = count[price]

    max_total = most_repeated_price * max_count

    max_avg = sum(m) / len(m)

    for menu in maxsubarrays[1:]:
        count = {}
        for price in menu:
            if price not in count:
                count[price] = 1
            else:
                count[price] += 1
        most_repeated_price1 = 0
        count1 = 0
        for price in count:
            if count[price] > count1:
                most_repeated_price1 = price
                count1 = count[price]
        total1 = most_repeated_price1 * count1
        avg1 = sum(menu) / len(menu)

    
        if count1 > max_count:
            m = menu
            max_count = count1
            max_total = total1
            max_avg = avg1
        elif count1 == max_count:
            if total1 > max_total:
                m = menu
                max_total = total1
                max_avg = avg1
            elif total1 == max_total:
                if avg1 > max_avg:
                    m = menu
                    max_avg = avg1
print(m)


    
    
    


