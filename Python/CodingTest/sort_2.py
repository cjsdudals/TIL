def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if str(numbers[i])[len(str(numbers[i]))] < str(numbers[j])[len(str(numbers[j]))]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            elif str(numbers[i])[0] == str(numbers[j])[0]:
                if str(numbers[i]*10)[0] < str(numbers[j]*10)[1]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    for num in numbers:
        answer += str(num)
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))