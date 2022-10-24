word_list = ["apple","watch","apolo","star","abocado"]

# 리스트 내포 사용하기 전 
result = []
for word in word_list:
    if word[0] =='a':
        result.append(word)
    
print(result)

# 리스트 내포 사용하기 전 

result = [i for i in word_list if i[0] == 'a']

print(result)