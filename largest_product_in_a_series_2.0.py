# https://www.hackinscience.org/exercises/largest-product-in-a-series

series: str = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
series = series.replace('\n', '')

def largest_product_of_adjacent_digits_in_series(series: str, number_of_adjacent_digits: int) -> int:
    window_start    = 0
    window_end      = number_of_adjacent_digits
    largest_product = 0
    product         = 1

    # Compute the first product of the "window" in the series
    for i in range(window_start, window_end):
        product *= int(series[i])
    largest_product = max(largest_product, product)

    # Subsequently,
    # 1. Divide the last computed product by the first element in the last window, then multiply the result by the last element in the new window.
    #    This avoids recalculating the product my multiplying all the elements in the window
    # 2. Unless, the first element of the last window is zero, then we recalculate the product my multiplying all the elements in the new window.
    #    This avoids a division by zero error
    while window_end < len(series):
        if int(series[window_start]) == 0:
            product = 1
            for i in range(window_start+1, window_end+1):
                product *= int(series[i])
        else:
            product = (product//int(series[window_start]) * int(series[window_end]))

        largest_product = max(largest_product, product)
        window_start += 1
        window_end += 1
    return largest_product

def tests() -> None:
    assert largest_product_of_adjacent_digits_in_series("716362", 4) == 216
    assert largest_product_of_adjacent_digits_in_series(series, 13) == 23514624000
    print("All tests have passed")

def main() -> None:
    tests()

if __name__ == "__main__":
    main()
