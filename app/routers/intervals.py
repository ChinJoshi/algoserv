from fastapi import APIRouter

router = APIRouter()



@router.post("/non-overlapping-intervals")
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        """
        intuition:

        Say the intervals are monotonically increasing by start of the interval
        If we go greedily, each time we encounter an interval, we can check if it's start is less than a previously encountered interval start
        This would give us some number of eliminations, but would it be the minimum?

        Say we have two intervals that overlap only each other:
        in that case we can say that it doesn't matter which interval you eliminate, either elimination results in one elimination

        Say we have more than two intervals that overlap only each other:
        [1,6],[4,8],[5,7],[5,9],[6,10],[10,20]
        We want to eliminate the interval which overlaps with the most other intervals
        Is there a case where the most overlapping interval would rather not be eliminated
        Say we left it around, then that would mean, every other interval that it overlaps with would have to be removed, since they all overlap with it. 
        Since 1 < # of overlapping intervals (since we have more than two intervals that overlap only each other), then yeah it stands to reason that w must always remove the most overlapping interval out of this group

        So in this example:
        [1,6] -> 3 overlaps
        [4,8] -> 4 overlaps
        [5,7] -> 4 overlaps
        [5,9] -> 4 overlaps
        [6,10] -> 3 overlaps
        [10,20] -> 0 overlaps

        So no matter what, when you have an interval that has the most overlaps , that is the one to eliminate, since if you don't eliminate it, you're gonna have to end up eliminating every interval that it overlapped with

        I don't think we actually need to sort it
        We'll start by iterating over the intervals, and putting them into a dict witha tuple of the interval as the key, and the set of intervals it overlaps as the value

        That operation would be O(n^2)

        O(N) to find the one with the max intervals
        Keep going until the set of intervals overlapping in every value is empty

        That'll be O(N^2) since we can at most remove N intervals and each removal could take up to N time since it could overlap with every other interval theoretically

        Overall we still have an O(N^2)
        Each time we do a removal, increment a counter
        Return the counter at the end


        Turns out this doesn't work for all testcases, because although we are greedily taking the most overlapped, it's a local greedy, not a global greedy. The greedy sample is just of the set of intervals that overlap with the most overlapped interval.
        The actual way to do this would be to:
        sort by ending value
        iterate over the sorted intervals, if you encounter an overlap between two intervals, remove the one which has the greater ending value, since that is the one that is more likely to overlap with the succeeding intervals
        This will be O(N*log(N)) for the sort
        O(N) for the removals
        Overall: O(N*Log(N))
        """

        removal_count = 0
        intervals.sort(key=lambda x: x[1])
        prev_interval_pointer = 0
        current_interval_pointer = 1
        while current_interval_pointer < len(intervals):
            if intervals[current_interval_pointer][0] < intervals[prev_interval_pointer][1]:
                removal_count += 1
                current_interval_pointer += 1
            else:
                prev_interval_pointer = current_interval_pointer
                current_interval_pointer += 1
        return removal_count        


        # # start with our overlap construction
        # removal_count = 0
        # # key is interval, value is set of intervals it overlaps with
        # overlaps = {}
        # for interval in intervals:
        #     if (interval[0],interval[1]) not in overlaps:
        #         overlaps[(interval[0],interval[1])] = set()
        #         for key in overlaps.keys():
        #             # if overlapping
        #             # if (interval[0] < key[1] and interval[0] > key[0]) or (interval[1] > key[0] and interval[1] < key[1]) or (interval[0] > key[0] and interval[1] < key[1]):
        #             if (not (interval[0] >= key[1] or interval[1] <= key[0])) and key != (interval[0],interval[1]):
        #                 overlaps[(interval[0],interval[1])].add(key)
        #                 overlaps[key].add((interval[0],interval[1]))
        #     else:
        #         # this case is if we have identical intervals, someof them have to be removed, unfortunately, it's gonna be the later ones
        #         removal_count +=1
        
        # # we could theoretically could have used a max heap to know which interval to eliminate next more efficiently, but in the overall running time of things, our algo would still be O(N^2) anyways
        # while True:
        #     # find the one with the max length
        #     max_overlaps_interval = None
        #     max_len = 0
        #     for interval in overlaps.keys():
        #         if len(overlaps[interval]) > max_len:
        #             max_overlaps_interval = interval
        #             max_len = len(overlaps[interval])
        #     if max_len == 0:
        #         break
        #     # print(f'overlaps: {overlaps}')
        #     # print(f'max_overlaps_interval: {max_overlaps_interval}')
        #     for interval in overlaps[max_overlaps_interval]:
        #         # print(f'overlapping_interval: {interval}')
        #         overlaps[interval].remove(max_overlaps_interval)
        #     overlaps.pop(max_overlaps_interval)
        #     removal_count += 1

        # return removal_count