def solution(participant, completion):
    completion.append("z" * 20)
    for p_name, c_name in zip(sorted(participant), sorted(completion)):
        if p_name != c_name:
            return(p_name)