# -*- coding: utf-8 -*-
# @Author  : RainQaQ
# @Time    : 2019/7/16 0:14
# IDE      :pycharm

# 冒泡排序


def BubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


nums = [3, 5, 15, 36, 26, 27, 2, 36, 4, 19]
print(BubbleSort(nums))
