from datetime import datetime


class FbPost:
    TEXT_LIMIT = 10

    def __init__(self, author):
        self.author = author
        self.post_time = datetime.now()
        self.post_txt = input("wpisz tresc posta: ")
        if len(self.post_txt) > self.TEXT_LIMIT:
            raise ValueError("za długi post")
        self.likes = 0
        self.edited = 0

    def view_post(self):
        print(f"autor: {self.author} post date: {self.post_time} \n {self.post_txt} \n likes: {self.likes}   times edited: {self.edited}")  

    def like_post(self):
        self.likes +=1

    def edit_post(self):
        print(f"Edytujesz post z {self.post_time}: \n {self.post_txt}")
        self.post_txt = input("Nowa tresc posta:")
        self.edited += 1
    
    def __str__(self):
        return f"{self.post_txt} by {self.author}"

if __name__ == "__main__":
    p1 = FbPost("Andrzej")
    p1.view_post()
    p1.like_post()
    p1.like_post()
    p1.edit_post()
    p1.view_post()


    

    