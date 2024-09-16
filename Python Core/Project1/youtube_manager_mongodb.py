from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://rupeshthakur:Pythontraining@python.ccl7n.mongodb.net/?retryWrites=true&w=majority&appName=Python")

db = client["youtube_manager"]

video_collection = db["videos"]

def list_all_data():
    print("*"*50)
    for video in video_collection.find({}):
        print(f"ID: {video['_id']}, \tName: {video['name']}, \tTime: {video['time']}")
    print("*"*50)

def add_data(name, time):
    video_collection.insert_one({'name': name, 'time': time})

def update_data(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)}, 
        {'$set': {"name": new_name, "time": new_time}}
    )

def delete_data(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})

def main():
    while True:
        print("\nYoutube Manager using MongoDB")
        print("1. List out youtube manager stored data")
        print("2. Add data into youtube manager")
        print("3. Update youtube manager data using id")
        print("4. Delete youtube manager data using i")
        print("5. Exit youtube manager App")
        choice = input("\nEnter your choise : ")

        match choice:
            case '1': 
                list_all_data()

            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_data(name, time)

            case '3':
                video_id = input("Enter video id: ")
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_data(video_id, name, time)

            case '4':
                video_id = input("Enter video id: ")
                delete_data(video_id)

            case '5':
                exit()
            case _: print("Invalid input please enter valid input")

if __name__ == "__main__":
    main()
