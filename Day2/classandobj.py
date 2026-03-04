# Class and Object Example using Instagram Reels

class Instagram:
    def __init__(self, title, description, creator_name, location):
        self.title = title                   
        self.description = description        
        self.creator_name = creator_name     
        self.location = location              
        self.likes = 0                        
        self.comments = []                    

    #methods
    def display_title(self):
        print("The title of the reel is:", self.title)

    def display_description(self):
        print("The description of the reel is:", self.description)

    def display_creator(self):
        print("The creator of the reel is:", self.creator_name)

    def display_location(self):
        print("The location of the reel is:", self.location)

    def display_likes(self):
        print("The likes of the reel is:", self.likes)

    def display_comments(self):
        print("Comments on the reel:")
        for comment in self.comments:
            print("-", comment)

    def liked(self):
        self.likes += 1

    def disliked(self):
        if self.likes > 0:
            self.likes -= 1

    def add_comment(self, comment):
        self.comments.append(comment)
    
    def delete_last_comment(self):
        if self.comments:
            temp_delete = self.comments.pop()
            print("Deleted comment:", temp_delete)
        else:
            print("No comments to delete")

# objects
reel1 = Instagram(
    "Dancing",
    "Dancing with friends",
    "Ramya",
    "Bangalore"
)

reel2 = Instagram(
    "Finance Minister Conference",
    "Finance minister conference with friends",
    "Ananya",
    "Delhi"
)

reel1.disliked()        #0
reel1.liked()           #1
reel1.liked()           #2
reel1.add_comment("Nice dance!")
reel1.add_comment("Amazing energy!")

reel2.liked()           #1
reel2.add_comment("Very informative")

reel1.display_likes()
reel2.display_likes()

reel1.display_creator()
reel1.display_location()
reel1.display_comments()
reel1.delete_last_comment()
 
print(id(reel1))
print(id(reel2))
