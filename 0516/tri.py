#삼각형의 면적을 구하는 프로그램을 작성하시오.
#삼각형의 면적 = 높이 * 밑변 * 0.5

height = int(input("높이 입력 : "))
base = int(input("밑변 입력 : "))

area = height * base * 0.5

print("높이는", height," 이고 밑변은", base, "인 삼각형의 면적은", area,"입니다.")
