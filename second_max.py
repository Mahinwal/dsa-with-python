def findSecondLargestElement(arr):
    if len(arr) < 2:
        return "List must have at least two unique elements!"

    max, s_max  = arr[0], arr[1]

    if len(arr) == 2 and max == s_max:
        return "List must have at least two unique elements!"

    if max < s_max:
        s_max = arr[0]
        max = arr[1]
        
    for i in range(2, len(arr)):
        if arr[i] > max:
            s_max = max
            max = arr[i]
        elif arr[i] > s_max and arr[i] < max:
            s_max = arr[i]

    if max != s_max:
        return s_max
    else:
        return "No second max number found!"

if __name__ == "__main__":
    test_cases = [
        [7, 12, 12, 12, 12, 12, 12],
        [7, 8, 1, 20, 8, 11, 12],
        [7, 8, 1, 20, 8, 11, 12],
        [-8, -9, 0, -1],
        [10, 10],
        [10],
        [12, 12, 12, 12, 12, 12, 12]
    ]   
    
    for test in test_cases:
        print(findSecondLargestElement(test))