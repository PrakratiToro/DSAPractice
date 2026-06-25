def two_sum(arr,target):
    hash_map = {}
    for i,num in enumerate(arr):
        complement = target - num
        if complement in hash_map:
            return (hash_map[complement],i)
        hash_map[num] = i
    return []
    
    
print(two_sum([1,2,3,4,15],7))