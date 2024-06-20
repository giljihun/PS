import Foundation

let nums = readLine()!.components(separatedBy: " ")

var A = nums[0].map {String($0)}
var B = nums[1].map {String($0)}

var result: [String] = []

A = A.reversed()
B = B.reversed()

if A.count > B.count {
    
    var carry: Int = 0
    var endI: Int = 0
    
    for i in 0..<B.count {
        
        var sum: Int = 0
        let sumResult: [String]
        
        sum = Int(A[i])! + Int(B[i])! + carry
        
        if sum >= 10 {
            carry = 1
        } else {
            carry = 0
        }
        
        sumResult = String(sum).map {String($0)}
        
        
        if sumResult.count > 1 {
            result.append(sumResult[1])
        } else {
            result.append(sumResult[0])
        }
        endI = i
        
    }
    
    for j in endI + 1..<A.count {
        var sum: Int = 0
        let sumResult: [String]
        
        sum = Int(A[j])! + carry
        
        if sum >= 10 {
            carry = 1
        } else {
            carry = 0
        }
        
        sumResult = String(sum).map {String($0)}
        
        if j == A.count - 1 {
            result.append(sumResult.joined())
        } else {
            if sumResult.count > 1 {
                result.append(sumResult[1])
            } else {
                result.append(sumResult[0])
            }
        }
    }
}

else if A.count == B.count {
    
    var carry: Int = 0
    
    for i in 0..<A.count {
        
        var sum: Int = 0
        let sumResult: [String]
        
        sum = Int(A[i])! + Int(B[i])! + carry
        
        if sum >= 10 {
            carry = 1
        } else {
            carry = 0
        }
        
        sumResult = String(sum).map {String($0)}
        
        if i == A.count - 1 {
            result.append(sumResult.joined())
        } else {
            if sumResult.count > 1 {
                result.append(sumResult[1])
            } else {
                result.append(sumResult[0])
            }
        }
    }
} else {
    
    var carry: Int = 0
    var endI: Int = 0
    
    for i in 0..<A.count {
        
        var sum: Int = 0
        let sumResult: [String]
        
        sum = Int(A[i])! + Int(B[i])! + carry
        
        if sum >= 10 {
            carry = 1
        } else {
            carry = 0
        }
        
        sumResult = String(sum).map {String($0)}
        
        if sumResult.count > 1 {
            result.append(sumResult[1])
        } else {
            result.append(sumResult[0])
        }
        endI = i
        
    }
    
    for j in endI + 1..<B.count {
        var sum: Int = 0
        let sumResult: [String]
        
        sum = Int(B[j])! + carry
        
        if sum >= 10 {
            carry = 1
        } else {
            carry = 0
        }
        
        sumResult = String(sum).map {String($0)}
        
        if j == B.count - 1 {
            result.append(sumResult.joined())
        } else {
            if sumResult.count > 1 {
                result.append(sumResult[1])
            } else {
                result.append(sumResult[0])
            }
        }
    }
}

result = result.reversed()
let answer = result.joined()
print(answer)
