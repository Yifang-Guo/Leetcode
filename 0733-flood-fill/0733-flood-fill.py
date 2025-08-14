class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        val = image[sr][sc]
        

        def dfs(r, c):
            if image[r][c] != val:
                return

            image[r][c] = color

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col and image[nr][nc] != color:
                    dfs(nr, nc)

        dfs(sr, sc)

        return image
