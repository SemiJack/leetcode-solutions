from operator import concat


class Solution:
    def concatenatedBinary(n: int) -> int:
        train = ''
        for i in range(1,n+1):
            p = (bin(i))[2:]
            print(p)
            train = train + p  
        print(int(train,2) % 1000000007)
if __name__ == '__main__':
    test = Solution
    test.concatenatedBinary(154)