Names = []
while True:
    name = input("학생 이름을 입력하세요: ")
    if name == "": #공백 입력 전까지 학생 이름을 입력 받음
        break
    Name.append(name)

print("학생 이름: ")
for name in Names:
    print(name, end=", ") #end="": 가로로 출력, end=", ": ,로 구분
