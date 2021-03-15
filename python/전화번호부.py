menu = 0
friends = []
while menu != 9:
    print("-----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3:
        name = input("이름을 입력하시오: ")
        if name in friends:
            friends.remove(name)
        else:
            print("존재하지 않는 이름입니다.")
    elif menu == 4:
        name = input("이름을 입력하시오: ")
        if name in friends:
            index = friends.index(name) #위치 값을 변수로 선언
            new_name = input("바꿀 이름을 입력하시오: ")
            friends[index] = new_name # del 쓸 필요 없이 간단히 입력
        else:
            print("존재하지 않는 이름입니다.")
# elif menu == 9: 필요 없음

