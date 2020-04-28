from math import sqrt

class Sudoku:
    def __init__(self,repr):
        super().__init__()
        self.repr = repr
        self.num = len(self.repr)
        self.search_space = self.create_search_space()


    def create_search_space(self):
        search_space = []
        for _ in range(self.num):
            a = []
            for __ in range(self.num):
                a.append(list(range(1,self.num+1)))
            search_space.append(a)

        return search_space


    def check(self, val,row, column):
        if val in self.repr[row] or val in list(zip(*self.repr))[column]:
            return False

        sub_matrix = int(sqrt(self.num))
        r,c = row//sub_matrix * sub_matrix , column  // sub_matrix * sub_matrix

        for i in range(sub_matrix):
               for j in range(sub_matrix):
                    if val == self.repr[r+i][c+j]:
                        return False
                    else: continue

        else:
            return True


    def add_value(self,row,column):
        if self.repr[row][column] == 0:
            for val in self.search_space[row][column]:
                if self.check(val,row,column):
                    self.repr[row][column] = val
                    break


    def __repr__(self):
        
        sub_matrix = int(sqrt(self.num))
        for row in range(self.num):
            for column in range(self.num):
                print(self.repr[row][column], end=" ")
                if column % sub_matrix == 2:
                    print("\t",end="")
            print()
            if row%sub_matrix ==2:
                print()
        
        return ""
  