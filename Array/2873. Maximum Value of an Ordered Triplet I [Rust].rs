impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut ans: i64 = 0;
        let mut max_dif: i32 = 0;
        let mut max_val: i32 = 0;

        for &k in &nums {
            ans = ans.max((k as i64) * (max_dif as i64));
            max_dif = max_dif.max(max_val - k);
            max_val = max_val.max(k);
        }
        ans        
    }
}
