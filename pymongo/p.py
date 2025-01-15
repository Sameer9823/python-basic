import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video['name']} and Time: {video['time']} ")
        
    

def add_video(name, time):
    video_collection.insert_one({"name":name, "time":time})

def update_video(videoId,newname, new_time):
    video_collection.update_one({"_id":ObjectId(videoId)}, {"$set": {"name": newname, "time":new_time}})

def delete_video(videoId):
    video_collection.delete_one({"_id": ObjectId(videoId)})

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

if __name__ == "__main__":
    main()