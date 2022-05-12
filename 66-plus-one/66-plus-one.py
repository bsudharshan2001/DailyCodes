class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        i=n-1
        num=0
        j=0
        while(i>=0):
            num+=digits[i]*(10**j)
            i-=1
            j+=1
        num=num+1
        lst = [int(x) for x in str(num)]
        return lst
            
        