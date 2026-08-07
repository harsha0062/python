from typing import List
from heapq import heappush, heappop

def scheduleCourse(courses: List[List[int]]) -> int:
    # Sort courses by their deadline
    courses.sort(key=lambda x: x[1])

    # Max-heap simulation using negative durations
    heap = []

    # Track the total time spent on selected courses
    max_time = 0

    # Process each course in deadline order
    for time, end_time in courses:
        # Store the duration as a negative value
        heappush(heap, -time)
        max_time += time

        # If the current schedule exceeds the deadline,
        # remove the longest course
        if max_time > end_time:
            big_time = heappop(heap)
            max_time += big_time

    # The number of courses remaining in the heap is the answer
    return len(heap)


# Input inside the code
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]

print(scheduleCourse(courses))