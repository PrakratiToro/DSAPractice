def find_min_rotated(arr):
    left , right = 0 , len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
print(find_min_rotated([30,40,50,10,20]))