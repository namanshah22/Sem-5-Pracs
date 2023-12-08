def add(A, M):
    carry = 0
    result = ""
    for i in range(len(A)-1,-1, -1):
        res = int(A[i]) + int(M[i]) + carry
        if res == 2:
            carry = 1
            res = 0
        elif res == 3:
            carry = 1    
            res = 1
        else:
            carry = 0
        result = str(res) + result      
    return result     

def twosComplement(num):
    # one's complement 
    n = len(num)
    comp = ""
    for i in range(n):
        if num[i] == '0':
            comp += '1'
        else:
            comp += '0'
    # adding 1        
    comp = add(comp, '1'.zfill(n))
    return comp
            
def leftShift(A, Q):
    A = A[1:] + Q[0]
    Q = Q[1:]
    return A, Q

def non_restoringDivision(M, Q):
    count = len(bin(Q)[2:]) + 1

    A = "".zfill(count)
    Q = bin(Q)[2:]
    M = bin(M)[2:].zfill(count)
    M_neg = twosComplement(M)

    print(f"\tA\t  Q \tM  \tAction")
    for i in range(count-1):
        print(A, Q, M, f" init      itr {i}")    

        A, Q = leftShift(A, Q)
        print(A, Q+"_", M, f" LS        itr {i}")

        if A[0] == '1':
            A = add(A, M)
        else:   
            A = add(A, M_neg)
        print(A, Q+"_", M, f" add/subt  itr {i}")

        if A[0] == '1':
            Q += '0'
        else:
            Q += '1'
        print(A, Q, M, f" Q-bit     itr {i}")    
    
    if A[0] == '1':
        A = add(A,M)

    print(A, Q)
    return A, Q

# input M & Q in decimal
Q = int(input("Enter the dividend in decimal form : "))
M = int(input("Enter the divisor in decimal form : "))

remainder, quotient = non_restoringDivision(M, Q)
quotient = int(quotient, 2)
remainder = int(remainder, 2)

print("The quotient is ", quotient)
print("The remainder is ", remainder)