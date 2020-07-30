# Function to find all interleaving of X and Y
def findInterleavings(X, Y, result=set(), curr=''):
    print(X,Y,result,curr)
 
    # insert curr into set if we have reached end of both Strings
    if not X and not Y:
        result.add(curr)
        return result
 
    # if X is empty, append its first character not in the
    # result and recur for remaining substring
    if X:
        result = findInterleavings(X[1:], Y, result, curr + X[0])
 
    # if Y is empty, append its first character not in the
    # result and recur for remaining substring
    if Y:
        result = findInterleavings(X, Y[1:], result, curr + Y[0])
 
    return result
 
 
if __name__ == '__main__':
 
    X = "AB"
    Y = "CD"
 
    # use set to handle duplicates
    result = findInterleavings(X, Y)
    print(result)
