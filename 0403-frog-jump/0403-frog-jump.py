class Solution:
    def canCross(self, stones: List[int]) -> bool:
        graph = {}
        for i in stones:
            graph[i] = set()
        graph[0].add(1)
        print(graph)
        for i in range(len(stones)):
            currStone = stones[i]
            currStoneSet = graph[currStone]
            for currPos in currStoneSet:
                newPos = currStone+currPos
                if newPos == stones[-1]:
                    return True
                if newPos in graph:
                    graph[newPos].add(currPos)
                    graph[newPos].add(currPos+1)
                    if(currPos>1):
                        graph[newPos].add(currPos-1)

        print(graph)

            