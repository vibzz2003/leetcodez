class Solution {
    func countAndSay(_ n: Int) -> String {
        if n == 1 {
            return "1"
        }

        let previousTerm = countAndSay(n-1)
        var result: String = ""
        var count: Int = 0
        var currentChar: Character? = nil

        for char in previousTerm {
            if char == currentChar {
                count += 1
            } else {
                if let currentChar = currentChar {
                    result += "\(count)\(currentChar)"
                }
                currentChar = char
                count = 1
            }
        }

        if let currentChar = currentChar {
            result += "\(count)\(currentChar)"
        }

        return result
    }
}