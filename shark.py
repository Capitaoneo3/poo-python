class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 0
   
    def __init__(self,name_p,age_p):
        self.name = name_p
        self.age = age_p

    def set_followers(self,followers_p):
        self.followers = followers_p
        print(f"Esse usuário tem {self.followers} seguidores")
    def set_name(self,name_p):
        self.name = name_p
    #faça um método que modifique o nome do tubarão
    #faça um método que apague todas as informações do tubarão
    def clean_all(self):
        self.animal_type = ""
        self.location = ""
        self.followers = 0
        self.age = 0
        self.name = ""
        print("tudo foi limpo")
        
new_shark = Shark("Joshi",20)
print(new_shark.name)
print(new_shark.age)

new_shark.clean_all()

print(new_shark.name)
print(new_shark.age)
