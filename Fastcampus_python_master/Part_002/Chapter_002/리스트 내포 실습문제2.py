list = ['오메가','None','비타민C500','None','홍삼절편']


# new_list =[] 

# for i in list:
#     if i == 'None':
#         i = ''
#     new_list.append(i)
# print(new_list)

new_list = [i if i != 'None' else '' for i in list]

print(new_list)

