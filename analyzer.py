# 2023-05-25T13:28,GET,/list
# 2023-05-25T13:28,GET,/search
# >>> number_of_requests("output.log","list")
def find_number_of_requests(filename: str, request: str) -> int:
    with open(filename) as the_file:
        return count_number_of_requests_in_string(the_file, request)
"""
lines = "2023-05-25T13:28,GET,/list
2023-05-25T13:28,GET,/search"
assert count_number_of_requests_in_string(lines, "/list") == 1
"""
def count_number_of_requests_in_string(lines, request) -> int:
    lines = split_file_in_tokens(lines)
    return count_number_of_requests(lines, request)

"""
lines = ["2023-05-25T13:28,GET,/list",
"2023-05-25T13:28,GET,/search"]
expected = [
    ["2023-05-25T13:28", "GET", "/list"],
    ["2023-05-25T13:28", "Post", "/search"] ]
result = split_file_in_tokens(lines, "/list")
assert result == expected
"""
def split_file_in_tokens(lines:list) -> list:
    return map(split_line_in_tokens, lines)
"""
line = "2023-05-25T13:28,GET,/list"
assert split_line_in_tokens(line) == ["2023-05-25T13:28", "GET", "/list" ]
"""
def split_line_in_tokens(line: str) -> tuple:
    tokens = line.split(",")
    return tuple(tokens)

# lines [
#    ("123", "GET","/list"),
#    ("123", "POST","/search")
# ]
# count_number_of_requests(lines, "/list")

def count_number_of_requests(lines, request):
    result = 0
    for tokens in lines:
        if(has_request_in_tuple(request, tokens)):
            result += 1
    return result

def has_request_in_tuple(request:str, tokens:tuple) -> bool:
    size = len(tokens)
    if size == 0:
        return False
    return tokens [size - 1] == request