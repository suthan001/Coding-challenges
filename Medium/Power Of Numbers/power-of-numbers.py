#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        D=1000000007
        p=pow(N,R,D)
        return p
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends