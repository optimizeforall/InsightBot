# Insight Bot

Insight Bot is a Python-based command line application that uses OpenAI's GPT-3.5 to generate insights on the contents of a given file. The bot can also review the contents of a file for improvements. It can be used to analyze text and generate meaningful insights or suggestions.

## Example
See: [two_sum.py](Example/two_sum.py)

![Alt text](image.png)


```
**Command: ibot -r two_sum.py**

Output: 

Analysis: 
This code is attempting to solve the two sum problem, which is to find two numbers in an array which sum up to a target number. The code is using a hashmap to store the numbers in the array and its index. 

Areas that can be improved for efficiency, readability, or compliance with best practices: 
1. The class name is misspelled as "Soltution", it should be "Solution".
2. The main function should be outside the class.
3. The code can be improved for readability by adding comments to explain what the code is doing.
4. The code should check for edge cases, such as an empty array or a target number that cannot be achieved with the given array.

Bugs: 
1. The code is not checking if there are duplicate numbers in the array, which could lead to incorrect results.

Recommendations to reduce time and/or space complexity:
1. Instead of using a hashmap, the code can use two pointers to traverse the array and check if the sum of two elements is equal to the target. This will reduce the time complexity from O(n) to O(nlog(n))

Updated Optimized Version: 

class Solution {
  List<int> twoSum(List<int> nums, int target) {
    // Edge case: return empty list if array is empty
    if (nums.length == 0) {
      return [];
    }

    // Edge case: return empty list if target cannot be achieved with given array
    int maxSum = nums[0] + nums[1];
    for (int i = 2; i < nums.length; i++) {
      maxSum = max(maxSum, nums[i - 1] + nums[i]);
    }
    if (target > maxSum) {
      return [];
    }

    int i = 0;
    int j = nums.length - 1;
    while (i < j) {
      int sum = nums[i] + nums[j];
      if (sum == target) {
        return [i, j];
      } else if (sum < target) {
        i++;
      } else {
        j--;
      }
    }

    return [];
  }
}

void main() {
  Solution s = Solution();
  print(s.twoSum([2, 7, 11, 15], 9));
}

Changes Made: 
1. Fixed the class name from "Soltution" to "Solution".
2. Moved the main function outside the class.
3. Added comments to explain what the code is doing.
4. Added edge case checks to return an empty list if the array is empty or the target cannot be achieved with the given array.
5. Replaced the hashmap with two pointers to traverse the array and reduce the time complexity from O(n) to O(nlog(n)).
```

## Dependencies

- Python 3, openai, argparse, os, pyperclip

## Installation

1. Clone this repository.

```sh
git clone https://github.com/optimizeforall/InsightBot.git
```

2. Change into the directory.

```sh
cd InsightBot
```

3. Install the necessary Python packages.

```sh
pip install -r openai pyperclip
```

4. Set your OpenAI API key in your environment variables.

```sh
export OPENAI_API_KEY='your-openai-api-key'
```

If you don't have an OpenAI API key, you can get one create one [here](https://platform.openai.com/account/api-keys).

5. Make bot accessible from anywhere.

```sh
chmod +x insight_bot.py
ln -s /path/to/insight_bot.py /usr/local/bin/ibot
```

I recommend using `ibot` as the command name, but you can use whatever you want.


## Usage

Insight Bot provides a command line interface with several options.

To generate insights on a file:

```sh
python ibot filename -i
```

To review a file and suggest imporovements:

```sh
python ibot filename -r
```

To copy the output to your clipboard:

```sh
python ibot filename -i -c
```

```sh
python ibot filename -r -c
```

Replace `filename` with thzse name of the file you want to process.

## Notes

The OpenAI API key should be kept secret. Do not include it in your scripts or upload it to public repositories.

The prompts used by the bot are stored in `prompt1.txt` and `prompt2.txt`. You can modify these files to change the prompts used for generating insights and conducting reviews.

The maximum number of tokens that can be generated in a single call to the OpenAI API is 2048. Adjust the `max_tokens` parameter as needed.

## License

This project is licensed under the terms of the MIT license.