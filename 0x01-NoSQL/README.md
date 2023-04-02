# 0x01. NoSQL

## About
- NoSQL database
- MongoDB
    - Basic CRUD operations
    - Aggregation operations
    - Shell methods
- Interacting with MongoDB using `pymongo`

## Tasks
0. Script that lists all databases in MongoDB.
    - File: [0-list_databases](0-list_databases)
1. Script that creates or uses the database my_db.
    - File: [1-use_or_create_database](1-use_or_create_database)

2. Script that inserts a document in the collection school.
    - File: [2-insert](2-insert)

3. Script that lists all documents in the collection school.
    - File: [3-all](3-all)

4. Script that lists all documents with name="Holberton school" in the collection school.
    - File: [4-match](4-match)

5. Script that displays the number of documents in the collection school.
    - File: [5-count](5-count)

6. Script that adds a new attribute to a document in the collection school.
    - File: [6-update](6-update)

7. Script that deletes all documents with name="Holberton school" in the collection school
    - File: [7-delete](7-delete)

8. Function that lists all documents in a collection.
    - Prototype: `def list_all(mongo_collection):`
    - File: [8-all.py](8-all.py)

9. Function that inserts a new document in a collection based on kwargs.
    - Prototype: `def insert_school(mongo_collection, **kwargs):`
    - File: [9-insert_school.py](9-insert_school.py)

10. Function that changes all topics of a school document based on the name.
    - Prototype: `def update_topics(mongo_collection, name, topics):`
    - File: [10-update_topics.py](10-update_topics.py)

11. Function that returns the list of school having a specific topic
    - Prototype: `def schools_by_topic(mongo_collection, topic):`
    - File: [11-schools_by_topic.py](11-schools_by_topic.py)

12. Python script that provides some stats about Nginx logs stored in MongoDB:
    - Database: logs
    - Collection: nginx
    - Display (same as the example):
        - first line: x logs where x is the number of documents in this collection
        - second line: Methods:
        - 5 lines with the number of documents with the method = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below)
        - one line with the number of documents with:
            - `method=GET`
            - `path=/status`
    - File: [12-log_stats.py](12-log_stats.py)
    - Sample output:
```
$ ./12-log_stats.py 
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

13. Script that lists all documents with name starting by Holberton in the collection school
    - File: [100-find](100-find)

14. Function that returns all students sorted by average score:
    - Prototype: `def top_students(mongo_collection):`
    - `mongo_collection` will be the pymongo collection object
    - The top must be ordered
    - The average score must be part of each item returns with `key = averageScore`
    - File: [101-students.py](101-students.py)
15. Improvement of [12-log_stats.py](12-log_stats.py) that adds the top 10 of the most present IPs in the collection nginx of the database logs:
    - File: [102-log_stats.py](102-log_stats.py)
    - Sample output:
```
$ ./102-log_stats.py 
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
IPs:
    172.31.63.67: 15805
    172.31.2.14: 15805
    172.31.29.194: 15805
    69.162.124.230: 529
    64.124.26.109: 408
    64.62.224.29: 217
    34.207.121.61: 183
    47.88.100.4: 166
    45.249.84.250: 160
    216.244.66.228: 150
```
