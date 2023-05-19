ckeck = '[(5+z)*6-y]+{-1*3-(2+x)}'
lst = { '[':'a', ']':'A',  '(':'b',  ')':'B',  '{':'c', '}':'C' }

arr = [ lst[el] for el in ckeck if el in lst.keys() ]


flag = 0 
while True:
    i = 2
    if arr == [] :
        print('expretion is ok')
        break
    else:
        while True:
            n = int(i/2)
            if n > len(arr):
                flag = 1
                break
            first = arr[:n]
            last  = arr[n:i]

            if ''.join(first).lower() == ''.join(last[::-1]).swapcase() and first != []:
                arr = arr[i:]
                print(arr)
                break
            i += 2
        if flag == 1 :
            print('expretion is NOT ok')
            break