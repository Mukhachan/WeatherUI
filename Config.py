
import os.path
check_file = os.path.exists('config.cfg')
if check_file == False:
    f = open('config.cfg', 'w+')
    f.close
    f.write('1\n' + '1')
    print(f.read(2))
    

elif check_file == True:

        f = open('config.cfg', 'r')
        read = f.readlines()
        print(read)
        f.close

        f = open('config.cfg', 'r')
        readline1 = f.readline()
        f.close

        try:            
            if read[0] == '1' or '0' or '\n':
                print('Всё ок')
        except:
            f = open('config.cfg', 'w+')
            f.write('1')
            f.close
            
        try:
            f = open('config.cfg', 'r')
            read = f.readlines()
            f.close
            if read[1]!='0' or '1' or '\n':
                f = open('config.cfg', 'w+')
                f.write(read[0] + '\n1')
                f.close
        except IndexError:
            f = open('config.cfg', 'w')
            

        if read[0] != '1' or '0' or '\n':
            f = open('config.cfg', 'w+')
            try:
                f.write('1\n' + read[1])
            except IndexError:
                f.write('1\n1')

            print('Там была белеберда. Я исправиль)')
            f.close

            f = open('config.cfg', 'r')
            read = f.readlines()
            print(read)
            f.close 