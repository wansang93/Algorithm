'''
Ver0.01(21-02-01)
이 파일은 내가 푼 문제 모두가 README.md의 리스트에 잘 들어갔는지 체크하는 문서입니다.
1. 파일 목록을 체크한다.
3. readme.md 목록을 복사하여 체크한다.
3. 백준 정답을 복사하여 체크한다.

1, 2, 3번의 3가지를 비교하여 없거나 추가한 것을 체크한다.
비교된 것을 수동으로 바꿔준다.

# 추후 업데이트 하기
파일 목록을 자동으로 체크하기
백준 문제 크롤링해서 자동으로 따오기
README.md파일 자동으로 따오기
'''

import re
import os

# check how many md files in my folder
targerdir = r"C:/Users/wansang/Desktop/Gitrep/Algorithm/BAEKJOON/problems"
 
file_list = os.listdir(targerdir)
file_list_py = [file for file in file_list if file.endswith('.md')]
print('폴더의 파일 갯수:', len(file_list_py) - 1)  # 1 is README.md

# 백준 문제 번호 넣기
tt = '''
1000 1001 1002 1008 1011 1065 1085 1110 1152 1157 1193 1316 1330 1427 1436 1546 1712 1929 1978 2108 2231 2292 2438 2439 2447 2557 2562 2577 2581 2588 2675 2739 2741 2742 2750 2753 2775 2798 2839 2869 2884 2908 2941 3009 3052 3053 4153 4344 4673 4948 5622 8393 8958 9020 9498 10171 10172 10250 10430 10718 10757 10809 10818 10829 10869 10870 10871 10872 10950 10951 10952 10989 10998 11021 11022 11650 11653 11654 11720 11729 14681 15552 15596 15649 15650 15651 15652
'''

# md 파일 문제 넣기
t = '''
- [1000](./problems/1000.md)
- [1001](./problems/1001.md)
- [1002](./problems/1002.md)
- [1008](./problems/1008.md)
- [1085](./problems/1085.md)
- [1011](./problems/1011.md)
- [1065](./problems/1065.md)
- [1110](./problems/1110.md)
- [1152](./problems/1152.md)
- [1157](./problems/1157.md)
- [1193](./problems/1193.md)
- [1316](./problems/1316.md)
- [1330](./problems/1330.md)
- [1427](./problems/1427.md)
- [1436](./problems/1436.md)
- [1546](./problems/1546.md)
- [1712](./problems/1712.md)
- [1929](./problems/1929.md)
- [1978](./problems/1978.md)
- [2108](./problems/2108.md)
- [2231](./problems/2231.md)
- [2292](./problems/2292.md)
- [2438](./problems/2438.md)
- [2439](./problems/2439.md)
- [2447](./problems/2447.md)
- [2557](./problems/2557.md)
- [2562](./problems/2562.md)
- [2577](./problems/2577.md)
- [2581](./problems/2581.md)
- [2588](./problems/2588.md)
- [2675](./problems/2675.md)
- [2739](./problems/2739.md)
- [2741](./problems/2741.md)
- [2742](./problems/2742.md)
- [2750](./problems/2750.md)
- [2753](./problems/2753.md)
- [2775](./problems/2775.md)
- [2798](./problems/2798.md)
- [2839](./problems/2839.md)
- [2869](./problems/2869.md)
- [2884](./problems/2884.md)
- [2908](./problems/2908.md)
- [2941](./problems/2941.md)
- [3009](./problems/3009.md)
- [3052](./problems/3052.md)
- [3053](./problems/3053.md)
- [4153](./problems/4153.md)
- [4344](./problems/4344.md)
- [4673](./problems/4673.md)
- [4948](./problems/4948.md)
- [5622](./problems/5622.md)
- [8393](./problems/8393.md)
- [8958](./problems/8958.md)
- [9020](./problems/9020.md)
- [9498](./problems/9498.md)
- [10171](./problems/10171.md)
- [10172](./problems/10172.md)
- [10250](./problems/10250.md)
- [10430](./problems/10430.md)
- [10718](./problems/10718.md)
- [10757](./problems/10757.md)
- [10809](./problems/10809.md)
- [10818](./problems/10818.md)
- [10829](./problems/10829.md)
- [10869](./problems/10869.md)
- [10870](./problems/10870.md)
- [10871](./problems/10871.md)
- [10872](./problems/10872.md)
- [10950](./problems/10950.md)
- [10951](./problems/10951.md)
- [10952](./problems/10952.md)
- [10989](./problems/10989.md)
- [10998](./problems/10998.md)
- [11021](./problems/11021.md)
- [11022](./problems/11022.md)
- [11650](./problems/11650.md)
- [11653](./problems/11653.md)
- [11654](./problems/11654.md)
- [11720](./problems/11720.md)
- [11729](./problems/11729.md)
- [14681](./problems/14681.md)
- [15552](./problems/15552.md)
- [15596](./problems/15596.md)
- [15649](./problems/15649.md)
- [15650](./problems/15650.md)
- [15651](./problems/15651.md)
- [15652](./problems/15652.md)
'''

baekjoon = set(re.findall(r'\d+', tt))
read_me = set(re.findall(r'\d+', t))
print('README 파일 갯수:', len(read_me))
print('백준   파일 갯수:', len(baekjoon))
print('backjoon, README 대칭차집합', baekjoon ^ read_me)
print('README   에만 있는 파일:', read_me - baekjoon)
print('baekjoon 에만 있는 파일:', baekjoon - read_me)

'''
폴더의 파일 갯수: 87
README 파일 갯수: 87
백준   파일 갯수: 87
backjoon, README 대칭차집합 set()
README   에만 있는 파일: set()
baekjoon 에만 있는 파일: set()
'''
