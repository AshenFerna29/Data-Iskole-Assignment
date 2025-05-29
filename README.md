# 🤹‍♂️ Superhero Universe Network – Take-Home Assignment

This Python project analyzes a fictional superhero network using two CSV files: one containing superhero details and another describing connections (friendships) between them. The application provides insights into the network and lets users interact by adding or deleting superheroes.

---

## Files Included

* `superheroes.csv`: Contains superhero ID, name, and the date they were added.
* `links.csv`: Contains pairs of superhero IDs that represent friendships (connections).
* `main.py`: The Python script that runs the full superhero network program.

---

## Features Implemented

* Load and parse superhero and connection data from CSV files
* Show total number of superheroes and total number of connections
* List the 3 most recently added superheroes
* Display the 3 most connected superheroes in the network
* Analyze a specific superhero: `dataiskole` (date added + friends)
* Add a new superhero with:
* Automatic ID assignment
* Timestamp of creation
* Name duplication protection (case-insensitive and normalized)
* Add connections to existing superheroes
* Delete a superhero (only if their ID > 11)
* Automatically deletes all connections related to the deleted superhero
* All updates persist in the `superheroes.csv` and `links.csv` files

## How to Run Your Code

1. **Install Python**: Ensure Python 3.12+ is installed.
2. **Install dependencies** (if not already installed):

   ```
   pip install pandas matplotlib networkx
   ```
3. **Make sure the following files are in the same directory**:

* main.py
* superheroes.csv
* links.csv

4. **Run the application**

   ```
   python main.py
   ```

## Sample Output

```
---------- Welcome to Superhero Universe Network ----------

The total number of the Superheroes: 11
The total number of connections: 42

----------------

Most recently added heroes:
         name created_at
   dataiskole 2025-05-26
Scarlet Witch 2025-05-24
      Ant-Man 2025-05-24

----------------

The Most Connected Superheroes:
Spider-Man (ID: 1) -- 10 Connections
Captain America (ID: 5) -- 10 Connections
Iron Man (ID: 2) -- 9 Connections

Dataiskole was added on: 2025-05-26 00:00:00
Friends of 'dataiskole':
 Spider-Man
 Captain America
 Scarlet Witch

----------------

Would you like to add a new Superhero? (YES/NO): yes
Enter your new Superhero's name: Batman

 The new Superhero 'Batman' is added with ID 12 on 2025-05-30 02:37:49

Do you want to add a connection to Batman? (YES/NO): yes
Available Superheroes:
 id            name
  1      Spider-Man
  2        Iron Man
  3            Thor
  4            Hulk
  5 Captain America
  6     Black Widow
  7  Doctor Strange
  8   Black Panther
  9   Scarlet Witch
 10         Ant-Man
 11      dataiskole
 12          Batman
Enter the ID of the superhero you want to connect with: 1
 Connection added between Batman and ID 1.

Do you want to add another connection? (YES/NO): no

----------------

Would you like to delete a superhero you added? (YES/NO): yes

Only superheroes with ID greater than 11 can be deleted.
Available Superheroes:
 id   name
 12 Batman

Enter the ID of the superhero you want to delete: 12

 Superhero 'Batman' (ID: 12) and all related connections were successfully deleted.

---- Remaining super heroes ----
 id            name
  1      Spider-Man
  2        Iron Man
  3            Thor
  4            Hulk
  5 Captain America
  6     Black Widow
  7  Doctor Strange
  8   Black Panther
  9   Scarlet Witch
 10         Ant-Man
 11      dataiskole
```

## Tools or Libraries Used

* Python 3.12
* pandas – For reading and manipulating CSV data
* datetime – To handle timestamps
* collections.Counter – To count superhero connections

## Extra Info

* All superhero names are normalized (case-insensitive, space and dash agnostic) to prevent duplicate entries.
* Users can only delete superheroes with ID greater than 11 (i.e., user-added ones).
* All additions and deletions persist by updating the actual CSV files.
* The code is modular and easily extendable if you wish to include more advanced analytics or UI.


##  Thank You!

This project was developed as part of a take-home coding challenge. It demonstrates practical Python skills with data analysis, user interaction, and file handling. Happy to walk you through the logic during the interview!
