# Log Analysis

Project Log Analysis- Udacity Full Stack Nanodegree course
A Reporting tool was built that will use information from the database to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using this information, the following code will answer questions about the site's user activity.

### Project Overview
For this project, the task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the `psycopg2` module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Why This Project?
In this project, I can stretch my SQL database skills. I will get practice interacting with a live database both from the command line and from my code. I will explore a large database with over a million rows. And I can build and refine complex queries and use them to draw business conclusions from data.

### RUNNING THE PROGRAM
1. To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder. 

#### PreRequisites:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here.
  3. Unzip this file after downloading it. The file inside is called newsdata.sql.
  4. Copy the newsdata.sql file.
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant/Log-Analysis.

3. Load the database using `psql -d news -f newsdata.sql`. 

4. Connect to the database using `psql -d news`.

5. Create the Views given below.

#### CREATE THE FOLLOWING VIEWS:

##### View 1

```sql
CREATE VIEW art_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```

##### View 2

```sql 
CREATE VIEW art_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```

##### View 3

```sql
CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
```

##### View 4

```sql
CREATE VIEW errlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```

7. Then exit `psql`.

8. Now execute the Python file - `python project.py`.

