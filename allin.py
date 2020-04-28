representation = [[0, 0, 0, 2],
                  [0, 2, 0, 4],
                  [3, 0, 0, 0],
                  [1, 0, 0, 0]]

numbers = [1, 2, 3, 4]

# ku bohet dfs edhe backtracking ka nevoje per permiresim
def vendos_numrin(rreshti, kolona):
    if rreshti == 4:
        return True

    for i in range(0, len(representation)):
        for j in range(0, len(representation[rreshti])):
            if representation[rreshti][kolona] == 0:
                if check_no(i, j):
                    if kolona < 9:
                        if vendos_numrin(rreshti, kolona + 1):
                            return True
                    else:
                        if vendos_numrin(rreshti + 1, 0):
                            return True
                representation[rreshti][kolona] = 0
        return False
    return True

# tries every number in the given coordinate
def check_no(rreshti, kolona):
    print("\n\n")
    for i, val in enumerate(representation):
        print('\n ------------------')
        for j, valZ in enumerate(representation[i]):
            print('|', representation[i][j], '|', end='')
    for num in numbers:
        search_space = []
        # if representation[pozita[0]][pozita[1]] == 0:
        for i in range(0, 2):
            for j in range(0, 2):
                search_space.append(representation[rreshti // 2 + i][kolona // 2 + j])

        if (num not in representation[rreshti]
                and num not in [col[rreshti] for col in representation]
                and num not in search_space):
            representation[rreshti][kolona] = num
            return True
    return False


def main():
    if vendos_numrin(0, 0):
        for i, val in enumerate(representation):
            print('\n ------------------')
            for j, valZ in enumerate(representation[i]):
                print('|', representation[i][j], '|', end='')
    else:
        print('nuk ka zgjidhje, po rrej se e kom gabim')


# if vendosNumrin((0,0)):

# def main():
#     for i, val in enumerate(representation):
#         print('\n ------------------')
#         for j, valZ in enumerate(representation[i]):
#             print('|', representation[i][j], '|', end='')


main()
# place_no(0, 0)
# print('\n-------------------')
# main()
