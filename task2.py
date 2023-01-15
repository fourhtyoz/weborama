"""
Скрипт получает один аргумент (файл формата .epub/.fb2 в командрной строке)
и возвразает список вида ["название", "имя автора", "издательство", "год"].
Если файл не найден, то возращает ошибку "файл не найден"
Если файл неправильного формата, то возвращает ошибку "неверный формат".
"""

# EPUB
# Модуля для обработки epub файлов
from ebooklib import epub

# Убирает оповещение от модуля ebooklib
epub.EpubReader.DEFAULT_OPTIONS = {'ignore_ncx': True}

def epub_parser(filename, namespace='DC', fields=['title', 'creator', 'publisher', 'date']):
    """
    Получает файл для обработки. В обязательные поля прописаны
    дефолтные значения: DC (по документации модуля) и метаданные,
    значения которых мы ищем.
    Функция возвращает список значений метаданных из fields.
    """
    book = epub.read_epub(filename)
    result = []
    for item in fields:
        info = book.get_metadata(namespace=namespace, name=item)
        if item == 'date':
            # Обработка строки даты из мета-данных
            date = info[0][0]
            result.append(date[:4]) # Вычленяется год
        else:
            result.append(info[0][0])
    print(result)

# FB2
from bs4 import BeautifulSoup as bs

def fb2_parser(filename, fields=['book-title', 'first-name', 'last-name', 'publisher', 'year']):
    """
    Получает файл для обработки. 
    В обязательное поля прописаны метаданные, которые мы ищем.
    Функция возвращает список значений метаданных из fields.
    """
    with open(filename, 'r') as f:
        content = f.readlines()
        content = ''.join(content) # Преобразуем в строки из списка
        
        # Используем BeautifulSoup для обоаботки xml файл
        bs_content = bs(content, 'xml') 
        res = [] 
        name = [] # Для форматирования имени автора
        for item in fields:
            if item == 'first-name' or item == 'last-name':
                info = bs_content.find(item).text
                name.append(info)
            else:
                info = bs_content.find(item).text
                res.append(info)
        name = ' '.join(name)
        res.insert(1, name)
        print(res)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        raise(TypeError)
    else:
        file = sys.argv[1]
        try:
            if '.epub' in file:
                epub_parser(file)
            else:
                fb2_parser(file)
        except FileNotFoundError:
            print(f'{file} not found')
        except:
            print(f'Error. Only EPUB or FB2 files are accepted')