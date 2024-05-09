import Foundation

let n = Int(readLine()!)!

func divide(n: Int, nums: [Int]) {
    if n == 1 {
        nums.forEach { print($0) }
        return
    }
    
    var i = 2
    while !(n % i == 0) {
        if i > Int(sqrt(Double(n))) {
            nums.forEach { print($0) }
            print(n)
            return
        }
        i += 1
    }
    divide(n: n / i, nums: nums + [i])
}

divide(n: n, nums: [])