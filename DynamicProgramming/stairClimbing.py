# You are climbing a staircase and it takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    def stairClimbing(self, n:int) ->int:
        oneStep,twoStep = 1,1;
        for i in range(n-1):
            temp = oneStep;
            oneStep += twoStep;
            twoStep = temp;
        return oneStep;


ob =  Solution();

print(ob.stairClimbing(3));
print(ob.stairClimbing(-1));
print(ob.stairClimbing(6));
