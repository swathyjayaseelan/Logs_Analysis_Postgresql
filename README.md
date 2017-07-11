# Logs_Analysis_Postgresql

## About
This is the third project in Udacity Full-Stack Developer Nanodegree.  In this project, a large Postgresql database with over a million rows is explored by building complex SQL queries. An internal reporting tool is built to explore the data and report the findings like the most viewed articles, popular authors so that business decisions can be made.

## Database Schema
Tables:
1. Articles - List of all the articles written by authors
2. Authors - List of all the authors
3. Log - Web server data of the requests received

## Prerequisites
1. Python version 2 and above
2. Vagrant 
3. Virtual Machine

## Installation
1. Install Vagrant and VM
2. Download [fullstack-nanodegree-vm]( https://github.com/udacity/fullstack-nanodegree-vm)
3. Download [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here. Unzip and get the newsdata.sql file and place it inside the vagrant directoy
4. Fork this repository or download this project and put the file "logsanalysis.py" inside the vagrant folder along with newsdata.sql

## To Execute
1. Open terminal and execute "vagrant up"
2. Log in using "vagrant ssh"
3. Change into directory /vagrant
4. Load the data in local database using "psql -d news -f newsdata.sql"
5. Connect to news database "psql -d news"
6. Create "popular" view by executing the below query
"CREATE VIEW popular AS SELECT articles.title AS Articles, COUNT(log.id) AS Views FROM articles LEFT JOIN log on log.path LIKE '/article/'||articles.slug GROUP BY articles.title ORDER BY Views DESC;"
7. Exit database using "\q"
8. Run the reporting tool script file "python logsanalysis.py"

P.S: Sample of the output is provided in the repository




