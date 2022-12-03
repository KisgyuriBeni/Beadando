import shutil

file = open("szoveg.txt", "r", encoding="utf-8")




for sor in file:
    print(sor.strip())

shutil.copyfile('szoveg.txt', 'masoltszoveg.txt')
file.close()

for i in range (1):
    shutil.copyfile('szoveg.txt', 'masoltszoveg.txt')
    print("sikerült!")
