class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        d = defaultdict(list)
        for i in range(len(groupSizes)):
            # print(d)
            size = groupSizes[i]
            if size in d:
                j = d[size][-1]
                if len(j)<size:
                    j.append(i)
                else:
                    d[size].append([i])
            else:
                d[size].append([i])
        ans = []
        for x, y in d.items():
            if len(y) == 1:
                ans.append(y[0])
            else:
                for j in range(len(y)):
                    ans.append(y[j])
        return ans


