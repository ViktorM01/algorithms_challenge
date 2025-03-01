func applyOperations(nums []int) []int {
    n := len(nums)
    for i := 0; i < n - 1; i++ {
        if nums[i] == nums[i + 1] {
            nums[i] *= 2
            nums[i + 1] = 0
        }
    }
    l := 0
    for r := 0; r < n; r++ {
        if nums[r] != 0 {
            nums[l], nums[r] = nums[r], nums[l]
            l++
        }
    }
    return nums
}
