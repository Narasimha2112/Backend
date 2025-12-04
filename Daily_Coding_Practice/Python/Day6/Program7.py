#Class with args

class Total:
    def sum(self, *nums):
        return sum(nums)

t = Total()
print(t.sum(10,20,40))