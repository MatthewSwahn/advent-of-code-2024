import re


def main():
    data_raw = open('day3\day3.txt', 'r').read()
    
    # id only "do" values from data
    dos = re.split(r"do\(\)", data_raw)
    
    results = list()
    for d in dos:
        # ignore values that have "don'ts" in front
        dnt_split = re.split(r"don't\(\)", d)
        mul_do = dnt_split[0]
        
        # id valid inputs
        mults = re.findall(r'mul\(\d{1,3},\d{1,3}\)', mul_do)
        
        # parse numbers from inputs
        for mul in mults:
            # extract ints from mul line
            nums = [int(x) for x in re.findall(r'\d+', mul)]
            # multiply numbers
            results.append(nums[0] * nums[1])
    
    print(sum(results))    
    
        
if __name__=='__main__':
    main()
