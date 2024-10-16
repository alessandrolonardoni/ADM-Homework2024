### Solutions File


#PROBLEM 1
#INTRODUCTION
# introduction - ArithmeticOperator
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
# -------------------------------------------------

# introduction - Division
a = int(input())
b = int(input())

print(a // b)
print(a / b)
# -------------------------------------------------

# introduction - Loops
number = int(input())
for x in range(number):
    print(x * x)
# -------------------------------------------------

# introduction - PrintFunction
def print_numbers(number):
    string = ''
    for i in range(number):
        string += str(i + 1)
    print(string)


number = int(input())
print_numbers(number)
# -------------------------------------------------

# introduction - PythonIfElse
number = int(input())

if number % 2 == 1:
    print('Weird')
elif 2 <= number <= 5:
    print('Not Weird')
elif 6 <= number <= 20:
    print('Weird')
elif number > 20:
    print('Not Weird')
# -------------------------------------------------

# introduction - SayHelloWorldWithPython
print("Hello, World!")
# -------------------------------------------------

# introduction - WriteAFunction
def is_leap(year):
    if (year % 4 == 0):
        if (year % 400 == 0):
            return True
        if (year % 100 == 0):
            return False
        return True
    return False

year = int(input())
print(is_leap(year))
# -------------------------------------------------



#DATA TYPES
# basic-data-types - finding-the-percentage
def average(marks):
    return "{0:.2f}".format(sum(marks) / 3)


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores


query_name = input()
print(average(student_marks[query_name]))
# -------------------------------------------------

# basic-data-types - FindTheRunnerUpScore
def second_highest(array):
    array.sort()
    maximum = array[len(array) - 1]
    for i in range(len(array)):
        if array[len(array) - 1 - i] < maximum:
            return array[len(array) - 1 - i]


n = int(input())
array = list(map(int, input().split()))
print(second_highest(array))
# -------------------------------------------------

# basic-data-types - ListComprehension
x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n])
# -------------------------------------------------

# basic-data-types - Lists
queries = int(input())
data = []
for _ in range(queries):
    command, *parameter = input().split()
    parameters = list(map(int, parameter))

    if command == 'insert':
        data.insert(parameters[0], parameters[1])
    elif command == 'print':
        print(data)
    elif command == 'remove':
        data.remove(parameters[0])
    elif command == 'append':
        data.append(parameters[0])
    elif command == 'sort':
        data.sort()
    elif command == 'pop':
        data.pop()
    elif command == 'reverse':
        data.reverse()
# -------------------------------------------------

# basic-data-types - nested-lists
if __name__ == "__main__":
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        scores.append(score)
    second_min_score = sorted(set(scores))[1]
    student_names = sorted(
        [student[0] for student in students if student[1] == second_min_score]
    )
    print("\n".join(student_names))
# -------------------------------------------------

# basic-data-types - tuples
length = int(input())
tokens = input().split()
data = list(map(int, tokens))
t = tuple(data)
print(hash(t))
# -------------------------------------------------



#STRINGS
# strings - alphabet-rangoli
a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    lines = []
    for row in range(size):
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    width = len(lines[0])
    
    for row in range(size-1, 0, -1):
        print(lines[row].center(width, '-'))
        
    for row in range(size):
        print(lines[row].center(width, '-'))
# -------------------------------------------------

# strings - capitalize!
def solve(s):
    ans = s.split(' ')
    ans1 = (((i.capitalize() for i in ans)))
    return ' '.join(ans1)
    
# -------------------------------------------------

# strings - designer-door-mat
def printPattern(pattern, count):
    for j in range(count):
        print(pattern, end='')


n, m = map(int, input().split())

# Upper part
for i in range(n//2):
    printPattern('-', (m-3) // 2 - (3 * i))
    printPattern('.|.', 2 * i + 1)
    printPattern('-', (m - 3) // 2 - (3 * i))
    print()

# Middle part
printPattern('-', (m - 7) // 2)
print('WELCOME', end='')
printPattern('-', (m - 7) // 2)
print()

# Lower Part
for i in range(n // 2):
    printPattern('-', 3 * (i + 1))
    printPattern('.|.', n - 2 * (i + 1))
    printPattern('-', 3 * (i + 1))
    print()
# -------------------------------------------------

# strings - find-a-string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:(i + len(sub_string))] == sub_string:
                count += 1
                i += len(sub_string) - 1

    return count

# -------------------------------------------------

# strings - merge-the-tools
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))      
        print(word1)
        i = i + k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
# -------------------------------------------------

# strings - mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[(position + 1):]


# -------------------------------------------------

# strings - string-formatting
width = len('{0:b}'.format(n))

for i in range(1, n + 1):
    print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))
# -------------------------------------------------

# strings - string-split-and-join
def split_and_join(string):
    tokens = string.split()
    return '-'.join(tokens)

# -------------------------------------------------

# strings - string-validators
def hasalpha(string):
    for character in string:
        if character.isalpha():
            return True

    return False


def hasalnum(string):
    for character in string:
        if character.isalnum():
            return True

    return False


def hasdigit(string):
    for character in string:
        if character.isdigit():
            return True

    return False


def haslower(string):
    for character in string:
        if character.islower():
            return True

    return False


def hasupper(string):
    for character in string:
        if character.isupper():
            return True

    return False


string = input()

print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))
# -------------------------------------------------

# strings - swap-case
def swap_case(s):
    result = ""
    for let in s:
        if let.isupper():
            result += let.lower()
        else:
            result += let.upper()
    return result


string = input()
print(swap_case(string))
# -------------------------------------------------

# strings - text-alignment
thickness = int(input())  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(
        ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
    )
# -------------------------------------------------

# strings - text-wrap
def wrap(string, max_width):
    paragraph = ''
    count = 0
    for i in range(len(string)):
        if i % max_width == 0 and i != 0:
            paragraph += '\n'
        paragraph += string[i]
    return paragraph
# -------------------------------------------------

# strings - the-minion-game
def minion_game(string):
    n = len(string)
    kevin_score = 0
    stuart_score = 0

    for i in range(n):
        if string[i] in "AEIOU":
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")     
# -------------------------------------------------

# strings - whats-your-name
def print_full_name(firstName, lastName):
    print('Hello ' + firstName + ' ' + lastName+ '! You just delved into python.')
# -------------------------------------------------



#SETS
# sets - check-subset
def get_set():
    return set(map(int, input().split()))


queries = int(input())

for _ in range(queries):
    input()
    A = get_set()
    input()
    B = get_set()
    print(A.issubset(B))
# -------------------------------------------------

# sets - introduction-to-sets
def average(array):
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    
    return (avg)
         

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
# -------------------------------------------------

# sets - is-strict-superset
def get_set():
    return set(map(int, input().split()))


def is_super_set(main, sets):
    for set in sets:
        if not main.issuperset(set):
            return False

    return True


A = get_set()
queries = int(input())
sets = []

for _ in range(queries):
    sets.append(get_set())

print(is_super_set(A, sets))
# -------------------------------------------------

# sets - no-idea
n, m = map(int, input().split())

array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for element in array:
    if element in A:
        happiness += 1
    elif element in B:
        happiness -= 1

print(happiness)
# -------------------------------------------------

# sets - set-add
n = int(input())
stamps = set()
for i in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))
# -------------------------------------------------

# sets - set-difference-operation
int(input())
english_subscriptions = set(map(int, input().split()))

int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.difference(french_subscriptions)
print(len(all_subscriptions))
# -------------------------------------------------

# sets - set-disacard-remove-pop
n = int(input())
numbers = set(map(int, input().split()))
queries = int(input())

for i in range(queries):
    command = input()

    if command == 'pop':
        numbers.pop()
    else:
        line = command.split()
        command = line[0]
        element = int(line[1])

        if command == 'remove':
            numbers.remove(element)
        else:
            numbers.discard(element)

print(sum(numbers))
# -------------------------------------------------

# sets - set-intersection-operation
int(input())
english_subscriptions = set(map(int, input().split()))

int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.intersection(french_subscriptions)
print(len(all_subscriptions))
# -------------------------------------------------

# sets - set-mutations
_ = input()
A = set(map(int, input().split()))

queries = int(input())

for i in range(queries):
    command = input().split()[0]
    temp = set(map(int, input().split()))

    if command == 'update':
        A.update(temp)
    elif command == 'intersection_update':
        A.intersection_update(temp)
    elif command == 'difference_update':
        A.difference_update(temp)
    else:
        A.symmetric_difference_update(temp)

print(sum(A))
# -------------------------------------------------

# sets - set-symmetric-difference
int(input())
english_subscriptions = set(map(int, input().split()))

int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.symmetric_difference(french_subscriptions)
print(len(all_subscriptions))
# -------------------------------------------------

# sets - set-union-operation
_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

NEW_SET = SET_N.union(SET_B)
print(len(NEW_SET))
# -------------------------------------------------

# sets - symmetric-difference-operation
_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.symmetric_difference(b)))
# -------------------------------------------------

# sets - the-captains-room
k = int(input())
array = list(map(int, input().split()))

frequencies = dict()

for element in array:
    frequencies[element] = (frequencies[element] if element in frequencies else 0) + 1

for key in frequencies:
    if frequencies[key] == 1:
        print(key)
        break
# -------------------------------------------------



#COLLECTIONS
# collections - collections-counter
import collections

number_of_shoes = int(input())
shoes = collections.Counter(list(map(int, input().split())))
queries = int(input())

profit = 0
for _ in range(queries):
    size, price = map(int, input().split())
    if size in shoes:
        profit += price
        if shoes[size] == 1:
            del shoes[size]
        else:
            shoes[size] -= 1

print(profit)
# -------------------------------------------------

# collections - collections-dequeue
import collections

queue = collections.deque()

queries = int(input())

for _ in range(queries):
    line = input()
    if line == 'pop':
        queue.pop()
    elif line == 'popleft':
        queue.popleft()
    else:
        line = line.split()
        command = line[0]
        element = int(line[1])
        if command == 'append':
            queue.append(element)
        else:
            queue.appendleft(element)

for element in queue:
    print(element, end=' ')
# -------------------------------------------------

# collections - collections-named-tuple
import collections

n, columns = (int(input()), input().split())
Grade = collections.namedtuple('Grade', columns)
marks = [int(Grade(*input().split()).MARKS) for _ in range(n)]
print((sum(marks) / len(marks)))
# -------------------------------------------------

# collections - collections-ordered-dict
import collections


n = int(input())

prices = collections.OrderedDict()

for i in range(n):
    line = input().split()
    cost = int(line[len(line) - 1])
    name = ' '.join(line[0:len(line) - 1])
    if name in prices:
        prices[name] += cost
    else:
        prices[name] = cost


for key in prices:
    print(key, prices[key])
# -------------------------------------------------

# collections - company-logo
import collections

if __name__ == '__main__':
    s = input()

    s = sorted(s)
    
    FREQUENCY = Counter(list(s))
    
    # using for loop to print the three words with frequency
    for k, v in FREQUENCY.most_common(3):
        print(k, v)
# -------------------------------------------------

# collections - default-dict-tutorial
import collections


n, m = map(int, input().split())
frequencies = collections.defaultdict(list)

for i in range(n):
    word = input()
    frequencies[word].append(i + 1)

for _ in range(m):
    word = input()
    if len(frequencies[word]) > 0:
        print(' '.join(map(str, frequencies[word])))
    else:
        print(-1)
# -------------------------------------------------

# collections - piling-up
for t in range(int(input())):
    l = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < l - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < l - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == l - 1 else 'No')
# -------------------------------------------------

# collections - word-order
import collections

frequencies = collections.OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print(len(frequencies))

for word in frequencies:
    print(frequencies[word], end=' ')
# -------------------------------------------------



#DATE AND TIME
# date-and-time - calendar-module
import datetime

month, date, year = map(int, input().split())
date = datetime.datetime(year=year, month=month, day=date)
print(date.strftime('%A').upper())
# -------------------------------------------------

# date-and-time - time-delta
import datetime

date_format = '%a %d %b %Y %X %z'
queries = int(input())

for _ in range(queries):
    date1 = datetime.datetime.strptime(input(), date_format)
    date2 = datetime.datetime.strptime(input(), date_format)
    diff = int(abs((date2 - date1).total_seconds()))
    print(diff)
# -------------------------------------------------



#EXCEPTIONS
# exceptions - errors-and-exceptions
def take_input():
    try:
        a, b = list(map(int, input().split()))
        print(a // b)
    except ZeroDivisionError as error:
        print('Error Code:', error)
    except ValueError as error:
        print('Error Code:', error)


n = int(input())
for _ in range(n):
    take_input()
# -------------------------------------------------



#BUILT-INS
# builsin - zipped
N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
# -------------------------------------------------

# builsin - Athlete-Sort
if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)
# -------------------------------------------------

# builsin - ginortS
s = input()
print(
    "".join(
        sorted(
            s,
            key=lambda x: (
                x.isdigit() and int(x) % 2 == 0,
                x.isdigit(),
                x.isupper(),
                x.islower(),
                x,
            ),
        )
    )
)
# -------------------------------------------------



#PYTHON FUNCTIONALS 
# python functionals - map-and-lambda-expressions
cube = lambda x: x ** 3


def fibonacci(n):
    List = [0, 1]
    for i in range(2, n):
        List.append(List[i-1] + List[i-2])
        
    return(List[0:n])


if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))
# -------------------------------------------------



#REGEX AND PARSING CHALLENGES
# regex and parsing - detect-floating-point-numbers
import re

pattern = '([+|-]){0,1}(\d)*[.](\d)+'


def is_float(number):
    try:
        float(number)
        info = re.match(pattern, number)
        return info is not None and info.span() == (0, len(number))
    except ValueError as _:
        return False


queries = int(input())
for _ in range(queries):
    number = input()
    print(is_float(number))
# -------------------------------------------------

# regex and parsing - detect-html-tags-attributes
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attribute in attrs:
            print('-> {} > {}'.format(*attribute))


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()
# -------------------------------------------------

# regex and parsing - group-groups-groupdict
import re

pattern = r'([a-zA-Z0-9])\1+'
match = re.search(pattern, input().strip())
print(match.groups()[0] if match else -1)
# -------------------------------------------------

# regex and parsing - hex-color-code
import re

hex_color = r'(?<!^)#([0-9a-fA-F]{3}){1,2}'

N = int(input())
for _ in range(N):
    line = input()
    for elem in re.finditer(hex_color, line):
        print(line[elem.start(): elem.end()] if elem is not None else '')
# -------------------------------------------------

# regex and parsing - html-parser-part-1
from html.parser import HTMLParser


# regex and parsing - create a subclass and override the handler methods
from html.parser import HTMLParser

N = int(input())
class MyHTMLParser(HTMLParser): # Subclass
    
    def handle_starttag(self, tag, attributes):
        print('Start :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attributes):
        print('Empty :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
Parser = MyHTMLParser()
Parser.feed(''.join([input().strip() for i in range(0, N)]))
# -------------------------------------------------

# regex and parsing - html-parser-part-2
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line > 1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


parser = CustomHTMLParser()

n = int(input())
html_string = ''
for i in range(n):
    html_string += input().rstrip() + '\n'

parser.feed(html_string)
# -------------------------------------------------

# regex and parsing - matrix-script
import re

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())

string = ''
for elem in zip(*data):
    string += ''.join(elem)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', string))
# -------------------------------------------------

# regex and parsing - re-findall-and-finditer
import re

consonants = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall("(?<=" + consonants + ")([aeiou]{2,})" + consonants, input(), re.I)
print('\n'.join(a or ['-1']))
# -------------------------------------------------

# regex and parsing - re-split
import re

regex_pattern = r"[.]|,"  # Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))
# -------------------------------------------------

# regex and parsing - re-start-end
import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)
# -------------------------------------------------

# regex and parsing - regex-substitution
import re

and_pattern = r' [&]{2}(?= )'
and_replacement = ' and'
or_pattern = r' [|]{2}(?= )'
or_replacement = ' or'

N = int(input())
for _ in range(N):
    string = input()
    string = re.sub(and_pattern, and_replacement, string)
    string = re.sub(or_pattern, or_replacement, string)
    print(string)
# -------------------------------------------------

# regex and parsing - validating-credit-card-numbers
import re

pattern_start = r'^'
pattern_no_repetition = r'(?!.*(\d)(-?\1){3})'
credit_card_pattern = r'[456]((\d){15}|(\d){3}(-[\d]{4}){3})'
pattern_end = r'$'

pattern = re.compile(
    pattern_start
    + pattern_no_repetition
    + credit_card_pattern
    + pattern_end
)

for _ in range(int(input())):
    credit_card = input()
    print("Valid" if pattern.search(credit_card) else 'Invalid')
# -------------------------------------------------

# regex and parsing - validating-parsing-email-address
import email.utils
import re

email_pattern = r'([a-zA-Z](\w|\d|_|-|[.])*)@([a-zA-Z])*[.]([a-zA-Z]{1,3})'


def is_valid_email_address(person):
    email = person[1]
    return re.fullmatch(email_pattern, email) is not None


people = []
n = int(input())
for _ in range(n):
    line = input()
    people.append(email.utils.parseaddr(line))

for element in (filter(is_valid_email_address, people)):
    print(email.utils.formataddr(element))
# -------------------------------------------------

# regex and parsing - validating-phone-numbers
import re
import email.utils 

N = int(input())

pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(0, N):
    parsed_addr = email.utils.parseaddr(input())
    if re.search(pattern, parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr)) 

# -------------------------------------------------

# regex and parsing - validating-postal-codes
regex_integer_in_range = r'^[1-9][\d]{5}$'  
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
# -------------------------------------------------

# regex and parsing - validating-roman-numerals
regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'

import re
print(str(bool(re.match(regex_pattern, input()))))
# -------------------------------------------------

# regex and parsing - validating-uid
import re

pattern_2_upper_case = r'[A-Z]{2}'
pattern_3_digits = r'(\d){3}'
pattern_alphanum = r'[0-9a-zA-Z]{10}'
pattern_has_repitions = r'^.*(.).*\1.*$'

for _ in range(int(input())):
    uid = ''.join(sorted(input()))
    try:
        assert re.search(pattern_2_upper_case, uid)
        assert re.search(pattern_3_digits, uid)
        assert re.search(pattern_alphanum, uid)
        assert not re.search(pattern_has_repitions, uid)
        assert len(uid) == 10
        print("Valid")
    except:
        print('Invalid')
# -------------------------------------------------



#XML
# xml - xml-1-find-the-score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.items()) + sum([get_attr_number(x) for x in node])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
# -------------------------------------------------

# xml - xml-2-find-max-depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    
    if level > maxdepth:
        maxdepth = level
    for x in elem:
        depth(x, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
# -------------------------------------------------



#CLOSURES AND DECORATIONS
# closures-and-decorators - decorator-2-name-directory
import operator

def person_lister(f):
    def inner(people):
         return map(f, sorted(people, key=lambda x: int(x[2])))

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
# -------------------------------------------------

# closures-and-decorators - standardize-mobile-numbers-using-decorator
def wrapper(f):
    def fun(l):
      
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
# -------------------------------------------------



#NUMPY
# numpy-python - array-mathematics
import numpy

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
A = numpy.array(A)

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))
B = numpy.array(B)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
# -------------------------------------------------

# numpy-python - arrays
import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
# -------------------------------------------------

# numpy-python - concatenate
import numpy

N, M, P = map(int, input().split())

data1 = []
for _ in range(N):
    data1.append(list(map(int, input().split())))

data2 = []
for _ in range(M):
    data2.append(list(map(int, input().split())))

result = numpy.concatenate((data1, data2), axis=0)
print(result)
# -------------------------------------------------

# numpy-python - dot-cross
import numpy
numpy.set_printoptions(legacy='1.13')


def zero(size):
    return [0 for _ in range(size)]


def get_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(list(map(int, input().split())))
    return matrix


N = int(input())
matrix1 = numpy.array(get_matrix(N))
matrix2 = numpy.array(get_matrix(N)).transpose()

result = []
for row in range(N):
    result.append(zero(N))
    for column in range(N):
        result[row][column] = int(numpy.dot(matrix1[row], matrix2[column]))

print(numpy.array(result))
# -------------------------------------------------

# numpy-python - eye-and-identity
import numpy

M, N = map(int, input().split())

print(str(numpy.eye(M, N)).replace('1',' 1').replace('0',' 0'))
# -------------------------------------------------

# numpy-python - flatten-and-transpose
import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
print(data.transpose())
print(data.flatten())
# -------------------------------------------------

# numpy-python - floor-ciel-and-rint
import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(list(map(float, input().split())), dtype=float)
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
# -------------------------------------------------

# numpy-python - inner-outer
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
# -------------------------------------------------

# numpy-python - linear-algebra
import numpy

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(float, input().split())))

result = round(numpy.linalg.det(matrix), 2)
print(result)
# -------------------------------------------------

# numpy-python - mean-var-std
import numpy

N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for n in range(N)])

print(numpy.mean(A, axis = 1))
print(numpy.var(A, axis = 0))
print(numpy.round(numpy.std(A), 11))
# -------------------------------------------------

# numpy-python - min-max
import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
data = data.min(axis=1)
result = data.max()
print(result)
# -------------------------------------------------

# numpy-python - polynomials
import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = list(map(float, input().split()))
x = float(input())
value = numpy.polyval(polynomial, x)
print(value)
# -------------------------------------------------

# numpy-python - shape-and-reshape
import numpy as np

array = np.array(list(map(int, input().split())))
array.shape = (3, 3)
print(array)
# -------------------------------------------------

# numpy-python - sum-and-prod
import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
data = data.sum(axis=0)
product = data.prod()
print(product)
# -------------------------------------------------

# numpy-python - zeroes-and-ones
import numpy

N = tuple(map(int, input().split()))
print(numpy.zeros(N, int))
print(numpy.ones(N, int))
# -------------------------------------------------



#PROBLEM 2
# problem 2 - birthday-cake-candles
import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    
    count=0
    big = max(ar)
    for i in range(len(ar)):
        if(ar[i]==big):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
# -------------------------------------------------

# problem 2 - Number Line Jumps
import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    
    if x1 < x2 and v1 < v2:
        return 'NO'
    else:
        if v1!=v2 and (x2-x1)%(v2-v1)==0:
            return 'YES' 
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
# -------------------------------------------------

# problem 2 - Viral Advertising
import math
import os
import random
import re
import sys


def viralAdvertising(n):
    
    shared =5
    cumulative=0
    for i in range(1,n+1):
        liked = shared//2
        cumulative+=liked
        shared = liked*3
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
# -------------------------------------------------

# problem 2 - Recursive Digit Sum
import math
import os
import random
import re
import sys


def superDigit(n, k):
    n = sum([int(n[i]) for i in range(len(n))]) * k
    return superDigit(str(n), 1) if n > 9 else n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
# -------------------------------------------------

# problem 2 - Insertion Sort-pt1
import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    tmp = arr[-1]
    for i in range(n-2, -1, -1):
        
        if arr[i] > tmp:
            arr[i+1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            arr[i+1] = tmp
            print(' '.join(map(str, arr)))
            return

    arr[0] = tmp
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
# -------------------------------------------------

# problem 2 - Insertion Sort-pt2
import math
import os
import random
import re
import sys


def insertionSort2(n, arr):

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            if i == n-1:
                arr = sorted(arr)
                print(*arr)
            else:
                arr[:i+1] = sorted(arr[:i+1])
                print(*arr)
        else:
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
# -------------------------------------------------