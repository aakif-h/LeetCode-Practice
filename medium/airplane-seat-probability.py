class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # assuming that we have more than 1 person to consider, we have two scenarios:
        # the first scenario is that some person 1 to n-1 sits in person n's seat randomly
        # the second scenario is that some person 2 to n-1 sits in person 1's seat, ending 
        # the seat-stealing cycle; therefore, person n does not need to find another seat.
        # as both events are weighted equally, the probability is ALWAYS 1/2
        if n == 1:
            return 1
        else:
            return 0.5
        
