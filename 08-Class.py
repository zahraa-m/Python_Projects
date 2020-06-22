#define a class called movies

class Movies(object):
    def __init__(self, name, year, type):
        self.name=name;
        self.year=year;
        self.type=type;

    def movie_f(self):
        print("Movie name:", self.name)
        print("Release year:", self.year)
        print("Movie type:", self.type)


#create an object

my_movie=Movies("Pride and Prejudice", 2005, "Romance and Drama")
my_movie.movie_f()