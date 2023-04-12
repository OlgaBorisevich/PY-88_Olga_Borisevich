def create_list():

    x = False
    # print(int(not (x)))

    # print(str(int(not (x))) + str(int(x)))

    return [int(x), int(not (x)), int(str(int(not (x))) + str(int(x)))]
print(create_list())