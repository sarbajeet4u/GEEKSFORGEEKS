#User function Template for python3

class Solution:
    def isDigitSumPalindrome(self,N):
        #code here
        
        num1 = 0
        
        for i in str(N):
            num1 += int(i)
            
        num2 = str(num1)[::-1]
        
        if num1 == int(num2):
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends