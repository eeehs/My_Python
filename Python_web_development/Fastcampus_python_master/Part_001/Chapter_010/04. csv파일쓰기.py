import csv 

data = [
    ["이름", "반", "번호"],
    ["제석",1,20],
    ["홍철",3,8],
    ["형돈",5,32],
]

file = open("student.csv","w",newline="",encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()