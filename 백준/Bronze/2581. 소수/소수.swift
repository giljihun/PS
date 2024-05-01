//
//  main.swift
//  PS_swift
//
//  Created by mobicom on 4/30/24.
//

import Foundation

var sum: Int = 0
var min: Int = 10001
var none: Bool = true

let M = Int(readLine()!)!
let N = Int(readLine()!)!

func isPrime(target : Int) -> Bool {

    if target <= 1 { return false }
    if target <= 3 { return true }
    
    for i in 2...(target-1) {
        if target % i == 0 {
            return false
        }
    }
    
    return true
}

for i in M...N {
    if isPrime(target: i) {
        none = false
        sum += i
        if min > i {
            min = i
        }
    }
}

if none == false {
    print(sum)
    print(min)
} else { print("-1") }

