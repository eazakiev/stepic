nums = set(int(input()) for _ in range(3))
print(nums)
print([len(nums)])
print(["Равносторонний", "Равнобедренный", "Разносторонний"][len(nums) - 1])

print([18, 5, 8][2])