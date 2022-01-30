# SQL 고득점 Kit

- 2020-09-04 ~ 2020-09-07 (4Days) Finished

SQL Site Link -> [https://programmers.co.kr/learn/challenges?tab=sql_practice_kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit)

## SELECT

### 모든 레코드 조회하기

``` sql
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 역순 정렬하기

``` sql
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```

### 아픈 동물 찾기

``` sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
```

### 어린 동물 찾기

``` sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
```

### 동물의 아이디와 이름

``` sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

### 여러 기준으로 정렬하기

``` sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
```

### 상위 n개 레코드

``` sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```

## SUM, MAX, MIN

### 최댓값 구하기

``` sql
SELECT MAX(DATETIME) 시간
FROM ANIMAL_INS
```

### 최솟값 구하기

``` sql
SELECT MIN(DATETIME) 시간
FROM ANIMAL_INS
```

### 동물 수 구하기

``` sql
SELECT COUNT(ANIMAL_ID) count
FROM ANIMAL_INS
```

### 중복 제거하기

``` sql
SELECT COUNT(DISTINCT NAME) count
FROM ANIMAL_INS
```

## GROUP BY

### 고양이와 개는 몇 마리 있을까

``` sql
SELECT ANIMAL_TYPE, COUNT(*) count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE
```

### 동명 동물 수 찾기

``` sql
SELECT NAME, COUNT(*) count
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```

### 입양 시각 구하기(1)

``` sql
SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 and HOUR <= 19
ORDER BY HOUR
```

### 입양 시각 구하기(2)

``` sql
SET @hour := -1;

SELECT (@hour := @hour + 1) as HOUR,
(SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23
```

- SET 옆에 변수명과 초기값을 설정할 수 있습니다.
  - @가 붙은 변수는 프로시저가 종료되어도 유지된다고 생각하면 됩니다.
  - 이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.
- @hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 :=은 비교 연산자 =과 혼동을 피하기 위한의 대입 연산입니다.
- SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.
- 이 때 처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0이 저장됩니다.
  - HOUR 값이 0부터 시작할 수 있습니다.
  - WHERE @hour < 23일 때까지, @hour 값이 계속 + 1씩 증가합니다.
  
> source from <https://chanhuiseok.github.io/posts/db-6/>

### 이름이 없는 동물의 아이디

``` sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
```

### 이름이 있는 동물의 아이디

``` sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

### NULL 처리하기

``` sql
SELECT ANIMAL_TYPE, IFNULL(NAME, "No name"), SEX_UPON_INTAKE
FROM ANIMAL_INS
```

## JOIN

### 없어진 기록 찾기

``` sql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID=ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
```

### 있었는데요 없었습니다

``` sql
SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE ANIMAL_INS.DATETIME>ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME
```

### 오랜 기간 보호한 동물(1)

``` sql
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID is NULL
ORDER BY A.DATETIME ASC limit 3
```

### 보호소에서 중성화한 동물

``` sql
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE '%Intact%'
AND (B.SEX_UPON_OUTCOME LIKE '%Neutered%' OR B.SEX_UPON_OUTCOME LIKE '%Spayed%')
```

## String, Date

### 루시와 엘라 찾기

``` sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID
```

### 이름에 el이 들어가는 동물 찾기

``` sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%EL%' AND ANIMAL_TYPE in ('dog')
ORDER BY NAME
```

### 중성화 여부 파악하기

``` sql
SELECT ANIMAL_ID, NAME, CASE
WHEN SEX_UPON_INTAKE LIKE '%Neutered%'OR SEX_UPON_INTAKE LIKE '%Spayed%'
THEN 'O'
ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS
```

### 오랜 기간 보호한 동물(2)

``` sql
SELECT AI.ANIMAL_ID, AI.NAME
FROM ANIMAL_INS AI
LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
WHERE AO.ANIMAL_ID IS NOT NULL
ORDER BY AO.DATETIME - AI.DATETIME DESC limit 2
```

### DATETIME에서 DATE로 형 변환

``` sql
SELECT ANIMAL_ID, NAME, 
DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
```
