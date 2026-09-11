list = [1,2,99,5,6,7,8,1,22,63,10,59,29,0,31,26,120,44,12]

def max_in_list(list, n, max):
    if n <= 0:
        return max

    if list[n] > max:
      max = list[n]
    return max_in_list(list, n - 1, max)

print(max_in_list(list, len(list) - 1 , list[len(list) - 1]))