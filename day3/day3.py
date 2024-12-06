import re


def main():
    data_raw = open('day3\day3.txt', 'r').read()
    
    # id valid inputs
    mults_raw = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data_raw)
    
    # parse numbers from inputs
    results = list()
    for mul in mults_raw:
        # extract ints from mul line
        nums = [int(x) for x in re.findall(r'\d+', mul)]
        # multiply numbers
        results.append(nums[0] * nums[1])
    
    print(sum(results))
    
        
if __name__=='__main__':
    main()