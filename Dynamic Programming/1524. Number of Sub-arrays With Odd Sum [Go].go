func numOfSubarrays(arr []int) int {
    cnt, prefSum, mod := 0, 0, 1000000007
    for _, num := range arr {
        prefSum += num
        if prefSum%2 != 0 {
            cnt++
        }
    }
    cnt += (len(arr) - cnt) * cnt
    return cnt % mod
}
