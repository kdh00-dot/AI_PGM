def fibonacci_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    try:
        n = int(input("몇 개의 피보나치 수를 출력할까요? "))
    except ValueError:
        print("정수를 입력해주세요.")
        return

    sequence = fibonacci_sequence(n)
    print("피보나치 수열:", sequence)


if __name__ == "__main__":
    main()
