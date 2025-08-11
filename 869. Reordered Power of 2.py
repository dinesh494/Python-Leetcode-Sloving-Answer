class Solution(object):
    def reorderedPowerOf2(self, n):
        def signature(num):
            return ''.join(sorted(str(num)))
        
        target = signature(n)
        
        # Check all powers of 2 up to 2^30
        for i in range(31):
            if signature(1 << i) == target:
                return True
        return False
