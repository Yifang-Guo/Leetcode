class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(minHeap, (distance, point[0], point[1]))

        res = []
        while k > 0:
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res


        
        