//
//  main.swift
//  PS_swift
//
//  Created by mobicom on 4/30/24.
//

import Foundation

while(true) {
    var nums: [Int] = []
    
    if let input = readLine() {
        if input == "-1" {
            break
        } else if let n = Int(input) {
            for i in 1...n-1 {
                if n % i == 0 {
                    nums.append(i)
                }
            }
            
            var sum: Int = 0
            
            for num in nums {
                sum += num
            }
            
            if sum == n {
                
                print("\(n) = ", terminator: "") // 개행 없애기
                for i in 0...nums.count-1 {
                    print(nums[i], terminator: "") // 요소 출력하고 개행 없애기
                    if i != nums.count - 1 {
                        print(" + ", terminator: "") // 마지막 요소가 아니면 + 추가
                    }
                }
                print()
            }
            else {
                print("\(n) is NOT perfect.")
            }
        }
    } else {
        break
    }
}
