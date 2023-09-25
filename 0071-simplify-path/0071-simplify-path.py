from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        parts = path.split('/')  # 경로를 슬래시로 분할
        
        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()  # 상위 디렉토리로 이동
            elif part and part != '.':
                stack.append(part)  # 현재 디렉토리 추가
        
        simplified_path = '/' + '/'.join(stack)
        return simplified_path if simplified_path else '/'
