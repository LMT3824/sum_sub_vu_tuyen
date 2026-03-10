def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    x = int(input("Nhập số thứ nhất: "))
    y = int(input("Nhập số thứ hai: "))

    print("Sum:", sum(x, y))
    print("Sub:", sub(x, y))