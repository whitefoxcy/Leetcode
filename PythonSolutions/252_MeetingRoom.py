"""
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
"""

class Solution(object):
    def canAttendMeetings(self, intervals):
        if len(intervals) <= 1:
           return True
    
        intervals.sort(key = lambda x: x[0])

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

intervals = [[7,10], [2,4], [1,3]]
tmp =  Solution()  
print(tmp.canAttendMeetings(intervals))