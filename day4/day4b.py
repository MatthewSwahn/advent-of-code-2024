import numpy as np

def get_val2d(in_arr:list, ind_x:int, ind_y:int):
    if ind_x <0 or ind_y<0:
        return ''
    try:
        val = in_arr[ind_y][ind_x]
        return val
    except IndexError:
        return ''

def x_check(in_list:list, ind_x:int, ind_y:int):
    w1 = get_val2d(in_list, ind_x, ind_y) + get_val2d(in_list, ind_x+1, ind_y+1) + get_val2d(in_list, ind_x+2, ind_y+2)
    w2 = get_val2d(in_list, ind_x+2, ind_y) + get_val2d(in_list, ind_x+1, ind_y+1) + get_val2d(in_list, ind_x, ind_y+2)
    return w1 in {'MAS', 'SAM'} and w2 in {'MAS', 'SAM'}

def main():
    with open('day4\\day4.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
    
    data_arr = np.array([list(line) for line in lines])
    
    checks = list()
    for yi, row in enumerate(data_arr):
        for xi, value in enumerate(row):
            checks.append(x_check(data_arr, xi, yi))
        
    print(sum(checks))
        
        
if __name__=='__main__':
    main()