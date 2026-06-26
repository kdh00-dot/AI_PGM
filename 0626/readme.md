# Python Containers

파이썬의 **컨테이너(Container)** 는 여러 개의 데이터를 저장하는
자료형입니다.

## 1. List (`list`)

-   순서: O
-   변경 가능(Mutable): O
-   중복 허용: O

``` python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)
```

주요 메서드

  메서드           설명
  ---------------- --------------------------
  `append(x)`      끝에 추가
  `insert(i, x)`   원하는 위치에 삽입
  `remove(x)`      값 삭제
  `pop()`          마지막 요소 삭제 및 반환
  `sort()`         정렬
  `reverse()`      순서 뒤집기

------------------------------------------------------------------------

## 2. Tuple (`tuple`)

-   순서: O
-   변경 가능: X (Immutable)
-   중복 허용: O

``` python
point = (10, 20)
print(point[0])
```

------------------------------------------------------------------------

## 3. Dictionary (`dict`)

-   키(Key)-값(Value) 저장
-   키는 중복 불가
-   변경 가능

``` python
student = {
    "name": "Kim",
    "age": 20
}

print(student["name"])
student["major"] = "Computer"
```

주요 메서드

  메서드       설명
  ------------ ---------------
  `keys()`     키 반환
  `values()`   값 반환
  `items()`    (키, 값) 반환
  `get(key)`   값 조회
  `update()`   수정

------------------------------------------------------------------------

## 4. Set (`set`)

-   순서 없음
-   중복 허용 안 함
-   변경 가능

``` python
nums = {1, 2, 2, 3}
print(nums)
```

집합 연산

``` python
a = {1,2,3}
b = {3,4,5}

print(a | b)
print(a & b)
print(a - b)
```

------------------------------------------------------------------------

## 컨테이너 비교

  자료형              순서          중복   수정
  ------------ ------------------- ------ ------
  List                  O            O      O
  Tuple                 O            O      X
  Dictionary    O(삽입 순서 유지)   키 X    O
  Set                   X            X      O

------------------------------------------------------------------------

## 자주 사용하는 내장 함수

``` python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))
```

## 요약

-   **List**: 가장 많이 사용하는 컨테이너
-   **Tuple**: 변경 불가능한 데이터 저장
-   **Dictionary**: 키-값 형태 저장
-   **Set**: 중복 제거 및 집합 연산

## 정리

파이썬 리스트는 여러 데이터를 효율적으로 저장하고 다루는 데 매우 유용한 자료형입니다. 데이터 관리, 반복 처리, 간단한 알고리즘 구현에 널리 사용됩니다.
