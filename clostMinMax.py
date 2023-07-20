class Solution:
    def closeMinMax(self, array):
        max_val = float('-inf')
        min_val = float('inf')
        for x in array:
            if x > max_val:
                max_val = x
            if x < min_val:
                min_val = x
        last_min_index = -1
        last_max_index = -1
        result = len(array)
        for i in range(len(array)):
            if array[i] == min_val:
                last_min_index = i
                if last_max_index >= 0:
                    result = min(result, i - last_max_index + 1)
            if array[i] == max_val:
                last_max_index = i
                if last_min_index >= 0:
                    a = i - last_min_index + 1
                    result = min(result, a)
        return result

size = int(input())
array = list(map(int, input().split()))
answer = Solution()
print(answer.closeMinMax(array))
