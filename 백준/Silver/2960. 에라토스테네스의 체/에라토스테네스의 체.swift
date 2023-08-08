import Foundation

let N = readLine()!.split(separator: " ").map {
    Int(String($0))! }

//func isPrime(n: Int) -> Bool {
//    if (n<4) {
//        return n == 1 ? false : true
//    }
//
//    for i in 2...Int(sqrt(Double(n))) {
//        if (n % i == 0) {
//            return false
//        }
//    }
//    return true
//}
    
func sieveOfEratosthenes(n: Int) -> Void {
    var arr = Array(repeating: true, count: n+1)
    var cnt = 0
    
    for i in 2..<n+1 {
        for j in stride(from: i, to: n+1, by: i) {
            if arr[j] {
                arr[j] = false
                cnt += 1
                if cnt == N[1] {
                    print(j)
                    break
                }
            }
        }
    }
    return
}

sieveOfEratosthenes(n: N[0])

