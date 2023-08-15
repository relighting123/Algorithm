class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9+7
        dp={}
        #print(dp)
        def count(i,cnt_songtyp):
            if i==goal and cnt_songtyp==n:
                return 1
            #기존 선택한 곡을 한번 더 선택 가능한 조건인 경우
            if  i==goal or cnt_songtyp>n:
                return 0
         
            #print(i,cnt_songtyp)
            if (i,cnt_songtyp) in dp:
                return dp[(i,cnt_songtyp)]
            ans = (n-cnt_songtyp)*count(i+1,cnt_songtyp+1)%mod

            
            if cnt_songtyp>k:
                ans+=count(i+1,cnt_songtyp)*(cnt_songtyp-k)
            dp[(i,cnt_songtyp)]=ans
            return dp[(i,cnt_songtyp)]
            
        return count(0,0)
        
        
        
        
        
        