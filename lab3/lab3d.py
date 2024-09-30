#!/usr/bin/env python3

# Author ID: bmsubba

import subprocess

# free_space() function definition
def free_space():
    # Run the df command to get the free space of the root directory
    command = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout, _ = process.communicate()
    # Decode the output from bytes to string and strip any new line characters
    free_space_value = stdout.decode('utf-8').strip()
    return free_space_value

# Main Program
if __name__ == '__main__':
    # Call the free_space function and print the result
    print(free_space())
