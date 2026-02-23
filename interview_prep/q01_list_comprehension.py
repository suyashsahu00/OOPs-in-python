# =============================================
# Q01: List Comprehension
# =============================================
# Task: Convert this for-loop into a ONE LINE list comprehension
#
# The for-loop version:
# result = []
# for i in range(1, 6):
#     result.append(i * i)
# print(result)  → [1, 4, 9, 16, 25]
#
# Now write it in ONE line using list comprehension:

result = [i*i for i in range(1,6)]     # Fill in the ?
print(result)
# Expected output: [1, 4, 9, 16, 25]
