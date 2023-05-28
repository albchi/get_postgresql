import random

# input : none
# output : FILEOUT = populate.sql
#        : 100 POSTGRESQL command to create a SQL table

NUM_OF_INSERTS = 100
FILEOUT= "populate.sql"

c1 = ("b","c","d","f","g","h","j","k")
c2 = ("a","e","i","o","u")
c3 = ("m","n","p","q","s","t","v","w")
#f = open("populate.sql", "w")
f = open(FILEOUT, "w")

f.write("CREATE DATABASE db_friends;")

f.write("\c db_friends;")

f.write("CREATE TABLE t_friends (id SERIAL PRIMARY KEY , name VARCHAR(100) NOT NULL, chill INT);")
f.write("\n")

f.write("\d;");

for tmp in range (NUM_OF_INSERTS):
   tc1 = random.choice(c1)
   tc2 = random.choice(c2)
   tc3 = random.choice(c3)

   # INSERT INTO t_friends(name, chill) VALUES ("Sal", 4");
   rname = tc1+tc2+tc3; # random name
   rchill = random.randint(0,9)
   rall = "INSERT INTO t_friends (name, chill) VALUES (\"" + str(rname) + "\",\"" + str(rchill) + "\")"

   print(rall);
   f.write("\n")
   f.write(str(rall));

f.close()
