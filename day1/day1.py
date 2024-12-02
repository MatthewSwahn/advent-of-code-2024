
def main():
    data = open('day1\day1.txt', 'r').read().split('\n')
    
    l1 = list()
    l2 = list()
    for x in data:
        l1.append(int(x.split()[0]))
        l2.append(int(x.split()[1]))
        
    l1.sort()
    l2.sort()

    diff= [abs(l1 -l2) for l1, l2 in zip(l1,l2)]

    print(sum(diff))

if __name__=='__main__':
    main()