import os,time,sys
clear = lambda: os.system('cls')

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

while True:
    answer = typingInput('Do you wish to play as a Party Member? (yes/no)')
    if answer.lower().strip() == 'yes':
        typingPrint('!!!WARNING, MUST TYPE ANSWERS IN LOWERCASE AND EXACT ANSWER CHOICE!!!\n')
        time.sleep(1.5)
        typingPrint('Welcome to Oceania, Party Member.\n')
        time.sleep(1.5)
        clear()
        answer = typingInput('Enter a choice, (Go to my Ministry or Stay home.)').lower().strip()
        if answer == 'go to my ministry':
            answer = typingInput('You pass by a charming man, you dont know what to say but you know hes against the party. (pay no mind/look his way) ')

            if answer == 'look his way':
                typingPrint('You two lock eyes for only a moment, he nods and drops a piece of paper.')
                answer = input('Do you dare pick up the paper? (yes/no)')
                if answer == 'yes': 
                    typingPrint('The note reads,"Come by my flat around 14:23PM, lets drink over some victory gin!"')
                    typingPrint('You quickly stuff the paper inside of your pocket, hiding it away from prying eyes.')
                    typingPrint('Playing with the paper in your pocket, you debate if you should go or not.')
                    typingPrint('You quickly shuffle to your desk and get to work.')
                    answer = input('You finish up the work day, still fumbling with the note on the way home, do you go? (yes/no)')
                    if answer == 'yes':
                        typingPrint('You walk to the adress looking as lost as ever you stumble upon a luxurious flat suite.')
                        answer = input('Theres still time to turn back, do you ring the bell? (yes/no)')
                        if answer == 'yes':
                            clear()
                            typingPrint('The bell has an ominous tone, just a singular deep bong. Youre terrified and dont know what to think,')
                            typingPrint('After an eternity the man opens the door, a warm aura radiates from this man, you suddenly feel as if everythings okay.')
                            typingPrint('You come in, and you two talk for a bit, the usual, work, gin, the victorys of oceania.')
                            print('Suddenly the tone changes. "I know what you think."')
                            print('...')
                            print('...')
                            print('Would you like to rebel, the BrotherHood needs you.')
                            answer = input('(yes/no)')
                if answer == 'no': 
                    print('You ignore the man and head to the bathroom.')
                    answer = input('You go to the bathroom, a strange man in a corner stares at you signaling you to come over, go or ignore?')
                if answer == 'go':
                    print('The man was a trap set by the thought police, and youre dragged away into vaporization.')
                if answer == 'ignore':
                    print('you ignore the man and do your business, finishing up youre work and heading home after a long day, enjoy the gin.')
            else:
                print('You go about your day, ignoring the man. You sit down to prepare to do your ministry paperwork.')
                answer = input('After about 140 minutes of work, you have to use the bathroom, do you go? (yes/no)')
                if answer == 'yes':
                    answer = input('You go to the bathroom, a strange man in a corner stares at you signaling you to come over, go or ignore?')
                if answer == 'go':
                    print('The man was a trap set by the thought police, and youre dragged away into vaporization.')
                if answer == 'ignore':
                    print('you ignore the man and do your business, finishing up youre work and heading home after a long day.')
                if answer == 'no':
                    print('You hold your bladder, finishing up your long hard day of work and heading home to a nice drink of gin.')

        elif answer == 'stay home':
            answer = input('You feel a bit bored skipping your ministry, Go to the Black Market? (yes/no) ')

            if answer == 'yes':
                answer = input('A soldier stops you on your way there, questioning you, Lie or Tell the truth?')
            if answer == 'lie':
                print('The soldier doesnt believe you, you are arrested and Vaporized.')
            if answer == 'tell the truth':
                print('The soldier arrests you, and youre taken in for torture and eventual vaporization.')
            if answer == 'no':
                print('You bum around and take the day off, youre relaxation is interrupted by a telescreen calling your name telling you to get on your hands and knees.')
        else:
            print("Invalid Choice, Prepare to be vaporized.")

    else:
        print('Prepare to be vaporized, Prole..')
        break
