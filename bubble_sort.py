def bubble_sort(ls):
    n = len(ls)
    if n < 2:
        return ls
    else:
        sorted_list = ls[:]
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if sorted_list[j] > sorted_list[j+1]:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                    swapped = True
            if not swapped:
                break
        
        return sorted_list
    
if __name__ == "__main__":
    print(bubble_sort([20, 13, 24, 36, 42]))