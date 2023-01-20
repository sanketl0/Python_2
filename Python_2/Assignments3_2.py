

def maximumElement(Arr):
    maxValue = Arr[0]
    for i in Arr:
        if i >  maxValue:
            maxValue = i
    return maxValue

def main():
    Arr = []

    print("Size of list : ")
    size = int(input())

    for i in range(0,size):
        print("Enter a values : ")
        value = int(input())
        Arr.append(value)

    print("Our list is : ",Arr)
    print("The maximum element of list is ",maximumElement(Arr))

if __name__ == '__main__':
    main()