# William Komer
# CTP Assignment 5- Shapes

#==== Input =====#
size = input('What Size?')
size = int(size)
char=input('what character?')
print('')



#===== Square =====#
row = 1
while row <= size:
 # Output a row
 col = 1
 while col <= size:
   # Output a single character, note the comma
   print(char, '', end='')
   col = col + 1
 # Output an empty string followed by an enter/return
 print('')
 row = row + 1
print('')

#===== Triangle =====#
row = 1
while row <= size:
    # Output a single row
    col = 1
    while col <= row:
        # Output the drawing character
        print(char, '', end = '')

        # The next column number
        col = col + 1

    # Output a newline to end the row
    print('')

    # The next row number
    row = row + 1
print('')

#===== Diagonal =====#
row = 1
while row <= size:
    # Output a single row
    col = 1
    
    # Output a newline to end the row
    print(char)
    
    while col <= row:
        # Output the drawing character
        print(' ', end = ' ')

        # The next column number
        col = col + 1

    # The next row number
    row = row + 1
print('')

#===== Reverse Triangle =====#
row = 1
while row <= size:
    # Output a single row
    col = size
    track =int(0)
    zero = int(0)
    while col>=row:
        while col > row:
        # Output the drawing character
            print(' ', '', end = '')
            col=col-1
        if col == row:
            track = col
            #print(char)
            while track>zero:
                print(char,'',end='')
                track = track - 1
            # The next column number
        col = col - 1        
        
    # The next row number
    row = row + 1
    print('')
print('')


#===== Centered Triangle =====#
row = 1
while row <= size:
    # Output a single row
    col = size
    track =int(0)
    zero = int(0)
    while col>=row:
        while col > row:
        # Output the drawing character
            print('', '', end = '')
            col=col-1
        if col == row:
            track = col
            #print(char)
            while track>zero:
                print(char,'',end='')
                track = track - 1
            # The next column number
        col = col - 1        
        
    # The next row number
    row = row + 1
    print('')
