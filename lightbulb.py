def solution(A):
    # write your code in Python 3.6

    #counts number of times lights are on    
    counter = 0
    
    for num in A:
        #if first number in list is 1, light is on
        if A[0] == 1:
            counter += 1
        elif A[0:num] == range(1,num + 1):
            counter += 1
            
    
    return counter

print solution([1,3,4,2,5])
print solution([2, 3, 4, 1, 5])
print solution([2, 1, 3, 5, 4])