impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut ans: Vec<Vec<i32>> = Vec::new();
        let (mut p1, mut p2) = (0, 0);

        while p1 < nums1.len() || p2 < nums2.len() {
            if p1 < nums1.len() && p2 < nums2.len() {
                if nums1[p1][0] == nums2[p2][0] {
                    ans.push(vec![nums1[p1][0], nums1[p1][1] + nums2[p2][1]]);
                    p1 += 1;
                    p2 += 1;
                } else if nums1[p1][0] < nums2[p2][0] {
                    ans.push(vec![nums1[p1][0], nums1[p1][1]]);
                    p1 += 1;
                } else {
                    ans.push(vec![nums2[p2][0], nums2[p2][1]]);
                    p2 += 1;
                }
            } else if p1 < nums1.len() {
                ans.push(vec![nums1[p1][0], nums1[p1][1]]);
                p1 += 1;
            } else if p2 < nums2.len() {
                ans.push(vec![nums2[p2][0], nums2[p2][1]]);
                p2 += 1;
            }
        }

        ans
    }
}
