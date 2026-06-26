# 파이썬 리스트

파이썬 **리스트(list)** 는 여러 값을 하나의 변수에 담아 순서대로 관리하는 자료형입니다. 대괄호 `[]`로 만들며, 요소를 추가하거나 수정하고 삭제할 수 있습니다.

## 기본 개념

- 리스트는 여러 개의 값을 하나의 변수에 저장할 수 있습니다.
- 요소의 순서가 있으며, 0부터 시작하는 인덱스로 접근합니다.
- 숫자, 문자열, 불리언 등 다양한 자료형을 함께 넣을 수 있습니다.

## 생성 방법

```python
fruits = ['apple', 'banana', 'cherry']
empty_list = []
```

리스트는 대괄호 안에 값들을 쉼표로 구분해 작성합니다.

## 인덱싱과 슬라이싱

- `fruits[0]` : 첫 번째 요소
- `fruits[-1]` : 마지막 요소
- `fruits[0:2]` : 처음부터 두 번째 요소까지

```python
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(fruits[-1])
print(fruits[0:2])
```

## 자주 쓰는 기능

- `append()` : 마지막에 요소 추가
- `insert()` : 원하는 위치에 요소 추가
- `remove()` : 특정 값 삭제
- `pop()` : 인덱스로 요소 꺼내고 삭제
- `len()` : 리스트 길이 확인
- `sort()` : 정렬
- `reverse()` : 순서 뒤집기

```python
numbers =[2][3][1]
numbers.append(4)
numbers.remove(1)
numbers.sort()
```

## 반복문과 함께 사용하기

리스트는 `for`문과 함께 자주 사용됩니다. 각 요소를 하나씩 꺼내서 처리할 수 있습니다.

```python
for fruit in fruits:
    print(fruit)
```

인덱스도 함께 보고 싶다면 `enumerate()`를 사용할 수 있습니다.

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

## 예시

```python
students = ['Kim', 'Lee', 'Park']
students.append('Choi')
print(students)
```

실행 결과 예시:

```python
['Kim', 'Lee', 'Park', 'Choi']
```
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
