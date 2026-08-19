class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l=len(hand)
        s=groupSize
        if l%s!=0:
            return False
        hand.sort()
        h={}
        for i in hand:
            h[i]=h.get(i,0)+1
        for i in hand:
            if h[i]==0:
                continue
            for j in range(s):
                if h.get(i+j,0)==0:
                    return False
                h[i+j]-=1
        return True
                
        

            
                

                
                



        