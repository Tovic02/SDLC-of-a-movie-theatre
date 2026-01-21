class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

class ShowTime:
    def __init__(self, movie, time, total_seats):
        self.movie = movie
        self.time = time
        self.available_seats = total_seats

    def process_booking(self, seats_requested):
        if seats_requested <= self.available_seats:
            self.available_seats -= seats_requested
            return True
        return False

class CinemaBookingSystem:
    def __init__(self):
        self.movies_catalog = []
        self.scheduled_shows = []

    def add_movie(self, title, genre):
        new_movie = Movie(title, genre)
        self.movies_catalog.append(new_movie)
        return new_movie

    def schedule_show(self, movie, time, capacity):
        show = ShowTime(movie, time, capacity)
        self.scheduled_shows.append(show)
        return show

# --- Execution / Demonstration ---
cbs = CinemaBookingSystem()
avatar = cbs.add_movie("Avatar: Way of Water", "Sci-Fi")
evening_show = cbs.schedule_show(avatar, "18:00", 50)

# Implementation of a Booking Request
booking_success = evening_show.process_booking(2)
print(f"Booking Status: {'Confirmed' if booking_success else 'Failed'}")
print(f"Remaining seats for {avatar.title}: {evening_show.available_seats}")
