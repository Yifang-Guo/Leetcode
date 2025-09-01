class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append([r, c])
                else:
                    mat[r][c] = -1

        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or mat[nr][nc] != -1:
                        continue
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append([nr, nc])

        return mat


        