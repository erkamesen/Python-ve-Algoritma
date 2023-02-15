import os
import errno
#Klasör oluşturma

def klasor_olusturma(count, rank):
    try:
        os.mkdir(f"./{rank} ")
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    os.chdir(f"./{rank} ")
    os.mkdir(f"./{count}. Problem ")
    os.chdir(f"./{count}. Problem ")
    with open("README.md", "w") as f:
        f.write(f"# Soru {count} - {rank}")
    os.chdir("/home/erkam/Dosyalar/Python ve Algoritma/Egzersizler - 300 Soru")

for i in range(1,301):
    if i<101:
        klasor_olusturma(count=i, rank="Başlangıç")
    elif i<201 and i>99:
        klasor_olusturma(count=i, rank="Orta")
    else:
        klasor_olusturma(count=i, rank="İleri")

    
    