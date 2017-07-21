# Copy-rename

<p>
цель:<br>
	одной из фич win10 является наличие красивых картинок на экране ожидания, которые система подбирает в зависимости от предпочтений пользователя (опция "вам понравилось увиденное?"). картинки периодически подгружаются с серверов microsoft. почему бы не использовать их в качестве фона рабочего стола...
	программа предназначена для эпизодического использования, по мере подгружения новых картинок.
</p>

задачи:
	-выборочное копирование файлов из одной директории в другую
	-фильтрация файлов по размеру
	-файлы удовлетворяющие условию фильтрации, сравнить с файлами имеющимися в целевой директории
	-если совпадений нет, скопировать файл с добавлением расширения
	
алгоритм:	
	*задать исходную и целевую директории
	*получить список имен файлов из обеих директорий
	*(for) поэлементно перебрать список имен файлов из исходной директории
		*сформировать путь к каждому файлу и получить его размеру
			*(if) задать условие фильтрации файлов по размеру
				*добавить расширение jpg к именам файлов удовлетворяющим условию фильтрации
				*сформировать пути К копируемым файлам и пути ДЛЯ копирования
				*(if) проверить наличие копируемого файла в целевой директории
					*если файла в директории нет, произвести копирование
					
	... PROFIT ...

	
ЗЫ: хочу сделать то-же самое, только с фильтрацией по параметрам изображения (height-width). но оказалось что в Python "нельзя так просто взять и получить размеры изображения графического файла". есть хитровыебанный и дохуя много-функциональный модуль, с помощью которого через глубокую жопу это можно сделать. но должен же быть путь прооще... мож посоветуешь что-нибудь?