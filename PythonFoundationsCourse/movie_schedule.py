
current_movies = {'The Grinch': '11:00am',
                  'Rudolph': '1:00pm', 
                  'Frosty the Snowman': '3:00pm',
                  'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
# key here is the key of the key-value pair
for key in current_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

# returns the value for the key specified 
showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', showtime)