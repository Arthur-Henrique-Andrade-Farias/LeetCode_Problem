class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Inicializa os índices para os elementos de nums1 e nums2
        i, j, k = m-1, n-1, m+n-1

        # Mescla os arrays de trás para frente
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Adiciona os elementos restantes de nums2, se houver
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1