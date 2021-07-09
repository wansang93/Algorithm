from itertools import combinations, chain

def get_all_subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


def solution(relation):
    all_subset = list(get_all_subset(list(range(0, len(relation[0])))))
    print(all_subset)

    unique_list = []
    for subset in all_subset:
        temp_set = set()
        for row in range(len(relation)):
            temp_string = ''
            for column in subset:
                temp_string += relation[row][column] + '.'
            if not temp_string in temp_set:
                temp_set.add(temp_string)
            else:
                break
        else:
            unique_list.append(subset)

    unique_list.sort(key=lambda x: len(x))
    print(unique_list)

    answer_list = []
    for subset in unique_list:
        subset = set(subset)
        check = True
        for j in answer_list:
            if j.issubset(subset):
                break
        else:
            answer_list.append(subset)

    print(answer_list)        

    return len(answer_list)



data = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(data))
