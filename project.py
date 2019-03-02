#!/usr/bin/env python3
# Import postgresql
import psycopg2

DBNAME = "news"

query1 = """SELECT *
            FROM art_views
            LIMIT 3;"""

query2 = """SELECT name, sum(art_views.views) AS view
            FROM art_authors, art_views
            WHERE art_authors.title = art_views.title
            GROUP BY name
            ORDER BY view desc;"""

query3 = """SELECT errlogs.date, round(100.0*errorcount/logcount,2) as percentage
            FROM logs, errlogs
            WHERE logs.date = errlogs.date
            AND errorcount > logcount/100;"""


def connect(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Question 1. What are the most popular three articles of all time?

def top_articles(query):
    results = connect(query)
    print('\n The most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' has ' + str(i[1]) + ' views')
        print(" ")


# Question 2. Who are the most popular article authors of all time?

def top_authors(query):
    results = connect(query)
    print('\n The most popular authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' has ' + str(i[1]) + ' views')
        print(" ")


# Question 3. On which days did more than 1% of requests lead to errors?

def error_percentage(query):
    results = connect(query)
    print('\n The days when more than 1% of requests lead to error:\n')
    for i in results:
        print('\t' + ' On ' + str(i[0]) + 'the error was' + str(i[1]) + ' % ')
        print(" ")

if __name__ == '__main__':
    top_articles(query1)
    top_authors(query2)
    error_percentage(query3)
