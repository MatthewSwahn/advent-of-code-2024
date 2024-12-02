
def counter(count_me:list):
    result = dict()
    for x in count_me:
        if x in result:
            result[x] = result[x]+1
        else:
            result[x] = 1
    return result

def main():
    data = open('day1\day1.txt', 'r').read().split('\n')
    l1 = list()
    l2 = list()
    for x in data:
        l1.append(int(x.split()[0]))
        l2.append(int(x.split()[1]))
        
    id_counter = counter(l2)
    diff= list()
    for item1 in l1:
        #item_diff = abs(item1-item2)
        mult = id_counter.get(item1)
        if mult:
            diff.append(item1 * mult)
    
    print(sum(diff))

if __name__=='__main__':
    main()