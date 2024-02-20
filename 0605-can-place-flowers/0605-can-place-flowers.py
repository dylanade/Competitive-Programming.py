class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=0
        while i < len(flowerbed):
            if (i==0 or flowerbed[i-1]==0)and (flowerbed[i]==0)and (i==len(flowerbed)-1 or flowerbed[i+1]==0):
                n=n-1
                i=i+2
            else:
                i=i+1
        return n<=0
        