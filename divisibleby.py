# num = int(input("Please choose a number to divide: "))
#
# listRange = list(range(1,num+1))
#
# divisorList = []
#
# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)
#
# print(divisorList)

# num = int(input("Please choose a number to divide: "))
#
# listRange= list(range(1,num+1))
# divisorList= []
# for i in listRange:
#     if num % i ==0:
#         divisorList.append(i)
# print(divisorList)


num = int(input("Please choose a number to divide: "))
listRange = list(range(1,num+1))
divisorlist = []
for i in listRange:
    if num%i== 0:
        divisorlist.append(i)
print(divisorlist)