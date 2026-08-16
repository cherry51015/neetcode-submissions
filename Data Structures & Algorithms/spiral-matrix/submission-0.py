class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        lt=0
        rt=len(matrix[0])
        top=0
        bot=len(matrix)
        while lt<rt and top<bot:
            for i in range(lt,rt):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,bot):
                res.append(matrix[i][rt-1])
            rt-=1
            if not (lt<rt and top<bot):
                break
            for i in range(rt-1,lt-1,-1):
                res.append(matrix[bot-1][i])
            bot-=1
            for i in range(bot-1,top-1,-1):
                res.append(matrix[i][lt])
            lt+=1
        return res

        