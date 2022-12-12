import unittest


def solution(str1, str2):
    numDice = int(str1)
    bet = str2.split()
    total = int(bet[0])
    kind = bet[-1]

    freq = [0]*6*numDice

    for i in range(6**numDice):
        results = [i//6**j % 6 + 1 for j in range(numDice)]
        freq[sum(results) - 1] += 1

    if kind == 'lower':
        tot = freq[total:]
    else:
        tot = freq[:max(0,total-1)]

    prob = sum(tot) / 6**numDice

    res = f"{prob:.3f} {'Yes!' if prob > .5 else 'No!'}"

    return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('7', '24 or higher'), '0.414 No!')  # add assertion here

    def test2(self):
        self.assertEqual(solution('5', '18 or higher'), '0.500 No!')  # add assertion here

    def test3(self):
        self.assertEqual(solution('2', '7 or lower'), '0.417 No!')  # add assertion here



if __name__ == '__main__':
    unittest.main()
