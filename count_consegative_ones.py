def count_consegative_ones(arr):
    count, maximum = 0, 0 

    for item in arr:
        if item == 1:
            if count >= maximum:
                count += 1
                maximum += 1
            else:
                count += 1
        else:
            count = 0
    return maximum

if __name__ == "__main__":
    arr = [1,1,0,1,1,1,0,1,1]

    print(count_consegative_ones(arr))