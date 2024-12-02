import numpy as np

def is_monotone(in_data:np.array):
    data_diff = np.diff(in_data)
    return np.all(data_diff > 0) or np.all(data_diff<0)

def safe_change(in_data:np.array):
    data_diff = np.diff(in_data)
    return np.all(np.abs(data_diff) <=3) and np.all(np.abs(data_diff) >=1)

def assess_list(in_data:np.array):
    return is_monotone(in_data) and safe_change(in_data)

def dampener_assess(in_data:np.array):
    for i in np.arange(len(in_data)):
        new_data = np.delete(in_data, i)
        res = assess_list(new_data)
        if res:
            return res
    return assess_list(in_data)

def main():
    data_raw = open('day2\day2.txt', 'r').read().split('\n')
    data = list()
    results = list()
    for x in data_raw:
        row = np.array([int(xi) for xi in x.split()])
        results.append(dampener_assess(row))
        data.append(row)
        
    print(sum(results))
        
if __name__=='__main__':
    main()