class Solution:
    def findComplement(self, num: int) -> int:
        binary = f'{num:b}'
        complement = ''
        
        for bit in binary:
            if bit == '1':
                complement += '0'
            else:
                complement += '1'
                
        return int(complement, 2)