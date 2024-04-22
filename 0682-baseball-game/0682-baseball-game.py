class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        score = 0
        
        for i in operations:
            if i == "+":
                if len(record)>=2:
                    record.append(int(record[-2])+int(record[-1]))
            elif i == "D":
                if record:
                    record.append(int(record[-1])*2)
            elif i == "C":
                record.pop()
            else:
                record.append(int(i))
        
        return sum(record)
            
                    
                    