var containsDuplicate = (nums) => {
    const numsSet = new Set(nums); //a set can contain only unique values
   return !(numsSet.size === nums.length); //return the opposite
};