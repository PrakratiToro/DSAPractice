from collections import defaultdict

def sliding_window_fixed(l,k):
    window_sum = 0
    for i in range(k):
        window_sum += l[i]
    largest = window_sum
    
    for right in range (k,len(l)):
        left = right - k
        window_sum -= l[left]
        window_sum += l[right]
        largest = max(largest,window_sum)
    return largest
print(sliding_window_fixed([1,2,3,7,4,1],3))

def sliding_window_dynamic(s):
    longest = 0
    l = 0
    counter : dict[str,int] = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]] +=1
        while counter[s[r]] > 1:
            counter[s[l]] -=1
            l+=1
        longest = max(longest,r-l+1)
    return (longest)
   
print(sliding_window_dynamic("abcdbea"))