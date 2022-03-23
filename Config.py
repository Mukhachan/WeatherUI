import os.path
check_file = os.path.exists('config.cfg')
if check_file == False:
    f = open('config.cfg', 'w+')

    f.close

    f.write('1' + '1')
    print(f.read(2))
    

elif check_file == True:

        f = open('config.cfg', 'r')
        read = f.readlines()
        
        try:
            print(read[0] + read[1])
        except:
            f.close()
            f = open('config.cfg', 'w+')
            f.write(read[0] + '1')