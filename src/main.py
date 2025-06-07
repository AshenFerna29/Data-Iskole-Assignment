#imports
from loader import load_superheroes, load_links
from analyzer import *
from interact import handle_user_interaction
import os

#main function
def main():
    try:
        os.system("clear" if os.name == "posix" else "cls")
        print(" Welcome to the Superhero Universe Network\n")

        
        heroes = load_superheroes("data/superheroes.csv")
        links = load_links("data/links.csv")

        
        try:
            total_heroes, total_links = get_total_counts(heroes, links)
            print(f" Total Superheroes: {total_heroes}")
            print(f" Total Connections: {total_links}\n")
        except Exception as e:
            print(f" Failed to compute totals: {e}")

        # Recently added heroes
        print(" Recently Added Superheroes (last 3 days):")
        try:
            recent_heroes = get_recent_heroes(heroes)
            if recent_heroes.empty:
                print("  - No recent heroes found.")
            else:
                for _, row in recent_heroes.iterrows():
                    print(f"  - {row['name']} (Added: {row['created_at']})")
        except Exception as e:
            print(f" Error displaying recent heroes: {e}")

        # Most connected heroes
        print("\n Most Connected Superheroes:")
        try:
            most_connected = get_most_connected(links, heroes)
            if not most_connected:
                print("  - No connection data available.")
            else:
                for name, id_, count in most_connected:
                    print(f"  - {name} (ID: {id_}) with {count} connections")
        except Exception as e:
            print(f" Error finding most connected heroes: {e}")
        # Info about 'dataiskole'
        print("\n Info on 'dataiskole':")
        try:
            added_on, friends = get_dataiskole_info(heroes, links)
            if added_on:
                print(f"  - Added on: {added_on}")
                print("  - Friends:")
                if friends:
                    for friend in friends:
                        print(f"    - {friend}")
                else:
                    print("    - No friends found.")
            else:
                print("  - 'dataiskole' not found.")
        except Exception as e:
            print(f" Error fetching 'dataiskole' info: {e}")

        # User interaction (add/delete/graph)

        try:
            heroes, links = handle_user_interaction(heroes, links)
        except Exception as e:
            print(f" Error in user interaction: {e}")

    except Exception as e:
        print(f"\n Unexpected error occurred in main program: {e}")

if __name__ == "__main__":
    main()
