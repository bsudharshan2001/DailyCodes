class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        flag=False
        while(flag==False):
            if(i*i==x):
                return i
            elif(i*i>x):
                return i-1
            i+=1
                
        