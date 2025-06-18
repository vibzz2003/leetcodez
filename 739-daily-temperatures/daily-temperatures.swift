class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        let n = temperatures.count
        var result = Array(repeating: 0, count: n)
        var stack: [Int] = [] // store indices

        for i in 0..<n {
            // While current temp is greater than temperature at top index in stack
            while let last = stack.last, temperatures[i] > temperatures[last] {
                let prevIndex = stack.removeLast()
                result[prevIndex] = i - prevIndex
            }
            stack.append(i)
        }

        return result
    }
}