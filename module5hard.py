from time import sleep
class UrTube():
    users = []
    videos =[]
    current_user = None
    def log_in(self, nickname, password):
        for _ in self.users:
            if (_.nickname.upper() == nickname.upper()
                    and _.password == hash(password)):
                self.current_user = _
        #if self.current_user == None:
            #print ("Need to register ", nickname)
    def register(self, nickname, password, age):
        found=0
        for _ in self.users:
            if _.nickname.upper()==nickname.upper():
                print (f"Пользователь {nickname} уже существует")
                found=1
                break
        if found == 0:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
            #print (f'Зарегистрирован {nickname}')

    def log_out(self):
        self.current_user = None

    def add(self,*video):
       for _ in video:
            if _ not in self.videos:
                self.videos.append(_)

    def get_videos(self,keyword):
        for_return=[]
        for _ in self.videos:
            if _.title.upper().__contains__(keyword.upper()) :
            #if _.title.upper().find(keyword.upper()) > -1:
               for_return.append(_.title)
        return for_return

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for _ in self.videos:
            if title.upper() == _.title.upper():
                if _.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:
                    for _.time_now  in range(0,_.duration):
                        _.time_now+=1
                        print(_.time_now, end=' ')
                        sleep(1)
                    print(" Конец видео")
                    _.time_now=0
                    return
        print(f'Видео {title} не существует')

class Video():
    def __init__(self, title, duration, time_now=0,
                 adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

class User():
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
