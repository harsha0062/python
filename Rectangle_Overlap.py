from typing import List

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    # Unpack the coordinates of the first rectangle
    r1x1, r1y1, r1x2, r1y2 = rec1

    # Unpack the coordinates of the second rectangle
    r2x1, r2y1, r2x2, r2y2 = rec2

    # Rectangles overlap only if:
    # 1. Their horizontal intervals overlap with positive width
    # 2. Their vertical intervals overlap with positive height
    return (
        max(r1x1, r2x1) < min(r1x2, r2x2)
        and
        max(r1y1, r2y1) < min(r1y2, r2y2)
    )


# Input inside the code
rec1 = [0, 0, 2, 2]
rec2 = [1, 1, 3, 3]

print(isRectangleOverlap(rec1, rec2))