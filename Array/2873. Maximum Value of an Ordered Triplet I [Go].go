func maximumTripletValue(nums []int) int64 {
    var ans, maxDif, maxVal int64 = 0, 0, 0

    for _, k := range nums {
        k64 := int64(k)
        if k64 * maxDif > ans {
            ans = k64 * maxDif
        }
        if maxVal - k64 > maxDif {
            maxDif = maxVal - k64
        }
        if k64 > maxVal {
            maxVal = k64
        }
    }
    return ans
}
