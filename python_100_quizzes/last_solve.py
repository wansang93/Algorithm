def lcs(x, y):
    m=len(x)
    n=len(y)

    #Syntax is column*rows for memoization table for m*n matrix
    L=[[None]*(n+1) for i in range(m+1)]
    
    #Loop over the memoization table
    for i in range(m+1):
        for j in range(n+1):
            #Initializing first row and cloumn of memoization table
            if i == 0 or j == 0:
                L[i][j]=0
            #Diagonal condtion if equal
            elif x[i-1] == y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            #Diagonal if value is not equal
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    
    #The final resullt
    return L[m][n]

x=input("First string : ")
y=input("Second string: ")
print("The length of LCS is : ",lcs(x,y))