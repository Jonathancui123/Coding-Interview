#Implement an algorithm to print all valid combinations of N pairs of parentheses
def printParentheses(N):
    start = ["()"]
    if (N==0):
        return
    elif (N==1):
        print("()")
        return

    list = recurse(N-1, start)
    for solution in list:
        print(solution)
    return

def isRepeat(string):
    build = ["()"] * (len(string)//2)
    check = "".join(build)
    if string == check:
        return True
    else:
        return False

def recurse(N, current):
    #Base case: N is zero
    #Current is a list of all current strings
    if (N == 0):
        return current;
    else:
        new = []
        for solution in current:
            new.append(solution + "()")
            new.append("("+solution+")")
            if (not isRepeat(solution)):
                new.append("()" + solution)
        return recurse(N-1, new)

N = int(input("give number"))
printParentheses(N)