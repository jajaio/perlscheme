import colors as c
import os

def run():
    option=input(c.yellow+"Would you like to view old data? or create new data? (1), (2)"+c.reset+" >>>"+c.violet)
    if option == '1':
        os.system('cat .data.txt')
        clean=input(c.yellow+'Would you like to delete this data message? (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
        if clean == 'y':
            os.system('rm .data.txt')
            print(c.yellow+'Data deleted!')
        elif clean == 'n':
            print(c.yellow+'Data saved!')
        else:
            print(c.yellow+'No answer provided. Message saved.')
        input('[Press enter to continue]')
        print(c.clear)
        run()
    elif option == '2':
        prompt = input(c.yellow+"What would you like to say?"+c.reset+" >>> "+c.violet)
        os.system('date >> .data.txt')
        os.system('echo '+prompt+' >> .data.txt')
        os.system('echo '+prompt+' >> .history.txt')
        #os.system('bash notify')
        input('Message sent! [Press enter]')
        print(c.clear)
    else:
        print('Invalid Response')
        t.sleep(1)
        print(c.clear)
        run()

if __name__ == '__main__':
    print(c.clear)
    print(c.yellow+"Welcome to Perl's Coding Scheme")
    while True:
        try:
            run()
        except(KeyboardInterrupt):
            print("Goodbye!")
            exit()
        except(EOFError):
            print("Goodbye!")
            exit()
