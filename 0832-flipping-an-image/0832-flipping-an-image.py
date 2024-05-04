class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j, bit in enumerate(image[i][::-1]):
                image[i][j] = 0 if bit == 1 else 1
        return image