version = [int(number) for number in input().split(".")]
# we need to increase the last digit
version[-1] += 1
# we go through from right to left we go from length the list
for index in range(len(version) - 1, - 1, -1):
    # we make statement if the index_jumps is 10
    if version[index] > 9:
        version[index] = 0
        # if the index_jumps is 10 we need to increase the next index_jumps with 1
        if version[index - 1] >= 0:
            version[index - 1] += 1
print('.'.join(str(number) for number in version))

# --------------------------------- 02. Next Version ---------------------
# You are fed up with changing the version of your software manually.
# Instead, you will create a little script that will make it for you.
# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
# The only rule is that the numbers cannot be greater than 9.
# If it happens, set the current number to 0 and increase the previous number.
# For more clarification, see the examples below.
# Note: there will be no case in which the first number will become greater than 9.

# Inputs:
# 1.2.3
# 1.3.9
# 3.9.9

# Outputs:
# 1.2.4
# 1.4.0
# 4.0.0
