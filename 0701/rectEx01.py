def get_rect_area(w, h):
    """"Calculate the area of a rectangle."""
    return w * h
def main():
    width = float(input("Enter the width of the rectangle."))
    height = float(input("Enter the height of the rectangle."))

    area = get_rect_area(width, height)
    print(f"The area of the rectangle is: {area}")

if __name__ == "__main__":
    main()

    def menu():
        print("1. 섭씨 온도 --> 화씨온도")
        print("2. 화씨 온도 --> 섭씨온도")
        print("3. 종료")
        selection = int(input("메뉴를 선택하세요: "))
        return selection

def ctod(c):
    temp = c*9.0/5.0 + 32
    return temp

def ftoc(f):
    temp = (f - 32.0)*5.0/9.0
    return temp

def input_f():
    F = float(input("화씨 온도를 입력하세요: "))
    return F

def input_c():
    c = float(input("섭씨 온도를 입력하세요: "))
    return c
def main():
    while True:
        index = menu()
        if index == 1 :
            t = input_c()
            t2 + ctof(t)
            print("화씨온도 = "< t2, "\n")
        elif index == 2:
            t = input_f()
            t2 = ftoc(t)
            print("섭씨온도 = ", t2, "\n")
        else :
            break
main()