//
//  boj3273.swift
//  PS
//
//  Created by 길지훈 on 2023/01/08.
//

import Foundation

let a = Int(readLine()!)
let n = a! //수열의 크기

let input = readLine()!.split(separator: " ").map { Int(String($0))! }

let b = Int(readLine()!)
let x = b! // 만들기 원하는 자연수 x

let arr = input.sorted(by: <)

var start = 0
var end = n - 1
var cnt = 0

while start < end {
    
    let sum = arr[start] + arr[end]
    
    if sum == x {
        cnt += 1
        start += 1
        end -= 1
    }
    else if sum > x {
        end -= 1
    }
    else {
        start += 1
    }
}

print(cnt)
