arr = [3, 4, 5, 7, 8, 9]
target = 16
num_dict = {}

for key, val in enumerate(arr):
    complement = target - val

    if complement in num_dict:
        print({complement, val})
    
    num_dict[val] = key

