
# python Copy_Rename-v2.3.py


import shutil
import os

source_directory = 'C:\\Users\\пк\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets' # исходная директория
target_directory = 'D:\\photo\\wallpaper\\win10\\new' # целевая директория

source_files = os.listdir(source_directory) # получение списка имен файлов из исходной директории
target_files = os.listdir(target_directory) # получение списка имен файлов из целевой директории

for each_file in source_files: # поэлементный перебор списка файлов
	f_size = os.path.getsize(os.path.join( source_directory, each_file)) # формирование пути к каждому файлу и получение его размера
	if f_size > 100000: # условие фильтрации файлов по размеру (в байтах)
		list_file_name = list( each_file ) # преобразование имени файла в список
		old_file_name = ''.join( list_file_name ) # сохранение в переменную старого имени файла в виде строки для дальнейшего формироваия пути к нему
		list_file_name.append( '.jpg' ) # добавление расширения
		new_file_name = ''.join( list_file_name ) # преобр списка с именем файла, в строку
		
		o_f_m = os.path.join( source_directory, old_file_name ) # формирование пути К копируемому файлу
		n_f_m = os.path.join( target_directory, new_file_name ) # формирование пути ДЛЯ копируемого файла с новым именем
			
		if new_file_name not in target_files: # проверка на вхождение
			shutil.copy( o_f_m, n_f_m) # копирование (и переименование) файла
			# os.rename( o_f_m, n_f_m ) # переименование (и перемещение) файла (не катит)


# З.Ы.: говоришь документации много не быает?..  )))

