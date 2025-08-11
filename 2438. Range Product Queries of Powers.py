class Solution(object):
    def productQueries(self, n, queries):
        MOD = 10**9 + 7
        
        # Step 1: Build powers array
        powers = []
        bit = 0
        temp = n
        while temp > 0:
            if temp & 1:
                powers.append(1 << bit)
            bit += 1
            temp >>= 1
        
        # Step 2: Prefix product
        prefix = [0] * len(powers)
        prefix[0] = powers[0] % MOD
        for i in range(1, len(powers)):
            prefix[i] = (prefix[i-1] * powers[i]) % MOD
        
        # Step 3: Answer queries
        ans = []
        for l, r in queries:
            if l == 0:
                product = prefix[r]
            else:
                product = (prefix[r] * pow(prefix[l-1], MOD-2, MOD)) % MOD
            ans.append(product)
        
        return ans
