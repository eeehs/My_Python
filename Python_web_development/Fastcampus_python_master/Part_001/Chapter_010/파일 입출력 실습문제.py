import csv

file = open("Python_web_development\Fastcampus_python_master\Part_001\Chapter_010\mystock.csv","r",encoding="utf-8-sig")

reader = csv.reader(file)

samsung = []
naver = []

i = 0
for data in reader:
    if i == 1:
        samsung.append(data)
    if i == 2:
        naver.append(data)
    i = i + 1
file.close()

samsung_proceeds = (int(samsung[0][3]) - int(samsung[0][1])) * int(samsung[0][2])
samsung_yield = (int(samsung[0][3])/(int(samsung[0][1])-1)) * 100

naver_proceeds = (int(naver[0][3]) - int(naver[0][1])) * int(naver[0][2])
naver_yield = (int(naver[0][3])/(int(naver[0][1])-1)) * 100

print(f"""
삼성전자 {samsung_proceeds} {samsung_yield}
NAVER {naver_proceeds} {naver_yield}
""")