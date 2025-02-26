impl Solution {
    pub fn max_absolute_sum(nums: Vec<i32>) -> i32 {
        let (mut max_sum, mut min_sum, mut sum) = (0, 0, 0);
        for &el in &nums {
            sum += el;
            max_sum = max_sum.max(sum);
            min_sum = min_sum.min(sum);
        }
        max_sum - min_sum
    }
}
