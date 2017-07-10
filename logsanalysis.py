#!/usr/bin/env python2.7
import psycopg2
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()

print "Three most popular articles of all time in order:"
print "\n"
cursor.execute("SELECT articles.title AS Articles, COUNT(log.id) AS Views" +
               " FROM articles LEFT JOIN log ON log.path" +
               " LIKE '/article/'||articles.slug GROUP BY" +
               " articles.title ORDER BY Views DESC LIMIT 3;")
temp = cursor.fetchall()
for row in temp:
        article, views = row
        print "Article: ", article
        print "Views: ", views
print "\n"
print "Most popular article author of all time in order:"
print "\n"
cursor.execute("SELECT authors.name,tmp.totalViews FROM" +
               " (SELECT articles.author,SUM(popular.views) AS TotalViews" +
               " FROM articles LEFT JOIN popular" +
               " ON articles.title=popular.articles" +
               " GROUP BY articles.author ORDER BY TotalViews DESC)" +
               " AS tmp JOIN authors ON authors.id=tmp.author;")
for row in cursor.fetchall():
        name, views = row
        print "Author name: ", name
        print "Views: ", views

print "\n"
print "More than 1% of errors occured in following days:"
print "\n"
cursor.execute("SELECT date,res.errors FROM" +
               " (SELECT date,ROUND(tmp.failure*100.0/tmp.total,1) AS errors" +
               " FROM (SELECT date(time),COUNT(*) AS" +
               " total,sum(case when status!='200 OK' then 1" +
               " else 0 end) AS failure" +
               " FROM log GROUP BY date(time) ORDER BY" +
               " date(time)) AS tmp) AS res WHERE res.errors>1;")
for row in cursor.fetchall():
        date, errors = row
        print "Date: ", date
        print "% of errors: ", errors

conn.close()


