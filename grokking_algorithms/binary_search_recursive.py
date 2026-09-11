numbers = [1, 2, 3, 5, 7, 11, 13, 17] ## 8 // 2
       ## [1, 2, 3, 5, 7][11, 13, 17, 92]

def binary_search(list, target, low, high):
    n = len(list)

    if low > high:
        return "Number not Found"
    
    mid = (low + high) // 2
    guess = list[mid]

    if guess == target:
        return mid
    elif guess > target:
        high = mid - 1
        return binary_search(list, target, low, high)
    else:
        low = mid + 1
        return binary_search(list, target, low, high)

## Have to return the array with the half that contains the target
print(binary_search(numbers, 88, 0, len(numbers) - 1))