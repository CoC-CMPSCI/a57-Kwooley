import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # data1: n1=5, n2=8, N=3 -> 5 8 13
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'5.*8.*13'], lines)


@pytest.mark.T2
def test_main_2():
    # data2: n1=5, n2=10, N=5 -> 5 10 15 25 40
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'5.*10.*15.*25.*40'], lines)


@pytest.mark.T3
def test_main_3():
    # data3: n1=1, n2=1, N=7 -> 1 1 2 3 5 8 13
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'1.*1.*2.*3.*5.*8.*13'], lines)


@pytest.mark.T4
def test_main_4():
    # data4: n1=0, n2=5, N=6 -> 0 5 5 10 15 25
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'0.*5.*5.*10.*15.*25'], lines)
