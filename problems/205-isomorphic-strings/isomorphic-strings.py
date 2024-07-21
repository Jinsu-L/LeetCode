class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def get_mapping(string):
            i = 0
            hash_map = dict()
            for c in string:
                if c not in hash_map:
                    hash_map[c] = str(i)
                    i += 1
            
            return "_".join([hash_map[c] for c in string])

        return get_mapping(s) == get_mapping(t)