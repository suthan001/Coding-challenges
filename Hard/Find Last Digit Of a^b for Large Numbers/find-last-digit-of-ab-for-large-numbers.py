#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        a=int(a)%10
        b=int(b)
        result=pow(a,b,10)
        return result



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