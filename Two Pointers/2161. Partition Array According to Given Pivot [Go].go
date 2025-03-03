func pivotArray(nums []int, pivot int) []int {
    var lst1, lst2, lst3 []int 
  
    for _, el := range nums {
        if el < pivot {
            lst1 = append(lst1, el) 
        } else if el == pivot {
            lst2 = append(lst2, el)
        } else {
            lst3 = append(lst3, el)
        }
    }

    result := append(lst1, lst2...)
    result = append(result, lst3...)

    return result
}
