if __name__ == '__main__':
    s = "qA2"

    print(any(c.isalnum for c in list(s)))
    print(any(c.isalpha for c in list(s)))
    print(any(c.isdigit for c in list(s)))
    print(any(c.islower for c in list(s)))
    print(any(c.isupper for c in list(s)))
