import sys, os
import re

sys.path.append("..")
from funcs.readfile import ReadFileObject 

# TO DO
class TOBEDEFINE:
    def __init__(self) -> None:
        # TO DO
        pass

    def to_be_define(self) -> None:
        # TO DO
        pass

if __name__ == "__main__":
    mode = "test" #"part2", "test"

    if mode == "test":
        # TO DO
        res_test1 = {0: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 1: {0: 'X', 1: 'X', 2: 'X', 3: '*', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 2: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 3: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: '#', 7: 'X', 8: 'X', 9: 'X'}, 4: {0: 'X', 1: 'X', 2: 'X', 3: '*', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 5: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: '+', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 6: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 7: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 8: {0: 'X', 1: 'X', 2: 'X', 3: '$', 4: 'X', 5: '*', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}, 9: {0: 'X', 1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'}}
     
        test_obj = TOBEDEFINE()
        unittest_dataprocessing = { 
            'test_1': res_test1 == test_obj.to_be_define()
            }
        for k, v in unittest_dataprocessing.items():
            print(f'{k}: {"passed" if v else "failed"}')

    else:
        # TO DO
        filepath = os.path.join(os.path.dirname(__file__), 'puzzle-day-TODO-input.txt')
        lines = ReadFileObject().get_lines_from_file(filepath)
        
        if lines[0]:
            func_obj = TOBEDEFINE(lines[1])
            # TO DO

            if mode == "part1": 
                # TO DO
                print(f'Total number is {sum}')

            if mode == "part2":
                # TO DO
                print(f'Total number is {sum}')

        else:
            print("Error when opening file!")
        
    