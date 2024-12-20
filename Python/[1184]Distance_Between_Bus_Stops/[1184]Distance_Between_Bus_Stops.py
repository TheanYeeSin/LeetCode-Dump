# Your Python code goes here.
class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        path = 0
        total = sum(distance)
        index = start
        if start > destination:
            while True:
                if index == len(distance):
                    index = 0
                if index == destination:
                    break
                path += distance[index]
                index += 1
        else:
            for i in range(start, destination):
                path += distance[i]

        return min(total - path, path)
