class Solution {
    func combinationSum2(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var result: [[Int]] = []
        var combination: [Int] = []
        let sortedCandidates = candidates.sorted() // Sorting helps in avoiding duplicates

        func backtrack(_ start: Int, _ remaining: Int) {
            if remaining == 0 {
                result.append(combination)
                return
            }

            for i in start..<sortedCandidates.count {
                // Skip duplicates
                if i > start && sortedCandidates[i] == sortedCandidates[i - 1] {
                    continue
                }

                let num = sortedCandidates[i]
                if num > remaining {
                    break
                }

                combination.append(num)
                backtrack(i + 1, remaining - num) // Move to the next number
                combination.removeLast() // Backtrack
            }
        }

        backtrack(0, target)
        return result
    }
}
