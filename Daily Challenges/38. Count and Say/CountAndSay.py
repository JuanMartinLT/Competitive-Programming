class Solution:
    def countAndSay(self, n: int) -> str:
        cnt = 1
        ans = "1"
        while cnt<n:
            cur = []
            for s,amt in groupby(ans):
                cur.append(str(len(list(amt))))
                cur.append(s)
            ans = ''.join(cur)
            cnt+=1
        return ans