from typing import List


class Meeting:
    def __init__(self, start, end, position) -> None:
        self.start = start
        self.end = end
        self.position = position


class Solution:

    def maximumMeetings(self, start: List[int], end: List[int]) -> int:
        count = 1
        n = len(start)
        meet: List["Meeting"] = [Meeting(start[i], end[i], i + 1) for i in range(n)]
        meet.sort(key=lambda x: (x.end, x.start))
        last_meeting = meet[0].end
        for i in range(1, n):
            if meet[i].start > last_meeting:
                count += 1
                last_meeting = meet[i].end
        return count


s = Solution()
print(s.maximumMeetings(start=[1, 3, 0, 5, 8, 5], end=[2, 4, 6, 7, 9, 9]))
