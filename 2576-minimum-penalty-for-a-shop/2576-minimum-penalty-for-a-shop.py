class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        yarr = [0 for i in range(len(customers)+1)]
        narr = [0 for i in range(len(customers)+1)]
    
        for i in range(1, len(customers)+1):
            if customers[i-1] == 'N':
                narr[i] = narr[i-1] + 1
            else:
                narr[i] = narr[i-1]
        
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == 'Y':
                yarr[i] = yarr[i+1] + 1
            else:
                yarr[i] = yarr[i+1]
                
        print(yarr, narr)
        
         
        m = float('inf')
        index = -1
        for i in range(len(customers)+1):
            if narr[i] + yarr[i] < m:
                m = narr[i] + yarr[i]
                index = i
        return index