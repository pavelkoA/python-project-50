### Hexlet tests and linter status:
[![Actions Status](https://github.com/pavelkoA/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pavelkoA/python-project-50/actions/workflows/hexlet-check.yml)
[![Actions Status](https://github.com/pavelkoA/python-project-50/actions/workflows/my-check.yml/badge.svg)](https://github.com/pavelkoA/python-project-50/actions/workflows/my-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/94c58bc4aede04bbc224/maintainability)](https://codeclimate.com/github/pavelkoA/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/94c58bc4aede04bbc224/test_coverage)](https://codeclimate.com/github/pavelkoA/python-project-50/test_coverage)

<h1>Вычислитель отличий</h1>

Утилита умеет сравнивать между собой json и yaml файлы.

## Содержание
- [Технологии](#технологии)
- [Установка пакета](#установка-пакета)
- [Утилита diff_generate](#утилита-diff_generate)
- [Сравнение файлов](#сравнение-файлов)
- [Сравнение файлов с вложенной структурой](#сравнение-рекурсивных-файлов)
- [Плоское представление отличий](#плоское-представление-отличий)


## Технологии
- [Python3](https://www.python.org/)


## Установка пакета

- Вводим команду для установки пакета
```sh
python3 -m pip install --user git+https://github.com/pavelkoA/python-project-50.git
```


## Утилита diff_generate

- Нам доступна утилита diff_generate,  которую можно импортировать из модуля gendiff
[![asciicast](https://asciinema.org/a/NebDKWglCP23z3G6n7nM1LnGj.svg)](https://asciinema.org/a/NebDKWglCP23z3G6n7nM1LnGj)


## Сравнение файлов

- Для того что бы сравнить два файла, необходимо ввести команду
```sh
gendiff path_file1 path_file2
```
[![asciicast](https://asciinema.org/a/QbcYPhzDLjQaiKsgfhIYD9YOa.svg)](https://asciinema.org/a/QbcYPhzDLjQaiKsgfhIYD9YOa)


## Сравнение файлов с вложенной структурой

- Так же есть возможность сравнить файлы с вложенной структурой:
[![asciicast](https://asciinema.org/a/h42f6CaaEY2ZSwp0MYMh7sBXj.svg)](https://asciinema.org/a/h42f6CaaEY2ZSwp0MYMh7sBXj)


## Плоское представление отличий

- Утилита позволяет выбрать текстовое представление отличий в файлах.
Для этого необходимо указать дополнительный параметр "plain"
```sh
gendiff path_file1 path_file2 --format plain
```
[![asciicast](https://asciinema.org/a/IYkaZ4hdpWvO81MqjgrzzyEFf.svg)](https://asciinema.org/a/IYkaZ4hdpWvO81MqjgrzzyEFf)
