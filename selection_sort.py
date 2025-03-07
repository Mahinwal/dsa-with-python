def selection_sort(ls):
    n = len(ls)
    if n < 2:
        return ls
    else:
        sorted_list = ls[:]
        for i in range(n-1):
            min_index = i
            for j in range(i+1, n):
                if sorted_list[j] < sorted_list[min_index]:
                    min_index = j
            sorted_list[i], sorted_list[min_index] = sorted_list[min_index], ls[i]    
        return sorted_list


if __name__ == "__main__":
    numbers = list(map(int, input("Enter the numbers to be sorted: ").split()))
    print(selection_sort(numbers))