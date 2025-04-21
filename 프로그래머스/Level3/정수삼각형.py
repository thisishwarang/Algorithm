def solution(triangle):
    memo = {}
    
    def calc(idx, level):
        if (idx, level) in memo:
            return memo[(idx, level)]
        
        if level == len(triangle) - 1:
            return triangle[level][idx]
        
        left = calc(idx, level+1)
        right = calc(idx+1, level+1)
        
        memo[(idx, level)] = triangle[level][idx] + max(left, right)
        return memo[(idx, level)]
        
    return calc(0, 0)