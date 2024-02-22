class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                curr_sum, count = img[i][j], 1
                
                if i != 0:
                    curr_sum += img[i-1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i-1][j-1]
                        count += 1
                        
                    if j != n-1:
                        curr_sum += img[i-1][j+1]
                        count += 1
                    
                if i != m-1:
                    curr_sum += img[i+1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i+1][j-1]
                        count += 1
                        
                    if j != n-1:
                        curr_sum += img[i+1][j+1]
                        count += 1
                        
                if j != 0:
                    curr_sum += img[i][j-1]
                    count += 1
                    
                if j != n-1:
                    curr_sum += img[i][j+1]
                    count += 1
                    
                avg = curr_sum // count
                curr_sum = avg
                ans[i][j] = avg
                
        return ans
                