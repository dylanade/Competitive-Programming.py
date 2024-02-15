class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens = {}
        self.duration = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if (tokenId in self.tokens.keys()):
            duration = self.tokens[tokenId]
            if (duration + self.duration) > currentTime:
                self.tokens[tokenId] = currentTime
                

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        
        for duration in self.tokens.values():
            if duration + self.duration > currentTime:
                count += 1
                
        return count
        

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)