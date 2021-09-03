from collections import Counter
nums = [1,2,2,2,3,6,6,8]
# lookup = Counter(nums)
# res = sorted(lookup,key = lookup.__getitem__)
# # print(res)
# # print(lookup)
# print(res)
import  collections

window = 'foobar'
words = ["foo","bar"]

dp = [False] * (len(window) + 1)
dp[0] = True
def check(window,words):
    for word in words:
        for i in range(len(window), len(word) - 1, -1):
            if window[i - len(word):i] == word:
                dp[i] |= dp[i - len(word)]
    print(dp)
    return dp[-1]

if __name__ == "__main__":
    print(check(window,words))



