class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        row, col = len(img), len(img[0])
        ans = [[0] * col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                curr_sum, count = img[i][j], 1
                
                if i != 0:
                    curr_sum += img[i-1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i-1][j-1]
                        count += 1
                        
                    if j != col-1:
                        curr_sum += img[i-1][j+1]
                        count += 1
                    
                if i != row-1:
                    curr_sum += img[i+1][j]
                    count += 1
                    
                    if j != 0:
                        curr_sum += img[i+1][j-1]
                        count += 1
                        
                    if j != col-1:
                        curr_sum += img[i+1][j+1]
                        count += 1
                        
                if j != 0:
                    curr_sum += img[i][j-1]
                    count += 1
                    
                if j != col-1:
                    curr_sum += img[i][j+1]
                    count += 1

                ans[i][j] = curr_sum // count
                
        return ans
                