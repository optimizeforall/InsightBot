#!/usr/bin/env python

import openai
import argparse
import os
import pyperclip  # This is for copying to clipboard

# Set up the argument parser
parser = argparse.ArgumentParser(description='Generate insights on a file.')
parser.add_argument('filename', type=str, help='The name of the file to generate insights on.')
parser.add_argument('-i', '--insight', action='store_true', help='Generate insights on the file.')
parser.add_argument('-r', '--review', action='store_true', help='Review the file for improvements.')
parser.add_argument('-c', '--clipboard', action='store_true', help='Copy the output to clipboard.')

# Parse the arguments
args = parser.parse_args()

# Read the file
with open(args.filename, 'r') as file:
    file_contents = file.read()

# Set prompt1 = prompt1.txt, so on and so forth
with open('prompt1.txt', 'r') as file:
    prompt1 = file.read() + '\n\n' + file_contents
  



prompt1 = """The following is a file, Summarize the key isnights to generat the optimal solution 
to this problem found in this code. I am interested about 1 sentence to remember what it was that 
allowed the solution to be clear, such as "use hash map", "use two pointers, find max by...",
thank your\n\n""" + file_contents;

prompt2 = """I'd appreciate if you conducted a thorough analysis of this code, pointing out 
areas that can be improved, whether for efficiency, readability, or compliance with best practices.
if there are any bugs or errors point those out too. Recommend any possible enhancements or refactoring
for better performance and maintainability. At the end, write out updated version, followed by all 
changes made. Thank you.\n\n""" + file_contents;

# Set up the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Generate insights using GPT-3.5
if args.insight:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt1,
      temperature=0.5,
      max_tokens=800,
    )
    output = response.choices[0].text.strip()
    print(output)
    if args.clipboard:
        pyperclip.copy(output)

# Conduct a review
if args.review:
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt2,
      temperature=0.5,
      max_tokens=800,
    )
    output = response.choices[0].text.strip()
    print(output)
    if args.clipboard:
        pyperclip.copy(output)

