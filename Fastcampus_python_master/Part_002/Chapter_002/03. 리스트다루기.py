# 리스트 메서드 

# 리스트 데이터 삭제 
fruits = ['apple','orange','mango']
del fruits[1]
print(fruits)

# 리스트 정렬

numbers =[5,2,8,1,10]
numbers.sort()
print(numbers)

# enumerate

for index, number in enumerate(numbers , 1):
    print(index,number)