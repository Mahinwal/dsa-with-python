def findLargestElement(ar):
    n = len(ar)

    if n == 1:
        return ar[0]
    else:
        largest = ar[0]
        for i in range(1, n):
            if ar[i] > largest:
                largest = ar[i]
        return largest
    
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    largest = findLargestElement(arr1)
    print("The largest element in the array is:", largest)


    arr2 = [8, 10, 5, 7, 9]
    largest = findLargestElement(arr2)
    print("The largest element in the array is:", largest)

    arr3 = [-5, -6, -10, -3, -7]
    largest = findLargestElement(arr3)
    print("The largest element in the array is:", largest)

    arr4 = [7]
    largest = findLargestElement(arr4)
    print("The largest element in the array is:", largest)
