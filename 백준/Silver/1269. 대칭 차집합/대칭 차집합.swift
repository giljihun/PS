import Foundation

let numAB = readLine()!.components(separatedBy: " ")
let numA = Int(numAB[0])!
let numB = Int(numAB[1])!

let A = readLine()!.components(separatedBy: " ")
let B = readLine()!.components(separatedBy: " ")

var setA = Set(A)
var setB = Set(B)

let commonElements = setA.intersection(setB)

let symmetricDifference = setA.symmetricDifference(setB)

print(symmetricDifference.count)
