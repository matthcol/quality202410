import math

def distance(A: tuple[float,float] , B: tuple[float,float]) -> float:
    # return math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
    return math.hypot(B[0] - A[0], B[1] - A[1])