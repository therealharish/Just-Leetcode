class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        bucketsort = defaultdict(list)
        results = {}
        for val in words: 
            bucketsort[len(val)].append(val)
            results[val] = 1
        for i in reversed(range(1,17)):#from 16 to 1 (bucket sort bounds)
            for val in bucketsort[i]:#for each value in the bucket that we are in 
                for i in range(len(val)):
                    predecessor = val[:i] + val[i+1:]#all the combinations of values that we can make by deleting a char
                    if predecessor in results: #if we have this value somewhere 
                        results[predecessor] = max(results[predecessor],results[val]+1)
        return max(results.values())