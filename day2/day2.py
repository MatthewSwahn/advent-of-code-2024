import numpy as np

def is_monotone(in_data:list):
    data_diff = np.diff(np.array(in_data))
    return np.all(data_diff > 0) or np.all(data_diff<0)

def safe_change(in_data:list):
    data_diff = np.diff(np.array(in_data))
    return np.all(np.abs(data_diff) <=3) and np.all(np.abs(data_diff) >=1)


def main():
    data_raw = open('day2\day2.txt', 'r').read().split('\n')
    data = list()
    results = list()
    for x in data_raw:
        row = [int(xi) for xi in x.split()]
        monotone_ind = is_monotone(row)
        safe_change_ind = safe_change(row)
        results.append(monotone_ind and safe_change_ind)
        data.append(row)
    
    print(sum(results))
        
if __name__=='__main__':
    main()