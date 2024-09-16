import sqlite3

con = sqlite3.connect("youtube_videos.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS youtube_videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM youtube_videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO youtube_videos(name, time) VALUES(?, ?)", (name, time))
    con.commit()

def update_video(videoId, name, time):
    cursor.execute("UPDATE youtube_videos SET name = ?, time = ? WHERE id = ?", (name, time, videoId))
    con.commit()

def delete_video(videoId):
    cursor.execute("DELETE FROM youtube_videos WHERE id = ?", (videoId))
    con.commit()

def main():
    while True:
        print("\nYoutube Manager")
        print("Choose an option from below....")
        print("1. List all youtube youtube_videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the App")
        choice = input("\nEnter your choice: ")

        match choice:
            case '1': 
                list_all_videos()

            case '2':
                name =  input("Enter the video name: ")
                time = input("Enter video time: ")
                add_video(name, time)

            case '3':
                videoId = input("Enter id to update video details : ")
                name =  input("Enter the video name: ")
                time = input("Enter video time: ")
                update_video(videoId, name, time)

            case '4':
                videoId = input("Enter id to delete video details : ")
                delete_video(videoId)
            
            case '5':
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()


