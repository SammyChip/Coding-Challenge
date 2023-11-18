function twoSum(nums, target) {
    const numToIndex = new Map();
    for (let i = 0; i < nums.length; i++) {
        const comp = target - nums[i];
        if (numToIndex.has(comp)) {
            return [numToIndex.get(comp), i];
        }
        numToIndex.set(nums[i], i);
    }
}
//same idea with hasmaps in python dictionaries ~ maps