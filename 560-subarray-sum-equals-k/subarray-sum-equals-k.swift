class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var sum: Int = 0
        var count: Int = 0
        var prefixSum: [Int: Int] = [0: 1]

        for num in nums {
            sum += num
            if let already: Int = prefixSum[sum - k] {
                count += already
            }

            prefixSum[sum, default: 0] += 1
        }
        return count
    }
}