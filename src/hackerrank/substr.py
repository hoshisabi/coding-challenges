def count_substring(string, sub_string):
    cnt = 0
    for i in range(0, len(string)):
        sl = string[i: i + len(sub_string)]
        if sub_string == sl:
            cnt += 1
    return cnt

print(count_substring("ABCDCDC", "CDC"))