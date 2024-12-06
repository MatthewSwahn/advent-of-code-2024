import numpy as np

def get_val2d(in_arr:list, ind_x:int, ind_y:int):
    if ind_x <0 or ind_y<0:
        return ''
    try:
        val = in_arr[ind_y][ind_x]
        return val
    except IndexError:
        return ''

def v_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x, ind_y+1) == 'M'
    a = get_val2d(in_list, ind_x, ind_y+2) == 'A'
    s = get_val2d(in_list, ind_x, ind_y+3) == 'S'
    return x and m and a and s

def h_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x+1, ind_y) == 'M'
    a = get_val2d(in_list, ind_x+2, ind_y) == 'A'
    s = get_val2d(in_list, ind_x+3, ind_y) == 'S'
    return x and m and a and s

def v_check_inv(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x, ind_y-1) == 'M'
    a = get_val2d(in_list, ind_x, ind_y-2) == 'A'
    s = get_val2d(in_list, ind_x, ind_y-3) == 'S'
    return x and m and a and s

def h_check_inv(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x-1, ind_y) == 'M'
    a = get_val2d(in_list, ind_x-2, ind_y) == 'A'
    s = get_val2d(in_list, ind_x-3, ind_y) == 'S'
    return x and m and a and s

def d19_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x+1, ind_y-1) == 'M'
    a = get_val2d(in_list, ind_x+2, ind_y-2) == 'A'
    s = get_val2d(in_list, ind_x+3, ind_y-3) == 'S'
    return x and m and a and s

def d91_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x-1, ind_y+1) == 'M'
    a = get_val2d(in_list, ind_x-2, ind_y+2) == 'A'
    s = get_val2d(in_list, ind_x-3, ind_y+3) == 'S'
    return x and m and a and s

def d73_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x+1, ind_y+1) == 'M'
    a = get_val2d(in_list, ind_x+2, ind_y+2) == 'A'
    s = get_val2d(in_list, ind_x+3, ind_y+3) == 'S'
    return x and m and a and s

def d37_check(in_list:list, ind_x:int, ind_y:int):
    x = get_val2d(in_list, ind_x, ind_y) == 'X'
    m = get_val2d(in_list, ind_x-1, ind_y-1) == 'M'
    a = get_val2d(in_list, ind_x-2, ind_y-2) == 'A'
    s = get_val2d(in_list, ind_x-3, ind_y-3) == 'S'
    return x and m and a and s


def main():
    with open('day4\\day4.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
    
    data_arr = np.array([list(line) for line in lines])
    
    checks = list()
    for yi, row in enumerate(data_arr):
        for xi, value in enumerate(row):
            # vert checks
            checks.append(v_check(data_arr, xi, yi))
            checks.append(v_check_inv(data_arr, xi, yi))
            
            # hori checks
            checks.append(h_check(data_arr, xi, yi))
            checks.append(h_check_inv(data_arr, xi, yi))
            
            # diag checks
            checks.append(d19_check(data_arr, xi, yi))
            checks.append(d73_check(data_arr, xi, yi))
            checks.append(d37_check(data_arr, xi, yi))
            checks.append(d91_check(data_arr, xi, yi))
            
    print(sum(checks))
        
        
if __name__=='__main__':
    main()