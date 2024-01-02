"""
Lesson 017
"""
import requests


def tokenizer(target, prefix, suffix):
    """
    returns all tokens that start with prefix and end with suffix
    """
    lst = []
    while True:
        if prefix in target and suffix in target:
            target = target[target.find(prefix) :]
            lst.append(target[: target.find(suffix) + len(suffix)])
            target = target[target.find(suffix[-1]) :]
        else:
            break
    # print(lst)
    return lst


def get_url_list(url):
    """
    returns a list of all urls in the url that are only referenced as hrefs
    """
    lst = []
    response = requests.get(url, timeout=100)
    response_list = [i for i in response.text.split("\n") if "href" in i]
    for i in response_list:
        # prefix = i[i.find("href")+6:i.find("href")+10]
        prefix = "http"
        r = tokenizer(i, prefix, '"')
        for j in r:
            lst.append(j[:-1])
    print(lst)
    return lst


def infix_to_postfix(infix_expression: str):
    """
    converts and returns the infix expression to postfix
    """
    precd = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0, ")": 0}
    result = []
    stack = []
    eqn = infix_expression.split()
    for i in eqn:
        if i not in precd:
            result.append(i)
        elif i == "(":
            stack.append(i)
            continue
        elif i == ")":
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
            continue
        else:
            if not stack:
                stack.append(i)
            else:
                while stack and precd[i] <= precd[stack[-1]]:
                    result.append(stack.pop())
                stack.append(i)
    while stack:
        result.append(stack.pop())
    print(result)
    return result


# infix_to_postfix("a + b * ( c + d ) ")
# print(tokenizer('arrarrarararara', 'r', 'a'))
# get_url_list("https://httpbin.org/")
