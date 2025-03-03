impl Solution {
    pub fn pivot_array(nums: Vec<i32>, pivot: i32) -> Vec<i32> {
        let mut lst1 = Vec::new();
        let mut lst2 = Vec::new();
        let mut lst3 = Vec::new();

        for el in nums {
            if el < pivot {
                lst1.push(el);
            } else if el == pivot {
                lst2.push(el);
            } else {
                lst3.push(el);
            }
        }

        lst1.extend(lst2);
        lst1.extend(lst3);

        lst1
    }
}
