class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = deque()
        def searchFile(queuepath):
            queue = queuepath
            ans = ""
            ans+=(queue.popleft())

            while queue:
                if queue[0]=="/":
                    break
               
                ans+=(queue.popleft())
            return (queue),(ans)
        
        # while True:
        #     if nextchar is '/..' or '/../':
        #         answerdelete
        #     if nextchar is '/.' or '/./'
        #        skip
        #     else 
        #        anser add
        
        queue=deque(path)
        ans=""
        FileMemory = deque()
        while queue:
            queue,nextFile = searchFile(queue)
            print(ans)
            #print(nextFile,ans)
            if nextFile =="/..":
                currFile=FileMemory.pop() if FileMemory else ""
               
                ans=ans[:-len(currFile)]
                print("delete",ans,currFile)
            elif nextFile == "/." or nextFile == "/" :
                continue
            else:
                ans+=nextFile
                FileMemory.append(nextFile)
               # print("get",ans)
        return ans if len(ans)>0 else "/"
            
            
            
            
             
