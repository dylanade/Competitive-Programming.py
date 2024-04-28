class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        hashmap = {p:s for p,s in zip(pos, speed)} 
        time = None
        fleet = 1
        for p in sorted(pos, reverse=True):
            new_time = (target-p)/hashmap[p]
            if not time:
                time = new_time
            else:
                if new_time > time:
                    fleet += 1
                    time = new_time
        return fleet