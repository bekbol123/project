from collections import Counter

def convert_to_arabic(number: str) -> int:
    c = dict(Counter(number))
    for k, v in c.items():
        if k in ['V', "L", 'D']:
            if v > 1:
                return -1
    if 'XXXX' in number or 'IIII' in number or 'CCCC' in number or 'MMMM' in number:
        return -1
    d = dict()
    d['I'] = 1
    d['V'] = 5
    d['X'] = 10
    d['L'] = 50
    d['C'] = 100
    d['D'] = 500
    d['M'] = 1000
    good = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    if len(number) == 0 or number == ' ':
        return 0
    res = 0
    for i in range(len(number)):
        if i < len(number) - 1 and d[number[i]] < d[number[i + 1]]:
            check = number[i:i + 2]
            if check not in good:
                return -1
            res -= d[number[i]]
            else:
            res += d[number[i]]
            return res

roman_number = input()
print(convert_to_arabic(roman_number))