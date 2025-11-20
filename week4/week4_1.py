import math

def solution(n):
    answer = 0
    for i in range(n // 2 + 1):
        j = n - 2*i
        a = 1
        for x in range(1, i+1):
            a *= x
        b = 1
        for x in range(1, j+1):
            b *= x
        c = 1
        for x in range(1, i+j+1):
            c *= x
        answer += c // (a*b)

        answer %= 1234567
    return answer



print(solution(5))
