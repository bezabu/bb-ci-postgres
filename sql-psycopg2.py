import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor obect of the database
cursor = connection.cursor()

# query 1 select all recors from Artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 select only the name column from the artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query 4
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# query 6
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
