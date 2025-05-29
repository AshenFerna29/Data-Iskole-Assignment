# Imports
import pandas as pd
from datetime import datetime, timedelta
from collections import Counter


# Load CSV data
superheroes_data = pd.read_csv("superheroes.csv", dtype={'id': int})
links_data = pd.read_csv("links.csv", dtype={'source': int, 'target': int})


print("---------- Welcome to Superhero Universe Network ----------\n")


superheroes_data['created_at'] = pd.to_datetime(superheroes_data['created_at'], errors='coerce')

# Total superheroes and connections
print(f"The total number of the Superheroes: {len(superheroes_data)}")
print(f"The total number of connections: {len(links_data)}")

print("\n----------------\n")

# Most recently added superheroes 
newest_heroes = superheroes_data.nlargest(3, 'created_at')
print("Most recently added heroes:")
print(newest_heroes[['name', 'created_at']].to_string(index=False))

print("\n----------------\n")

# Top  most connected superheroes
connections = pd.concat([links_data['source'], links_data['target']])
top_connections = Counter(connections).most_common(3)
print("The Most Connected Superheroes:")
for hero_id, count in top_connections:
    hero_row = superheroes_data[superheroes_data['id'] == hero_id]
    if not hero_row.empty:
        hero_name = hero_row.iloc[0]['name']
        print(f"{hero_name} (ID: {hero_id}) -- {count} Connections")
    else:
        print(f"Unknown Hero (ID: {hero_id}) -- {count} Connections")

print()

# Info about superhero 'dataiskole'
info_dataiskole = superheroes_data[superheroes_data['name'].str.lower() == 'dataiskole']
if not info_dataiskole.empty:
    dataiskole_id = info_dataiskole.iloc[0]['id']
    print(f"Dataiskole was added on: {info_dataiskole.iloc[0]['created_at']}")

    friends_from = links_data[links_data['source'] == dataiskole_id]['target']
    friends_to = links_data[links_data['target'] == dataiskole_id]['source']
    friend_ids = pd.concat([friends_from, friends_to]).unique()
    friend_names = superheroes_data[superheroes_data['id'].isin(friend_ids)]['name'].tolist()

    if friend_names:
        print("Friends of 'dataiskole':\n", '\n '.join(friend_names))
    else:
        print("Friends of 'dataiskole': None")
else:
    print("Dataiskole is not found in the superhero list.")

print("\n----------------\n")

# Add new superheroes
while True:
    add_hero = input("Would you like to add a new Superhero? (YES/NO): ").upper().strip()
    
    if add_hero == "YES":
        while True:
            new_name = input("Enter your new Superhero's name: ").strip()

            
            normalized_input = new_name.lower().replace(" ", "").replace("-", "")

            
            normalized_existing = superheroes_data['name'].str.lower().str.replace(" ", "").str.replace("-", "")

            if normalized_input in normalized_existing.values:
                print(f" A superhero similar to '{new_name}' already exists. Please enter a more distinct name.\n")
            else:
                
                new_name = new_name.title().strip()
                break

        new_id = int(superheroes_data['id'].max()) + 1
        new_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Add new superhero
        new_hero = pd.DataFrame([{
            'id': new_id,
            'name': new_name,
            'created_at': new_date
        }])
        superheroes_data = pd.concat([superheroes_data, new_hero], ignore_index=True)
        superheroes_data.to_csv('superheroes.csv', index=False)
        print(f"\n The new Superhero '{new_name}' is added with ID {new_id} on {new_date}\n")

        # Add connections
        new_connection = input(f"Do you want to add a connection to {new_name}? (YES/NO): ").upper().strip()
        while new_connection == "YES":
            try:
                print("Available Superheroes:")
                print(superheroes_data[['id', 'name']].to_string(index=False))

                target_id = int(input("Enter the ID of the superhero you want to connect with: "))
                if target_id in superheroes_data['id'].values:
                    new_link = pd.DataFrame([{'source': int(new_id), 'target': int(target_id)}])
                    links_data = pd.concat([links_data, new_link], ignore_index=True)
                    links_data.to_csv('links.csv', index=False)
                    print(f" Connection added between {new_name} and ID {target_id}.\n")
                else:
                    print(" That ID does not exist. Please enter a valid ID.\n")
            except ValueError:
                print(" Invalid input. Please enter a number.\n")

            new_connection = input("Do you want to add another connection? (YES/NO): ").upper().strip()

        break

    elif add_hero == "NO":
        print("Exiting superhero addition mode...\n")
        break
    else:
        print(" Invalid input. Please enter YES or NO.\n")


# ODeleting section
print("\n----------------\n")
delete_choice = input("Would you like to delete a superhero you added? (YES/NO): ").upper().strip()

if delete_choice == "YES":
    while True:
        try:
            print("\nOnly superheroes with ID greater than 11 can be deleted.")
            deletable_heroes = superheroes_data[superheroes_data['id'] > 11]

            if deletable_heroes.empty:
                print(" No user-added superheroes found to delete.")
                break

            print("Available Superheroes:")
            print(deletable_heroes[['id', 'name']].to_string(index=False))

            delete_id = int(input("\nEnter the ID of the superhero you want to delete: "))

            if delete_id <= 11:
                print(" You are not allowed to delete superheroes with ID 11 or below.\nPlease try again.\n")
                continue
            elif delete_id not in superheroes_data['id'].values:
                print(" That ID does not exist.\nPlease try again.\n")
                continue
            else:
                
                name_to_delete = superheroes_data[superheroes_data['id'] == delete_id].iloc[0]['name']
                superheroes_data = superheroes_data[superheroes_data['id'] != delete_id]
                superheroes_data.to_csv('superheroes.csv', index=False)

                
                links_data = links_data[(links_data['source'] != delete_id) & (links_data['target'] != delete_id)]
                links_data.to_csv('links.csv', index=False)

                print(f"\n Superhero '{name_to_delete}' (ID: {delete_id}) and all related connections were successfully deleted.\n")
                print("---- Remaining super heroes ---- ")
                print(superheroes_data[['id', 'name']].to_string(index=False))
                break  

        except ValueError:
            print(" Invalid input. Please enter a numeric ID.\n")

else:
    print("No deletion performed. Exiting program.\n")

