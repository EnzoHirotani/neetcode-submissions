class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

#contar num hash O(n)
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

#ordenar pra achar os mais frequentes
        arr = sorted(hash, key=hash.get, reverse=True)

#pegar os k mais frequentes
        saida = []
        for i in range(k):
            saida.append(arr[i])
        return saida