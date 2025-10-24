from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

def find_free_slots(intervals: List[List[int]], start: int, end: int) -> List[List[int]]:
    merged = merge_intervals(intervals)
    free_slots = []

    prev_end = start
    for interval in merged:
        if interval[0] > prev_end:
            free_slots.append([prev_end, interval[0]])
        prev_end = max(prev_end, interval[1])

    if prev_end < end:
        free_slots.append([prev_end, end])

    return free_slots

# Example usage
events = [[9, 10], [12, 13], [11, 12], [14, 15]]  # Meetings in 24h format
work_hours = [9, 18]

print("Merged events:", merge_intervals(events))
print("Free slots:", find_free_slots(events, work_hours[0], work_hours[1]))
