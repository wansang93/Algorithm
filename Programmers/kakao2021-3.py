import math

def get_time(str):
    h, m = map(int, str.split(':'))
    # print(h, m)
    return h * 60 + m

def solution(fees, records):
    answer = []
    defalut_time, default_fee, unit_time, unit_fee = fees

    parking = {}
    result_time = {}
    for record in records:
        time, car_num, status = record.split()
        if status == 'IN':
            # print(get_time(time), car_num, '들어옴')
                parking[car_num] = get_time(time)
        elif status == 'OUT':
            # print(get_time(time), car_num, '나감')
            if car_num not in result_time:
                result_time[car_num] = get_time(time) - parking[car_num]
            else:
                result_time[car_num] += get_time(time) - parking[car_num]
            parking[car_num] = -1

    for car_num in parking:
        if parking[car_num] != -1:
            if car_num not in result_time:
                result_time[car_num] = get_time("23:59") - parking[car_num]
            else:
                result_time[car_num] += get_time("23:59") - parking[car_num]

    result = sorted(result_time)

    for all_time in result:
        all_time = int(all_time)
        total = default_fee
        if all_time > defalut_time:
            total += unit_fee * math.ceil((all_time - defalut_time) / unit_time)
        answer.append(total)

    return answer



data1 = [180, 5000, 10, 600]
data11 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

data2 = [120, 0, 60, 591]
data22 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

data3 = [1, 461, 1, 10]
data33 = ["00:00 1234 IN"]

print(solution(data1, data11))  # [14600, 34400, 5000]
print(solution(data2, data22))  # [0, 591]
print(solution(data3, data33))  # [14841]
