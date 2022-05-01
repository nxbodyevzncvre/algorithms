def string_clean(s):
    string_1 = s
    new_string = ''.join((x for x in string_1 if not x.isdigit()))
    return new_string


string_clean("Wh7y can't we3 bu1y the goo0d software3? #cheapskates3")
