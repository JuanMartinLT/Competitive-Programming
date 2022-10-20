class Solution:
    def intToRoman(self, num: int) -> str:
        
        lookup  = {1: 'I',4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50:'L', 90: 'XC', 100: 'C',
              400: 'CD', 500: 'D', 900 : 'CM', 1000: 'M' }
        
        ans = []
        arr = sorted(zip(lookup.keys(),lookup.values()),key=lambda f:f[0])
        while num!=0:
            nxt = 0
            nxtch = ''
            for val,ch in arr:
                if val>nxt and num>=val:
                    nxt = val
                    nxtch = ch
            num -= nxt
            ans.append(nxtch)
        return ''.join(ans)