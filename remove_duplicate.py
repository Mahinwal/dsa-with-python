def remove_duplicate(arr):
    ptr = arr[0]
    output = []
    output.append(ptr)

    for item in arr[1:]:
        if item != ptr:
            output.append(item)
            ptr = item
    return output


if __name__ == "__main__":
    duplicate_arr = [1, 1, 2, 2, 2, 3, 3, 4]
    print(remove_duplicate(duplicate_arr))

    # One liner solution 
    print(list(set(duplicate_arr)))
    