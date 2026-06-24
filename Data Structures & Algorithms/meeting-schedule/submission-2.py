"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 0:
            return True
        sorted_intervals = sorted(intervals, key=lambda a: a.start)
        last_end = sorted_intervals[0].end
        for meeting in sorted_intervals[1:]:
            if meeting.start < last_end:
                return False
            last_end = meeting.end
        return True
