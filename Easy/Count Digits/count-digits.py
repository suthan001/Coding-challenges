#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        count=0
        val=N
        while N!=0:
            s=N%10
            if(s!=0 and val%s==0):
                count += 1
            N=N//10
        return count
    
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends