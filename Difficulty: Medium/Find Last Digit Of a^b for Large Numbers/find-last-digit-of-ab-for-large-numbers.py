#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        a=int(a)%10
        b=int(b)
        n=pow(a,b,10)
        return n
        
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(str,input().split())
        
        ob = Solution()
        print(ob.getLastDigit(a,b))
# } Driver Code Ends