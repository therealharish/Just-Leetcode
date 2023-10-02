class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        alice = bob = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] == colors[i + 1] == 'A':
                alice += 1
            elif colors[i-1] == colors[i] == colors[i + 1] == 'B':
                bob += 1
        
        print(alice, bob)
        
        if alice == bob:
            return False
        elif alice > bob:
            return True
        else:
            return False
             
        