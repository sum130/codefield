def solution(brown, yellow):
    answer = []
    total = brown + yellow
    w = 0
    h = 0
    for h in range(3, total):
        if total % h == 0:
            for h in range(3, total):
                w = total // h
                if (w-2) * (h-2) == yellow:
                    answer = [h, w]

    return answer