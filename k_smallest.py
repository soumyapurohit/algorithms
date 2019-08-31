list = [5,2,13,19]
def smallest(list):
    k = 1
    list.sort()
    # time complexity is O nlogn 
    print("k-th smallest number is",list[k-1])

smallest(list)