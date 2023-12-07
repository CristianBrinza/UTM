class PermutationHandler:
    def __init__(self):
        self.pc_1 = [
            [57, 49, 41, 33, 25, 17, 9],
            [1, 58, 50, 42, 34, 26, 18],
            [10, 2, 59, 51, 43, 35, 27],
            [19, 11, 3, 60, 52, 44, 36],
            [63, 55, 47, 39, 31, 23, 15],
            [7, 62, 54, 46, 38, 30, 22],
            [14, 6, 61, 53, 45, 37, 29],
            [21, 13, 5, 28, 20, 12, 4]
        ]

    def get(self):
        return self.pc_1
    
    def get_permuted(self, bit_stream):
        permuted_key = ''
        for entry in self.pc_1:
            for index in entry:
                permuted_key += bit_stream[index - 1]
        return permuted_key
    
    def print_pc_1(self):
        for entry in self.pc_1:
            row = ''
            for index in entry:
                str_index = str(index)
                row += str(index) + (4 - len(str_index)) * ' '
            print(row)
            
        