from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        answer = deque()
        for card in deck:
            if answer:
                answer.appendleft(answer.pop())
            answer.appendleft(card)
        return list(answer)