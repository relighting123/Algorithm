class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = deque()
        def searchFile(queuepath):
            queue = queuepath
            File = ""
            File+=(queue.popleft())

            while queue:
                if queue[0]=="/":
                    break
               
                File+=(queue.popleft())
            return (queue),(File)
        
        queue=deque(path)
        ans=""
        FileMemory = deque()
        while queue:
            queue,nextFile = searchFile(queue)
            if nextFile =="/..":
                currFile=FileMemory.pop() if FileMemory else ""               
                ans=ans[:-len(currFile)]
            elif nextFile == "/." or nextFile == "/" :
                continue
            else:
                ans+=nextFile
                FileMemory.append(nextFile)
        return ans if len(ans)>0 else "/"
            
            
            
            
             
