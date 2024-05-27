import os
import shutil
import ctypes
from ctypes import wintypes

def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Не удалось удалить {file_path}. Причина: {e}')

def empty_recycle_bin():
    try:
        SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI = 0x00000002
        SHERB_NOSOUND = 0x00000004

        result = SHEmptyRecycleBin(None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)
        if result != 0:
            print(f'Ошибка при очистке корзины: {result}')
    except Exception as e:
        print(f'Не удалось очистить корзину. Причина: {e}')


# Noņemiet režģi, lai aktivizētu funkcionalitāti palaišanas laikā.

# clear_directory(r"C:\Users\Something")
# empty_recycle_bin()
