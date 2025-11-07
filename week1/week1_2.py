#week1_2

def solution(num):
    answer = ''
    
    
    num %= 2
    if (num == 0):
        answer = 'Even'
    else:
        answer = 'Odd'    
    
    return answer

print(solution(3))
