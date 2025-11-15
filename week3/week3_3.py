from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)
    toatl = 0
    for i in sorted_counts:
        toatl += i
        answer += 1
        if toatl >= k:
            break
    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
