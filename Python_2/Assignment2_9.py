
def countDigit(n):
    count = 0
    while n !=0:
        n//=10
       # count+=1
        count = count+1
    return count
def main():
    print("enter numberrs")
    num = int(input())

    print(countDigit(num))



if __name__ == "__main__":
    main()