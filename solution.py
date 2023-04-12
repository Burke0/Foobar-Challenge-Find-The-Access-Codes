def solution(l):
    # Initialize a list c with zeros to keep track of the count of numbers
    # that l[i] is divisible by
    c = [0] * len(l)
    
    # Initialize a variable count to keep track of the number of lucky triples
    count = 0
    
    for i in range(0, len(l)):
        for j in range(0,i):
            #print('i: ', i, ' j: ', j )
            if l[i] % l[j] == 0:
                
                # If l[i] is divisible by l[j], increment the count in the c list
                # for the current index i
                c[i] += 1
                
                # Add the count of numbers that l[j] is divisible by to the count variable
                # to get the total number of lucky triples
                count += c[j] 
                #print(count)
    
    return count 
  
print(solution([1, 2, 3, 4, 5, 6])) # Expected Output: 3

print(solution([1, 1, 1])) #Expected Output: 1
