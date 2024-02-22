class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(img), len(img[0])
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                curr_sum, count = img[i][j], 1
                
                if i != 0:
                    curr_sum += img[i-1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i-1][j-1]
                        count += 1
                        
                    if j != cols-1:
                        curr_sum += img[i-1][j+1]
                        count += 1
                    
                if i != rows-1:
                    curr_sum += img[i+1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i+1][j-1]
                        count += 1
                        
                    if j != cols-1:
                        curr_sum += img[i+1][j+1]
                        count += 1
                        
                if j != 0:
                    curr_sum += img[i][j-1]
                    count += 1
                    
                if j != cols-1:
                    curr_sum += img[i][j+1]
                    count += 1
                    
                avg = curr_sum // count
                curr_sum = avg
                ans[i][j] = avg
                
        return ans
                