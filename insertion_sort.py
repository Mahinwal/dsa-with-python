def insertion_sort(ls):
    n = len(ls)

    if n < 2:
        return ls
    else:
        sorted_list = ls[:]

        for i in range(1, n):
            key = sorted_list[i]
            j = i -1

            while j >= 0 and sorted_list[j] > key:
                sorted_list[j+1] = sorted_list[j]
                j -= 1
            sorted_list[j+1] = key
            
        return sorted_list

if __name__ == "__main__":
    print(insertion_sort([15, 26, 10, 8, 17]))