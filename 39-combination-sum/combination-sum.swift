class Solution {
    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        var result: [[Int]] = []
        
        func backtrack(_ combination: inout [Int], _ remaining: Int, _ start: Int) {
            if remaining == 0 {
                result.append(combination)
                return
            }
            
            for i in start..<candidates.count {
                let num = candidates[i]
                if remaining - num < 0 {
                    continue
                }
                combination.append(num)
                backtrack(&combination, remaining - num, i) 
                combination.removeLast() 
            }
        }
        
        var combination: [Int] = []
        backtrack(&combination, target, 0)
        return result
    }
}
