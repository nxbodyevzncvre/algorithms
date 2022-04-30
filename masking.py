def maskify(cc):
    cc = cc
    size = len(cc)
    replacement = "####"
    if size > 4:
        cc = "#" * (size - 4) + cc[-4:]
    elif not size:
        cc = ''
    else:
        cc = cc
    print(cc)
