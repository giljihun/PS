//  main.swift
//  PS
//
//  Created by 길지훈 on 2023/01/01.
//

import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let rule: [Int] = [1, 1, 2, 2, 2, 8]
let length = rule.count
var result: [Int] = []

for i in (0...length - 1) {
    result.append((rule[i]) - (input[i]))
}

for i in 0...result.count - 1 {
    print(result[i], terminator:" ")
}


// * 1 1 2 2 2 8 *

// 0 1 2 2 2 7 -> 1 0 0 0 0 1
// 2 1 2 1 2 1 -> -1 0 0 1 0 7

// -> 1 1 2 2 8 에서 각 인덱스 번호 숫자를 빼면 된다.
