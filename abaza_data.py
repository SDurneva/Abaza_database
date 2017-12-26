#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from openpyxl import load_workbook


def create_db():
    f = open('abaza_db.sql', 'r', encoding='utf-8')
    conn = sqlite3.connect('abaza_database.db')
    c = conn.cursor()
    command = f.read()
    c.executescript(command)

def some_data():
    commands_inf = ['INSERT INTO Informant (full_name, gender, year_of_birth, birthplace, education, occupation, '
                    'native_language, speaks_since_childhood, fathers_birthplace, fathers_native_language, '
                    'mothers_birthplace, mothers_native_language, mother_speaks_Abaza, fam_lang_childh, fam_lang_now, '
                    'speaks_Circaccian, speaks_Circ_freq) '
                    'values('Айсанов Зауаль Джибович', 'м' , 1941, 'Инжич-Чукун' , 'высшее (русский язык)', ' \
                     ''читель истории', 'абазинский', 'со школы', 'Инжич-Чукун', 'абазинский', 'Зеюко' , 'черкесскй' , ' \
                     ''да' , 'дома с матерью на черкесском; со старшим братом на абазинском' , '', 'свободно', ' \
                     ''раньше чаще, сейчас нет, снохи были черк.' );', 'INSERT INTO Informant (full_name, gender, year_of_birth, birthplace, education, occupation, native_language, speaks_since_childhood, fathers_birthplace, fathers_native_language, mothers_birthplace, mothers_native_language, mother_speaks_Abaza, fam_lang_childh, fam_lang_now, speaks_Circaccian, speaks_Circ_freq) values('Озова Сакинат Мухамедовна (сестра Фатимы Асанаевой)', 'ж', 1961, 'Инжич-Чукун', 'среднее', 'бухгалтер', 'абазинский', 'да', 'Инжич-Чукун', 'абазинский', 'Эльбурган', 'абазинский', 'да', 'абазинский', 'абазинский', 'очень хорошо', 'иногда  на работе');']
    conn = sqlite3.connect('abaza_database.db')
    c = conn.cursor()
    for comm in commands_inf:
        c.execute(comm)
    commands_intw = ['INSERT INTO Interviewer (full_name, academic_stat, email, university) VALUES('Дурнева Софья Павловна', 'студент', 'sonia.durneva@gmail.com', 'НИУ ВШЭ');', 'INSERT INTO Interviewer (full_name, academic_stat, email, university) VALUES('Аркадьев Пётр Михайлович', 'доцент', 'alpgurev@gmail.com', 'РГГУ');']
    for comm in commands_intw:
        c.execute(comm)
    commands_exs = ['INSERT INTO Example (text, translation, datetime, subject, informantid, interviewerid) VALUES('Ауи тшылпщитI.', 'Она отдыхает.', 2017-07-06, 'рефлексив', 1, 1);', 'INSERT INTO Example (text, translation, datetime, subject, informantid, interviewerid) VALUES('Ауи тшпылщИтI.', 'Она отдыхает.', 2017-07-06, 'рефлексив', 2, 1);', 'INSERT INTO Example (text, translation, datetime, subject, informantid, interviewerid) VALUES('Ауат ртараквАла шырпсАхтI.', 'Они поменялись местами.', '2017-07-06', 'рефлексив', 1, 1);', 'INSERT INTO Example (text, translation, datetime, subject, informantid, interviewerid) VALUES('АуАт ргЫларта рпсахтI.', 'Они поменялись местами.', '2017-07-06', 'рефлексив', 2, 1);']
    for comm in commands_exs:
        c.execute(comm)
    commands_alts = ['INSERT INTO Alternatives (example1id, example2id) VALUES (1, 2);', 'INSERT INTO Alternatives (example1id, example2id) VALUES (3, 4);']
    for comm in commands_alts:
        c.execute(comm)
    commands_advs = ['INSERT INTO Advisor (interviewerid, advisorid) VALUES (1,2);']
    for comm in commands_advs:
        c.execute(comm)
def main():
    fill_informants()


if __name__ == "__main__":
   main()