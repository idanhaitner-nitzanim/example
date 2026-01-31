class Content:
    def __init__(self, content_name, content_creator, genre):
        self.content_name = content_name
        self.content_creator = content_creator
        self.set_genre(genre)
        self.number_of_views = 0
        self.list_of_ratings = []

    def set_genre(self, genre):
        if genre not in ["Comedy","Horror","Drama"]:
            print("Gnere can only be one of the list")
            return False
        self.genre = genre
        return True

    def add_rating(self, rating)
        self.list_of_ratings.append(rating)

    def get_average_rating(self):
        num_of_ratings = len(self.list_of_ratings)
        if num_of_ratings > 0:
            return sum(self.list_of_ratings) / len(self.list_of_ratings)
        return 0

class Viewer:
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.listOfViewed = []
        self.listOfRated = []

    def rate_content(self,content: Content, rating):
        if rating < 0 or rating > 5:
            print("Rating must be between 0 and 5")
            return False
        if content in self.listOfRated:
            print("Content has already been rated")
            return False
        self.listOfRated.append(content)
        content.add_rating(rating)
        return True



class Creator(Viewer):
    def __init__(self, user_name, user_id):
        super().__init__(user_name, user_id)
        self.listOfUploads = []
        self.limit = 10

    def upload_content(self, content):
        if len(self.listOfUploads) < self.limit:
            if content in self.listOfUploads:
                print("Cannot upload this content twice")
                return False
            else:
                self.listOfUploads.append(content)
                return True
        else:
            print("Cannot upload more than 10 contents")
            return False

class PlatformManager(Creator):
    def __init__(self, user_name, user_id):
        super().__init__(user_name, user_id)
        self.listOfCreators = []
        self.limit = 20

    def get_details(self):
        print(self.user_name)
        for creator in self.listOfCreators:
            print(f"Creator ${creator.user_name} uploaded ${len(creator.listOfUploads)} videos")

