func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	ans := [][]int{}
	p1, p2 := 0, 0

	for p1 < len(nums1) || p2 < len(nums2) {
		if p1 < len(nums1) && p2 < len(nums2) {
			if nums1[p1][0] == nums2[p2][0] {
				ans = append(ans, []int{nums1[p1][0], nums1[p1][1] + nums2[p2][1]})
				p1++
				p2++
			} else if nums1[p1][0] < nums2[p2][0] {
				ans = append(ans, []int{nums1[p1][0], nums1[p1][1]})
				p1++
			} else {
				ans = append(ans, []int{nums2[p2][0], nums2[p2][1]})
				p2++
			}
		} else if p1 < len(nums1) {
			ans = append(ans, []int{nums1[p1][0], nums1[p1][1]})
			p1++
		} else if p2 < len(nums2) {
			ans = append(ans, []int{nums2[p2][0], nums2[p2][1]})
			p2++
		}
	}

	return ans
}
