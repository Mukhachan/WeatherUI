f = open('cfg.cfg', 'w')
x = '1'
f.write('Записал - ' + x)
f.close()


f = open('cfg.cfg', 'r')
read = str(f.readlines())
print("Прочитал - " + read[0])
f.close()