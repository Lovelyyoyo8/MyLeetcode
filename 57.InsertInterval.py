class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0
    # 将所有起始位置小于待插入区间的区间直接添加到结果列表中
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
    
    # 开始合并区间
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
    
    # 将合并后的区间加入结果列表
        result.append(newInterval)
    
    # 将剩余的区间加入结果列表
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result
