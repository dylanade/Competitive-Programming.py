class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        import collections
        counter = collections.defaultdict(int)

        for bill in bills:
            if bill == 5:
                counter[5] += 1
            elif bill == 10:
                if counter[5] > 0:
                    counter[5] -= 1
                    counter[10] += 1
                else:
                    return False
            elif bill == 20:
                if counter[5] > 0 and counter[10] > 0:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False
            else:
                return False

        return True