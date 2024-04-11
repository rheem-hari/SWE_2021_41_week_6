from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # 숫자와 그 인덱스를 추적하기 위한 사전 생성
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# 예제 사용법
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # 출력: [0, 1]
    print(twoSum([3, 2, 4], 6))       # 출력: [1, 2]
    print(twoSum([3, 3], 6))          # 출력: [0, 1]
