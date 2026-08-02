class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        r = len(board)
        c = len(board[0])

        used = [[False] * c for _ in range(r)]

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def backtrack(i,j,start):

            if i < 0 or i >= r or j < 0 or j >= c:
                return False

            if used[i][j]:
                return False

            if board[i][j] != word[start]:
                return False

            # matched the last character
            if start == len(word)-1:
                return True

            used[i][j] = True

            for di,dj in directions:

                ni = i + di
                nj = j + dj

                if backtrack(ni,nj,start+1):
                    return True

            used[i][j] = False

            return False

        for i in range(r):
            for j in range(c):

                if backtrack(i,j,0):
                    return True

        return False