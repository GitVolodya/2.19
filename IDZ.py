#!/usr/bin/env python3Х
# -*- coding: utf-8 -*-
# Для своего варианта лабораторной работы 2.17
# добавьте возможность хранения файла данных в домашнем каталоге пользователя.
# Для выполнения операций с файлами необходимо использовать модуль pathlib.

import argparse
import json
from pathlib import Path


def input_data():
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        student = {"фамилия и инициалы": input("Введите фамилию и инициалы студента: "),
                   "номер группы": input("Введите номер группы студента: "), "успеваемость": []}
        for j in range(5):
            mark = int(input(f"Введите оценку {j + 1}: "))
            student["успеваемость"].append(mark)
        students.append(student)
    students.sort(key=lambda x: x["фамилия и инициалы"])
    return students


def save_data(students, filename):
    with open(filename, "w") as file:
        json.dump(students, file, ensure_ascii=False)


def read_data(filename):
    with open(filename, "r") as file:
        students = json.load(file)
        students.sort(key=lambda x: x["фамилия и инициалы"])
        return students


def print_students_with_mark2(students):
    found = False
    for student in students:
        if 2 in student["успеваемость"]:
            print(f"Студент: {student['фамилия и инициалы']}, группа: {student['номер группы']}")
            found = True
    if not found:
        print("Нет студентов с оценкой 2")


def main():
    parser = argparse.ArgumentParser(description="Process student data")
    parser.add_argument("--filename", help="Имя файла для сохранения/загрузки данных", default="students.json")
    args = parser.parse_args()

    home_directory = Path.home()
    filename = home_directory / args.filename

    students = input_data()
    save_data(students, filename)

    students = read_data(filename)
    print_students_with_mark2(students)


if __name__ == "__main__":
    main()
