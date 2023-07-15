List<int> twoSum(List<int> nums, int target) {
  Map<int, int> set = {};

  for (int i = 0; i < nums.length; i++) {
    // if in set
    if (set.containsKey(target - nums[i])) {
      return [i, set[target - nums[i]]!];
    }
    set[nums[i]] = i;
  }

  return [0, 0];
}

void main() {
  print(twoSum([2, 7, 11, 15], 9));
}
