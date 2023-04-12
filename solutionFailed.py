#The function uses three nested loops to iterate over all possible combinations of indices (i, j, k) that satisfy the constraints. 
#For each combination, it checks if l[i] divides l[j] and l[j] divides l[k]. 
#If both conditions are satisfied, the count is incremented.

#The time complexity of the function is O(n^3), where n is the length of the input list. 
#Note that if there are no lucky triples, the function returns 0.

#Only passes 4 out of 5 test cases

def solution(l):
    count = 0
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:
                for k in range(j+1, n):
                    if l[k] % l[j] == 0:
                        count += 1
    return count

print(solution([1, 2, 3, 4, 5, 6])) # Expected Output: 3

print(solution([1, 1, 1])) #Expected Output: 1



