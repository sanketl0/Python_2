
def checkPrime(num):
    for i in range(1,num):
        if (num % i)==0:
            print("prime nmmber")
            break
        else:
            print("not prime number")



def main():

   print("enter a number :")
   num = int(input())

   checkPrime(num)

if __name__ == "__main__":
    main()