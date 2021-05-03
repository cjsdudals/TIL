def solution(array, commands):
    answer = []
    for command in commands:
        sort = array[command[0]-1:command[1]]
        for i in range(len(sort)):
            for j in range(i, len(sort)):
                if sort[i] > sort[j]:
                    sort[i], sort[j] = sort[j], sort[i]
        answer.append(sort[command[2]-1])

    return answer

print(solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]]))