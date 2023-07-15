# Insight Bot

Insight Bot is a Python-based command line application that uses OpenAI's GPT-3.5 to generate insights on the contents of a given file. The bot can also review the contents of a file for improvements. It can be used to analyze text and generate meaningful insights or suggestions.

## Example
    
```sh  
ibot two_sum.py -i
```
Output:
```

Analysis: 
This code is attempting to find the indices of two numbers in a list that add up to a target value. 

Areas that can be improved: 
1. Efficiency: This code has a time complexity of O(n^2) because it is using nested for loops. 
2. Readability: This code could be made more readable by adding more descriptive variable names and comments.
3. Compliance with best practices: The code does not have any major issues with best practices.

Bugs:
No bugs have been identified.

Recommendations to reduce time and/or space complexity:
1. Use a hash table to store the elements in the list. This will reduce the time complexity from O(n^2) to O(n). 

Updated optimized version:
def two_sum(nums, target):
    # Create a dictionary to store the elements in the list
    nums_dict = {}
    
    # Loop through the list and store the elements in the dictionary
    for i, num in enumerate(nums):
        nums_dict[num] = i
        
    # Loop through the list again and check if the difference between the target and current element is in the dictionary
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_dict and nums_dict[diff] != i:
            return [i, nums_dict[diff]]
            
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)

Changes made:
1. Added a dictionary to store the elements in the list.
2. Added a loop to store the elements in the dictionary.
3. Added a loop to check if the difference between the target and current element is in the dictionary.
4. Added more descriptive variable names and comments.
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

- To generate insights on a file:

```sh
python ibot filename -i
```

- To review a file and suggest imporovements:

```sh
python ibot filename -r
```

- To copy the output to your clipboard:

```sh
python ibot filename -i -c
```

```sh
python ibot filename -r -c
```

Replace `filename` with the name of the file you want to process.

## Notes

The OpenAI API key should be kept secret. Do not include it in your scripts or upload it to public repositories.

The prompts used by the bot are stored in `prompt1.txt` and `prompt2.txt`. You can modify these files to change the prompts used for generating insights and conducting reviews.

The maximum number of tokens that can be generated in a single call to the OpenAI API is 2048. Adjust the `max_tokens` parameter as needed.

## License

This project is licensed under the terms of the MIT license.