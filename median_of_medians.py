import numpy as np
def divide(arr,size=5):
    # arr = [1,2,3,4,5,6,7,8,9,10]->[1,2,3,4,5] & [6,7,8,9,10]
    final = []
    median = []
    for i in range(0, len(arr), size):
        final.append(arr[i:i+size])
        median.append(np.median(arr[i:i+size]))
    return final, median
        
def MoM(arr,k):
    # Length of arr
    n = len(arr)
    # If less than 10, then brute force and find k-th smallest
    if n<=10:
        return sorted(arr)[k-1]
    
    # Call divide into groups of size n/5 
    groups,medians = divide(arr,5)
    
    # Call Median of Median on medians of each group
    b = MoM(medians,len(medians)//2)
    
    # Create a partion of all items left and right of b
    left_partion = []
    right_partion = []
    for num in arr:
        if num<b:
            left_partion.append(num)
        else:
            right_partion.append(num)
    
    kprime = len(left_partion) # rank
    
    # Check if the rank is greater or less than the current k
    if kprime > k:
        arrprime = left_partion
        return MoM(arrprime,k)
    elif kprime < k:
        arrprime = right_partion
        return MoM(arrprime,k-kprime)
    else:
        return b

    
    
arr = [776, 430, 817, 937, 992, 123, 424, 597, 264, 921, 197, 67, 421, 748, 429, 13, 21, 31, 881, 169, 233, 275, 735, 267, 64, 903, 686, 286, 540, 876, 909, 619, 123, 843, 654, 350, 189, 447, 387, 482, 365, 813, 244, 555, 748, 871, 253, 490, 825, 362, 152, 604, 401, 315, 768, 975, 914, 50, 621, 933, 180, 574, 49, 990, 622, 366, 984, 512, 423, 986, 472, 854, 193, 205, 584, 673, 428, 900, 839, 795, 408, 403, 756, 59, 80, 146, 292, 726, 800, 843, 207, 791, 172, 784, 979, 148, 219, 296, 20, 931]



#arr = [1,2,3,4,5,6,7,16,17,18,19,20]
print(MoM(arr,13))