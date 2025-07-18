from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[tuple]) -> int:
        if not intervals:
            return 0

        start, end = zip(*intervals)

        start = sorted(start)
        end = sorted(end)

        i, j, counter, result = 0, 0, 0, 0
        while i < len(start):
            if start[i] < end[j]:
                counter += 1
                result = max(result, counter)
                i += 1

            else:
                counter -= 1
                j += 1

        return result


s = Solution()

test_cases = [[(0, 40), (5, 10), (15, 20)], [(4, 9)]]

for test in test_cases:
    result = s.minMeetingRooms(test)
    print(result)
