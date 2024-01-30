"""
A player's moves will never impact the moves for the other player.
Thus all the moves a player can make are already available at the start of the game.
In AAAABBBAABBBBBAAA, Alice has 3 moves and Bob has 4 moves.
Alice needs 1 extra move than Bob to win since she goes first.
So if both have 1 move each, Alice goes first, then bob and then alice cannot move and loses.
Thus is Alice > Bob, then she wins, else bob wins.

O(n) time to get counts of both alice and bob.
O(1) space.
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice = 0
        bob = 0

        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice += 1
                else:
                    bob += 1
        
        if alice > bob:
            return True
        else:
            return False
