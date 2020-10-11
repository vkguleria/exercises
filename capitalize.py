# Complete the solve function below.
# input a string and it'll capitalize the initial letter of words found in the string
# input sample "Hi there 3g   v3inod Vinod ji"
#
import re
def solve(s):
    def do_capitalize(m):
        return m.group(0).capitalize()
    return re.sub(r'\w+',do_capitalize,s)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)

