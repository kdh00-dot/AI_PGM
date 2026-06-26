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

## 정리

파이썬 리스트는 여러 데이터를 효율적으로 저장하고 다루는 데 매우 유용한 자료형입니다. 데이터 관리, 반복 처리, 간단한 알고리즘 구현에 널리 사용됩니다.
