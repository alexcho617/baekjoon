# import sys 
# S1 = sys.stdin.readline().strip().upper() 
# S2 = sys.stdin.readline().strip().upper() 
# len1 = len(S1) 
# len2 = len(S2) 
# matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 
# for i in range(1, len1 + 1): 
#     for j in range(1, len2 + 1): 
#         if S1[i - 1] == S2[j - 1]: 
#             matrix[i][j] = matrix[i - 1][j - 1] + 1 
#         else: 
#             matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]) 
# print(matrix[-1][-1])






#/https://www.acmicpc.net/problem/9251
#LCS
import sys
s1 = sys.stdin.readline().strip().upper()
s2= sys.stdin.readline().strip().upper()

len1 = len(s1)
len2 = len(s2)
matrix = [[0]*(len2+1)]*(len1+1)
    
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] 

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if s1[i-1] == s2[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
print(matrix[-1][-1])