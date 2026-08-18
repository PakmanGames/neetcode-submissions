class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_track = {}
        for i in range(len(s)):
            if not s[i] in t:
                return False
            else:
                if s[i] in s_track:
                    s_track[s[i]] += 1
                else:
                    s_track[s[i]] = 1
        t_track = {}
        for i in range(len(t)):
            if not t[i] in s:
                return False
            else:
                if t[i] in t_track:
                    t_track[t[i]] += 1
                else:
                    t_track[t[i]] = 1
        
        for key, val in s_track.items():
            if val != t_track[key]:
                return False
        return True