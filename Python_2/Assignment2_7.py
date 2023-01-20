

def main():
    print("enter a number:")
    num = int(input())


    for i in range(1,num):
        for j in range(1,num+1):
            print(j,end=" ")
        print()


if __name__ == "__main__":
    main()