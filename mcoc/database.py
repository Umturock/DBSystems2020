import os
import psycopg2
from flask import current_app

DATABASE_URL = current_app.config['DATABASE_URL']


def add_champion(name, rank, level, star, siglevel, account):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO champion (name, rank, level, star, siglevel, account)
                        VALUES ({name},{rank},{level},{star}, {siglevel}, {account});")


def get_champion(ID, name, star, account):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            if ID is not None:
                condition = f"ID = {ID}"
            else:
                condition = f"name = {name} AND star = {star} AND account = {account}"
            cur.execute(f"SELECT * FROM champions WHERE {condition};")


def update_champion(column, value, condition):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE champion SET {column} = {value} WHERE {condition};")


def remove_champion(ID):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM champions WHERE ID = {ID};")


def add_synergy(type, rootchamp, targetchamp, effect):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO synergy (type, rootchamp, targetchamp, effect)
                        VALUES ({type},{rootchamp},{targetchamp},{effect});")


def get_synergy(ID, rootchamp, targetchamp):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            if ID is not None:
                condition = f"ID = {ID}"
            else:
                condition = f"rootchamp = {rootchamp} AND targetchamp = {targetchamp}"
            cur.execute(f"SELECT * FROM synergy WHERE {condition};")


def update_synergy(ID, rootchamp, targetchamp, newtext):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE synergy SET effect = {newtext} WHERE rootchamp = {rootchamp} AND targetchamp = {targetchamp};")


def remove_synergy(ID):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM synergy WHERE ID = {ID};")


def add_account(password, email, accounttitle, accountleve):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"INSERT INTO account (password, email, accounttitle, accountleve)
                        VALUES ({password},{rootemailchamp},{accounttitle},{accountleve});")


def get_account(ID, email):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            if ID is not None:
                condition = f"ID = {ID}"
            else:
                condition = f"email = {email}"
            cur.execute(f"SELECT * FROM account WHERE {condition};")



def update_account(column, value, condition):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE account SET {column} = {value} WHERE {condition};")



def remove_account(ID):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(f"DELETE FROM account WHERE ID = {ID};")
