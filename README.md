# 🤹‍♂️ Superhero Universe Network – Take-Home Assignment

This Python project analyzes a fictional superhero network using two CSV files: one containing superhero details and another describing their connections. The application provides interactive features, robust error handling, and visual network representation using graphs.

---

## Files Included

* `superheroes.csv`: Contains superhero ID, name, and the timestamp they were added.
* `links.csv`: Contains pairs of superhero IDs representing their connections.
* `main.py`: The Python script that runs the full superhero network program.
* `loader.py`: Loads superhero and link data safely.
* `interact.py`: Handles user interactions like adding or deleting superheroes.
* `fileops.py`: Saves updated data back to CSVs.
* `analyzer.py`: Provides data insights like recent additions or most connected.
* `visualizer.py`: Displays a clear, interactive graph of the network.

---

## Features Implemented

* Load and validate superhero and connection data from CSV files
* Show total count of superheroes and their connections
* Display 3 most recently added superheroes (with timestamp)
* Display 3 most connected superheroes
* Analyze a specific superhero: `dataiskole`
  * When they were added
  * Who their friends are
* Add a new superhero with:
  * Auto-incremented ID
  * Current timestamp
  * Name duplication prevention (case-insensitive and format-agnostic)
* Add connections to existing superheroes by ID
* Delete a superhero (ID > 11 only to preserve built-in heroes)
  * Automatically removes related connections
* Clear graph visualization using `networkx` and `matplotlib`
* Persistent updates to `superheroes.csv` and `links.csv`
* Input validation and full error handling for user mistakes

---

## How to Run Your Code

1. **Install Python**: Make sure Python 3.12 or higher is installed.
2. **Install required libraries**:

   ```bash
   pip install pandas matplotlib networkx
   ```

3. **Ensure all files are placed in the appropriate directory**:

   ```
   - data/
     - superheroes.csv
     - links.csv
   - src/
     - main.py
     - loader.py
     - analyzer.py
     - interact.py
     - fileops.py
     - visualizer.py
   ```

4. **Run the application**:

   ```bash
   python src/main.py
   ```

---

## Sample Output

```
---------- Welcome to Superhero Universe Network ----------

The total number of the Superheroes: 14
The total number of connections: 58

----------------

Most recently added heroes:
    Ashen 2025-06-06
dataiskole 2025-05-26
Scarlet Witch 2025-05-24

----------------

The Most Connected Superheroes:
Spider-Man (ID: 1) -- 10 Connections
Captain America (ID: 5) -- 10 Connections
Iron Man (ID: 2) -- 9 Connections

Dataiskole was added on: 2025-05-26 00:00:00
Friends of 'dataiskole':
 - Spider-Man
 - Captain America
 - Scarlet Witch

----------------

Do you want to ADD or DELETE a superhero? (ADD/DELETE/SKIP): add
Enter new superhero's name: Ashen
✅ Superhero 'Ashen' added with ID 14.

Do you want to add a connection? (YES/NO): yes
 id           name
  1     Spider-Man
  2       Iron Man
  ...
 13      Superman
 14         Ashen
Enter ID to connect with: 1
🔗 Connection added between 14 and 1.

Do you want to add a connection? (YES/NO): no

----------------

Do you want to ADD or DELETE a superhero? (ADD/DELETE/SKIP): delete
Only superheroes with ID > 11 can be deleted.
 id   name
 12 Bat Man
 13 Superman
 14   Ashen

Enter ID to delete: 14
✅ Deleted superhero 'Ashen' and all associated connections.

----------------

Do you want to display the superhero graph? (YES/NO): yes
[ Graph window opens ]
```

---

## Tools or Libraries Used

* Python 3.12
* pandas – For data manipulation and CSV operations
* matplotlib – To draw the graph
* networkx – For building and analyzing the network
* datetime – To handle and compare timestamps
* collections.Counter – To count connection frequencies

---

## Extra Info

* User inputs are validated (non-empty names, valid IDs, YES/NO prompts).
* Protected heroes (ID ≤ 11) cannot be deleted to maintain base network integrity.
* Graphs are built with meaningful node labels and connection lines for clarity.
* Error handling ensures the app doesn’t crash due to bad input or file issues.
* Loop continues for ADD/DELETE actions until the user chooses SKIP.

---

## Thank You!
