def hanoi(disks, source, auxiliary, target):
    if disks == 1:
        print('Move disk 1 from peg{} to peg{}.'.format(source, target))
        return
    hanoi(disks - 1, source, target, auxiliary)
    print('Moves disk{} from peg{} to peg{}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)

disks = int(input('Enter number of disks:'))
hanoi(disks, 'A', 'B', 'C')

a = int(input('Enter a number:'))
b = int(input('Enter a number:'))
maximum = lambda a, b: a if a > b else b
print(f'{maximum(a, b)} is the maximum number')
