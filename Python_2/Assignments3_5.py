
import MarvellousNum
Data_input= []

def Input(Size,arr):
    for i in range(0,Size,1):
        print("Enter values : ")
        value = int(input())
        Data_input.append(value)
    return Data_input

def sum(primeArr):
    sum = 0
    for i in primeArr:
        sum = sum + i
    return sum

def listx():
    print("Enter Size : ")
    size = int(input())

    print("Our Data is : ", Input(size, Data_input))

    print("prime number in our Data is : ", MarvellousNum.ChkPrime(Data_input))

    print("Sum of prime number is : ", sum(MarvellousNum.ChkPrime(Data_input)))


if __name__ == "__main__":
    listx()