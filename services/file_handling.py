import os
import sys

BOOK_PATH = '../book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = [',', '.', '!', ':', ';', '?']
    split_text = text[start:]
    max_index = 0
    for m in marks:
        if len(text) < start + size:
            if split_text[:size].rfind(m) > max_index:
                max_index = split_text[:size].rfind(m)
        else:
            if (
                split_text[:size].rfind(m) > max_index and
                split_text[split_text[:size].rfind(m) + 1] != '.'
            ):
                max_index = split_text[:size].rfind(m)
    split_text = split_text[:max_index + 1]
    return (split_text, len(split_text))


# Функция, формирующая словарь книги
def prepare_book(path: str):
    with open(path, encoding='utf-8') as file:
        fileContent = file.read()
    n = 1
    while fileContent:
        page_res = _get_part_text(fileContent, 0, PAGE_SIZE)
        fileContent = fileContent[page_res[1]:]
        book[n] = page_res[0].lstrip()
        n += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
