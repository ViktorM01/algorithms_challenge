func twoSum(nums []int, target int) []int {
	seen := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if idx, exists := seen[complement]; exists {
			return []int{idx, i}
		}
		seen[num] = i
	}
	return []int{}
}
