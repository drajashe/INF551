# coding: utf-8
import sys
import mysql.connector
cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1',database='sakila')
cursor = cnx.cursor()
search_this_category = []
search_this_category = sys.argv[1]

query="SELECT c.name, COUNT(c.category_id) as film_count FROM  category as c  JOIN film_category as s on c.category_id = s.category_id JOIN film as t on t.film_id = s.film_id GROUP by c.category_id ORDER BY c.name;"


cursor.execute(query)
results = cursor.fetchall()
#print results 
for x  in results:
        if x[0].lower() == search_this_category.lower():
            print x[1]
cnx.commit()
cursor.close()
cnx.close()
