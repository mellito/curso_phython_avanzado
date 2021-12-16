# [1,1,2,2,4] -> [1,2,4]

def remuve_duplicate(some_list):
    # without_duplicate = []
    # for element in some_list:
    #     if element not in without_duplicate:
    #         without_duplicate.append(element)
    # return without_duplicate
    set_list = set(some_list)

def main():

    # random_list =[1,1,2,2,4]
    # set_list = lambda setlist : set(setlist)
    # print(set_list(random_list))

    random_list =[1,1,2,2,4]
    print(remuve_duplicate(random_list))

if __name__ == '__main__':
    main()