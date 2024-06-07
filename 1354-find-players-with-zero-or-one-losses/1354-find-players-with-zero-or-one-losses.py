class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # TLE: 124/127
        # winners = set()
        # losers = []

        # for x, y in matches:
        #     winners.add(x)
        #     losers.append(y)
            
        # count = Counter(losers)
        # answer = [[], []]
        # for x in winners:
        #     if x not in losers:
        #         answer[0].append(x)

        # for y in count:
        #     if count[y] == 1:
        #         answer[1].append(y)

        # answer[0].sort()
        # answer[1].sort()
        # return answer

        losers = collections.Counter()
        players = set()

        for x, y in matches:
            losers[y] += 1
            players.add(x)
            players.add(y)

        no_losses = []
        one_loss = []

        for player in players:
            if losers[player] == 0:
                no_losses.append(player)
            elif losers[player] == 1:
                one_loss.append(player)

        return [sorted(no_losses), sorted(one_loss)]
        