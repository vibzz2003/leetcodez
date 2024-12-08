class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1) 

        for i in range(n - 1, -1, -1):
            points, skip = questions[i]
            next_question = i + skip + 1
            dp[i] = max(points + (dp[next_question] if next_question < n else 0), dp[i + 1])

        return dp[0]