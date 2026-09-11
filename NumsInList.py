list = [2,4,7,3,1,5,9,5,8,2,9,4,6,11,5,2,66,2,0,1,9]
print("Original list: ", list)

def count_items(list, n):
    if n <= 0:
        return 0
    return count_items(list, n - 1) + 1

print("Original list size: ", len(list))
print("Recursive list size: ", count_items(list, len(list)))