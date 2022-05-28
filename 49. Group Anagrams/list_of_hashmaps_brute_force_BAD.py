class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a list of hashmaps of all strings in the list
        hashmap_list = []
        for s in strs:
            hashmap = {}
            for c in s:
                if c not in hashmap.keys():
                    hashmap[c] = 1
                else:
                    hashmap[c] = hashmap[c] + 1
            hashmap_list.append(hashmap)
        
        print(hashmap_list)
        
        # go through all elements and make pairs, replace paired up elements with None
        anagrams = []
        for i in range(0, len(hashmap_list)):
            if hashmap_list[i] != None:
                current_anagrams = [strs[i]] # CHANGE 
                for j in range(i+1, len(hashmap_list)):
                    if hashmap_list[j] != None:
                        if hashmap_list[i] == hashmap_list[j]:
                            current_anagrams.append(strs[j]) # CHANGE
                            
                            # set the paired up word to None
                            hashmap_list[j] = None
                        else:
                            pass
                    else:
                        pass
                anagrams.append(current_anagrams)
            else:
                pass
        
        
        return anagrams