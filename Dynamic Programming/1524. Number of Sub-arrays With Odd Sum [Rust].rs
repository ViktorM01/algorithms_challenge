impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        let mut cnt: i64 = 0;
        let mut pref_sum: i64 = 0;
        let mod_val: i64 = 1_000_000_007;
        
        for &num in &arr {
            pref_sum += num as i64;
            if pref_sum % 2 != 0 {
                cnt += 1;
            }
        }
        
        let len = arr.len() as i64;
        cnt = (cnt * (len - cnt) + cnt) % mod_val;
        
        cnt as i32
    }
}
