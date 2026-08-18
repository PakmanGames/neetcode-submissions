class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let array = []
        for (let i = 0; i < nums.length; i++) {
            if (array.some(item => item == nums[i])) {
                return true
            }
            array.push(nums[i])
        }
        return false
    }
}
