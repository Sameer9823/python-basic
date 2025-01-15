import sqlite3

conn = sqlite3.connect("video.db")

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   duration TEXT NOT NULL
               )
               ''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(videoId,name, time):
    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, time, videoId))
    conn.commit()

def delete_video(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoId,))
    conn.commit()

def main():
    while True:
        print("\nYoutube Manager | Choose an option:")
        print("1. List favourite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            add_video(name, time)
        elif choice == "3":
            videoId = input("Enter the video ID: ")
            name = input("Enter the video name: ")
            time = input("Enter the video duration: ")
            update_video(videoId,name, time)
        elif choice == "4":
            videoId = input("Enter the video ID: ")
            delete_video(videoId)
        elif choice == "5":
            print("Exiting YouTube Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
    conn.close()
            
if __name__ == "__main__":
    main()