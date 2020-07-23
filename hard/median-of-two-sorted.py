class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined = []
        if nums1 == []:
            combined = nums2
        elif nums2 == []:
            combined = nums1
        else:
            i = j = 0
            for _ in range(len(nums1)+len(nums2)):
                if nums1 == []:
                    if nums2 != []:
                        combined.append(nums2[0])
                        nums2.pop(0)
                        continue
                if nums2 == []:
                    if nums1 != []:
                        combined.append(nums1[0])
                        nums1.pop(0)
                        continue
                if nums1[0] < nums2[0]:
                    combined.append(nums1[0])
                    nums1.pop(0)
                    continue
                combined.append(nums2[0])
                nums2.pop(0)
                
        print(combined)
        if len(combined)%2 == 0:
            return float(combined[len(combined)//2 - 1] + combined[len(combined)//2])/2
        return combined[len(combined)//2]
