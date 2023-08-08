while let n = readLine() { //1번

    var count = 0 //자릿수를 세기위한 변수
    var next = 1 //1, 11, 111, ... 을 하기위한 변수이다.
    
    while true {
        count += 1
        if next % Int(n)! == 0 { //2번
            print("\(count)")
            break
        }else {
            next = ((next * 10) + 1)
            next %= Int(n)!
        }
        
    }
}