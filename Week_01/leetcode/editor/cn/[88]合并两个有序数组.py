# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针 
#  👍 563 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """
        1.合并后再排序
        时间复杂度 : O((n + m)log(n + m))
        空间复杂度:O(1)
        """
        # for i in range(m, m+n):
        #     nums1[i] = nums2[i-m]
        # nums1.sort()
        """
        2.双指针法，从前往后
        时间复杂度：O(N+M)
        空间复杂度：O(m)
        """
        arr = [0 for _ in range(m+n)]
        i = 0
        p = 0
        q = 0
        while p < m or q < n:
            # 注意两个边界条件
            if p == m:
                arr[i] = nums2[q]
                q += 1
            elif q == n:
                arr[i] = nums1[p]
                p += 1
            elif nums1[p] <= nums2[q]:
                arr[i] = nums1[p]
                p += 1
            else:
                arr[i] = nums2[q]
                q += 1
            i += 1
        for j in range(len(arr)):
            nums1[j] = arr[j]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    import copy
    # nums1 = [1,2,3,0,0,0]
    # nums2 = [2,5,6]
    # nums0 = copy.deepcopy(nums1)
    # nums1 = []
    # print(nums1,nums0)
    # p = 0
    # q = 0
    # while p < 3 and q < 3:
    #     if nums0[p] < nums2[q]:
    #         nums1.append(nums0[p])
    #         p += 1
    #     else:
    #         nums1.append(nums2[q])
    #         q += 1
    # if p < 3:
    #     nums1[p + q:] = nums0[p:]
    # if q < 3:
    #     nums1[p + q:] = nums2[q:]
    # print(nums1)
