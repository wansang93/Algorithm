def solution(encrypted_text, key, rotation):
    answer = ''
    
    # rotation 복구하기
    if rotation < 0:
        rotation = abs(rotation) % len(encrypted_text)
        encrypted_text = encrypted_text[-rotation:] + encrypted_text[:-rotation]
    else:
        rotation = rotation % len(encrypted_text)
        encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]

    for i, v in enumerate(encrypted_text):
        # v, key[i] 관계 설명하기
        difference = ord(v) - ord(key[i])
        if difference < 0:
            answer += chr(ord('z') + difference)
        else:
            answer += chr(ord('a') + difference - 1)

    return answer

print(solution('qyyigoptvfb', 'abcdefghijk', 3))  # 'hellopython'
