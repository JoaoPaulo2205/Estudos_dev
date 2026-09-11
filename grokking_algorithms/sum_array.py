num = [2,4,6]
sum = 0

for i in range (len(num)):
    sum += num[i]

print(len(num))
print("Using for loop: ", sum)

def rec(arr, size):
    if size <= 0:
        return 0
    return rec(arr, size - 1) + arr[size - 1]

print("Using recursion: ", rec(num, len(num)))