def solution(relation):
    answer = 0
    # len_relation_row = len(relation[0])
    len_relation_column = len(relation)

    # TODO
    # get_subset algorithm
    
    # test example
    subset = [[0], [1], [2], [3], [0, 1], [0, 2, 3], [1, 2], [2, 3], [3]]

    # get_unique_subset algorithm
    unique_subset = []
    for numbers in subset:
        temp = []
        for y in range(len_relation_column):
            word = ''
            for number in numbers:
                word += relation[y][number] + '.'
            # print(word)
            if word not in temp:
                temp.append(word)
            else:
                break
        else:
            unique_subset.append(numbers)
            # print(temp)
    print(unique_subset)

    # 


    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))