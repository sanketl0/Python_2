
def star(num):
    for i in range(0,num,1):
        print(" * ")

def main():
    print("enter number")
    no = int(input())

    star(no)

if __name__ == "__main__":
    main()