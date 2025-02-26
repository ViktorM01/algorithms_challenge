func maxAbsoluteSum(nums []int) int {
	maxSum, minSum, sum := 0, 0, 0
	for _, el := range nums {
		sum += el
		maxSum = int(math.Max(float64(maxSum), float64(sum)))
		minSum = int(math.Min(float64(minSum), float64(sum)))
	}
	return maxSum - minSum
}
