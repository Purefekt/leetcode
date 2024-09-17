class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        s1 = s1.split(' ')
        s2 = s2.split(' ')

        count_s1 = collections.defaultdict(int)
        count_s2 = collections.defaultdict(int)

        for w in s1:
            count_s1[w] += 1
        for w in s2:
            count_s2[w] += 1
        
        s1_unique = set()
        s2_unique = set()
        for k,v in count_s1.items():
            if v==1:
                s1_unique.add(k)
        for k,v in count_s2.items():
            if v==1:
                s2_unique.add(k)
        
        all_s1 = set(list(count_s1.keys()))
        all_s2 = set(list(count_s2.keys()))

        only_s1 = s1_unique - all_s2
        only_s2 = s2_unique - all_s1
        res = only_s1.union(only_s2)
        return res
        