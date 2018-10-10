from tabulate import tabulate

def import_albums_file(filename="text_albums_data.txt"):
    album = []
    file = open(filename, 'r')
    line = file.readlines()
    for f in line:
        album.append(f.split(','))
    return album


print(import_albums_file())


list = import_albums_file()

lower_time_limit = (input('insert lower time limit: '))
upper_time_limit = (input('upper time limit: '))
lower_time_limit = lower_time_limit.split(':')
lower_time_limit = int(lower_time_limit[0] + lower_time_limit[1])
upper_time_limit = upper_time_limit.split(':')
upper_time_limit = int(upper_time_limit[0] + upper_time_limit[1])

def show_longest_shortest(albums):  
    albums_by_the_length = []
    for x in list:
            y = x[4].split(':')
            time = y[0] + y[1]
            time = int(time.strip())
            if time < upper_time_limit and time > lower_time_limit:
                albums_by_the_length. append(x)
                return albums

 
print(tabulate(show_longest_shortest(list), ['Artist', 'Album', 'Year', 'Genre', 'Length']))


                