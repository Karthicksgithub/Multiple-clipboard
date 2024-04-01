import sys
import clipboard
import json
import os

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in clipboard file.")
        return {}
    except Exception as e:
        print("An error occurred:", e)
        return {}

def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]
        data = load_data(SAVED_DATA)

        if command == "save":
            key = input("Enter a key: ")
            if key in data:
                overwrite = input("Key already exists. Do you want to overwrite it? (y/n): ")
                if overwrite.lower() != "y":
                    print("Save operation canceled.")
                    return
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
            print("Data saved!")
        elif command == "load":
            key = input("Enter a key: ")
            if key in data:
                clipboard.copy(data[key])
                print("Data copied to clipboard.")
            else:
                print("Key does not exist.")
        elif command == "list":
            print(data)
        else:
            print("Unknown command")
    else:
        print("Please pass exactly one command.")

if __name__ == "__main__":
    main()
