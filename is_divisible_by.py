from typing import List


def sum_digits(num: int) -> int:
    str_num = str(num)
    return sum([int(i) for i in str_num])


def is_divisible_by(nums: List[int], divisible_by: int, sum_divisible_by: int) -> List[int]:
    result: List[int] = []
    for i in nums:
        if i % divisible_by == 0 and sum_digits(i) % sum_divisible_by == 0:
            result.append(i)
    return result


def main() -> None:
    print(is_divisible_by(range(1500, 1700), 7, 3))


if __name__ == "__main__":
    main()
