class Solution:
    def smallestNumber(self, num: int) -> int:
        ans = ''
        i = 0
        if num >= -9 and num <= 9:
            return num
        elif num > 9:
            result = sorted(list(str(num)))
            while result[i] == '0' and i < len(result):
                i += 1
            last = ''.join(result[i+1:])
            ans += f"{result[i]}{i*'0'}{last}"
        else:
            n = str(num)[1:]
            result = sorted(list(str(num)), reverse=True)
            while result[i] == '0' and i < len(result):
                i += 1
            last = ''.join(result[i+1:len(result)-1])
            ans += f"-{result[i]}{i*'0'}{last}"
        return int(ans)