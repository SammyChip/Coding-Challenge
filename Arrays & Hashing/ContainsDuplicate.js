var containsDuplicate = (nums) => {
    const numsSet = new Set(nums); //a set can contain only unique values
    const equalCheck = numsSet.size === nums.length;

    return !equalCheck;
};