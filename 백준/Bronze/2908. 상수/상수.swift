//
//  main.swift
//  PS
//
//  Created by 길지훈 on 2023/01/01.
//

import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let a = Int(input[0]) // 734
let b = Int(input[1]) // 893
var c = 0
var d = 0
var e:[String] = []
var f:[String] = []


for i in 1...3 {
    let level: Double = Double(i)
    c = (a % Int(pow(10.0, level))) / Int(pow(10.0, level - 1))
    e.append(String(c))
}

for i in 1...3 {
    let level: Double = Double(i)
    d = (b % Int(pow(10.0, level))) / Int(pow(10.0, level - 1))
    f.append(String(d))
}


let result_a = Int(e[0] + e[1] + e[2])!
let result_b = Int(f[0] + f[1] + f[2])!

if result_a > result_b {
    print(result_a)
}
else {print(result_b)}
