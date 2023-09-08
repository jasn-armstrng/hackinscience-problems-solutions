from math import floor

def sum_multiples_of_3_or_5(n: int) -> int:
    x = floor((n-1)/3)
    y = floor((n-1)/5)
    z = floor((n-1)/15)

    # print(x, y, z)
    return int((3*x*(x+1)/2) + (5*y*(y+1)/2) - (15*z*(z+1)/2))

def main() -> None:
    print(sum_multiples_of_3_or_5(1000))

if __name__ == "__main__":
    main()
