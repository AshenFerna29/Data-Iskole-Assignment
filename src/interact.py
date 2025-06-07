# src/interact.py
import pandas as pd
from datetime import datetime
from loader import load_superheroes, load_links
from fileops import save_superheroes, save_links

def add_superhero(heroes_df, links_df):
    try:
        while True:
            name = input("Enter new superhero's name: ").strip()
            if not name:
                print(" Name cannot be empty.")
                continue

            clean_names = heroes_df['name'].str.lower().str.replace(" ", "").str.replace("-", "")
            if name.lower().replace(" ", "").replace("-", "") in clean_names.values:
                print(" That superhero already exists! Try another name.")
                continue

            break  

        new_id = heroes_df['id'].max() + 1 if not heroes_df.empty else 1
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_hero = pd.DataFrame([{'id': new_id, 'name': name.title(), 'created_at': created_at}])
        heroes_df = pd.concat([heroes_df, new_hero], ignore_index=True)
        print(f" Superhero '{name}' added with ID {new_id}.")

        while True:
            conn = input("Do you want to add a connection? (YES/NO): ").strip().upper()
            if conn == "NO":
                break
            elif conn != "YES":
                print("Please type YES or NO.")
                continue

            try:
                print(heroes_df[['id', 'name']].to_string(index=False))
                target_id = int(input("Enter ID to connect with: "))
                if target_id not in heroes_df['id'].values:
                    print(" Invalid ID. No superhero found with that ID.")
                    continue
                new_link = pd.DataFrame([{'source': new_id, 'target': target_id}])
                links_df = pd.concat([links_df, new_link], ignore_index=True)
                print(f" Connection added between {new_id} and {target_id}.")
            except ValueError:
                print(" Please enter a valid numeric ID.")
    except Exception as e:
        print(f" Error while adding superhero: {e}")

    return heroes_df, links_df


def delete_superhero(heroes_df, links_df):
    try:
        print("Only superheroes with ID > 11 can be deleted.")
        deletable = heroes_df[heroes_df['id'] > 11]
        if deletable.empty:
            print("No deletable superheroes found.")
            return heroes_df, links_df

        print(heroes_df[['id', 'name']].to_string(index=False))

        while True:
            try:
                del_id = int(input("Enter ID to delete: "))
                if del_id <= 11:
                    print(" This ID is protected and cannot be deleted.")
                elif del_id not in heroes_df['id'].values:
                    print(" Superhero ID not found.")
                else:
                    name = heroes_df[heroes_df['id'] == del_id]['name'].values[0]
                    heroes_df = heroes_df[heroes_df['id'] != del_id]
                    links_df = links_df[(links_df['source'] != del_id) & (links_df['target'] != del_id)]
                    print(f" Deleted superhero '{name}' and all associated connections.")
                    break  
            except ValueError:
                print(" Invalid input. Please enter a valid numeric ID.")
    except Exception as e:
        print(f" Error while deleting superhero: {e}")

    return heroes_df, links_df


def handle_user_interaction(heroes, links):
    try:
        while True:
            action = input("Do you want to ADD or DELETE a superhero? (ADD/DELETE/SKIP): ").strip().upper()

            if action == "ADD":
                heroes, links = add_superhero(heroes, links)
            elif action == "DELETE":
                heroes, links = delete_superhero(heroes, links)
            elif action == "SKIP" or action == "":
                break
            else:
                print(" Invalid option. Please choose ADD, DELETE, or SKIP.")
                continue

            try:
                save_superheroes(heroes)
                save_links(links)
            except Exception as save_err:
                print(f" Failed to save files: {save_err}")

    except Exception as e:
        print(f" Unexpected error in user interaction: {e}")

    # Ask once after all interaction
    show = input("Do you want to display the superhero graph? (YES/NO): ").strip().upper()
    if show == "YES":
        try:
            from visualizer import show_graph
            show_graph(heroes, links)
        except ImportError:
            print(" Could not import visualizer module.")
        except Exception as vis_err:
            print(f" Error displaying graph: {vis_err}")

    return heroes, links

