
def number(no):
    if(no%5==0):
        return "true"
    else:
        return "false"

def main():
    print("Enter number")
    num1 = input()

    Divisions = number(int(num1))

    print(Divisions)


if __name__ == "__main__":
    main()