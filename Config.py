import os.path

check_file = os.path.exists('cfg.txt')
if check_file == False:
    def config():
        f = open('cfg.txt', 'w+')
        x = '1'
        f.write(x)
        f.close

    config()
else:
    print("Конфиг уже есть")