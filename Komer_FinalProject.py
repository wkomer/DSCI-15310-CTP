# William Komer
# CTP Final Project

#==== Setup ====#

# The way that I am setting this up is as if you are getting into a battle with
# a wild pokemon, You have to choose the 
choice = ('')
track =0
#==== Input Start ====#

print('A Wild Pichu Appears.')
print('')
print('You Need to Choose what to do:')
print('')
pichu = bool(True)
while pichu == True:
    print('1: Check Pokedex type Dex')
    print('2: Pick your Pokemon type Poke')
    print('3: Run Away type Run')
    print('')
    ans = input('What Will you Do ')
#used to check that the correct answer was inputed into.
    if ans=='Run':
        print('Can Not Run Away')
 #       ans = 'Poke'
        print('')
    
    if ans =='Dex':
        print('Your PokeDex Opens and Reads Out:')
        print('')
        print('Tiny Mouse Pokemon:')
        print('Type: Electric')
        print('Weakness to Ground Type Pokemon')
        print('')
        print('*Pokedex Shuts Down*')
        print('')

    if ans =='Poke':
        print('You have Four Pokemon to choose from')
        print('')
        print('1: Chikorita- Grass Type')
        print('2: Cyndiquil- Fire Type')
        print('3: Totodile - Water Type')
        print('4: Cubone - Ground Type')
        print ('')
        choice = input(' Which Will You Choose? ')

        print(choice)

#==== MOVE AREA ====#
        while pichu == True:
            if choice == 'Chikorita':
                print('Moves: ')
                print('1: Tackle')
                print('2: Razor Leaf')
                print('3: Growl')
                print('4: Poison Powder')
                move = input('Which Move Will You Choose?')
                print('')

            if choice =='Cyndiquil':
                print('Moves:')
                print('1: Tackle')
                print('2: Leer')
                print('3: Smokescreen')
                print('4: Ember')
                move = input('Which Move Will You Choose?')
                print('')
            if choice =='Totodile':
                print('Moves:')
                print('1: Scratch')
                print('2: Leer')
                print('3: Water Gun')
                print('4: Rage')
                move= input('Which Move Will You Choose?')
                print('')
            if choice =='Cubone':
                print('Moves:')
                print('1: Growl')
                print('2: Tail Whip')
                print('3: Bone Club')
                print('4: Headbutt')
                move=input('Which Move Will You Choose?')
    
#==== Battle Area ====#
                if track == 1:
                    print('Pichu Used Charm')
                    print(choice,'used',move)
                    print('Pichu Fainted')
                    pichu = False
                if track==0:
                    print('Pichu Used Thundershock')
                    print( choice,'used ', end = move)
                    print('')
                    track = track+1
            
print('Pichu is Fainted, You won the Battle!!!')
    
