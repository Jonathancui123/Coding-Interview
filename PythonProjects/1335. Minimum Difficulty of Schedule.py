class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        return self.minDifficultyHelper(0, jobDifficulty, d)
    
    def minDifficultyHelper(self, nextJob, jobDifficulty, daysLeft):
        # Returns the minimum sum of difficulties over the number of days left
        
        #Base case - an invalid decision has been made:
        jobsLeft = len(jobDifficulty) - nextJob
        if (daysLeft > jobsLeft or (daysLeft == 0 and jobsLeft > 0)):
            return -1
        
        if (daysLeft == 0):
            return 0
        
        difficulties = []
        # Try doing all different numbers of jobs on this day
        for i in range(1, jobsLeft + 1):
            todayDifficulty = max(jobDifficulty[nextJob:(nextJob+i)])
            remainingDifficulty = self.minDifficultyHelper(nextJob + i, jobDifficulty, daysLeft - 1)
            if (remainingDifficulty >= 0):
                difficulties.append(todayDifficulty + remainingDifficulty)
        
        if len(difficulties) == 0:
            return -1
        else:
            return min(difficulties)
        
        # Handle the case where we get -1