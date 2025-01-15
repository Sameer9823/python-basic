import json

def load_data():
    try:
        with open("videos.txt", "r") as file:
            test = json.load(file)
            # print(type (test))
            return test
        
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("videos.txt", "w") as file:
        json.dump(videos, file)
    
    
    
def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: ({video['time']})")
    
    print("*" * 50)
def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    update = int(input("Enter the number of the video you want to update: "))
    if 1 <= update <= len(videos):
        name = input("Enter the new name of the video: ")
        time = input("Enter the new time of the video: ")
        videos[update - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid video number.")

def delete_video(videos):
    list_all_videos(videos)
    delete = int(input("Enter the number of the video you want to delete: "))
    if 1 <= delete <= len(videos):
        del videos[delete - 1]
        save_data_helper(videos)
    else:
        print("Invalid video number.")


        
def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager | Choose an option:")
        print("1. List favourite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    main()

