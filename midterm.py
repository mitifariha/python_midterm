class Star_Cinema:
    hall_list=[]


    @classmethod
    def entry_hall(cls,rows, cols, hall_no):
        hall= Hall(rows,cols,hall_no)
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.seats={}
        self.show_list=[]
        Hall.hall_list.append(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        seats = [[('free') for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seats


    def book_seats(self, id, seats):
        if id in self.seats:
            for seat in seats:
                row, col = seat
                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print(f"Seat ({row}, {col}) is not available.")
                    continue
                if self.seats[id][row][col] == 'free':
                    self.seats[id][row][col] = 'booked'
                    print(f"Seat ({row}, {col}) successfully booked!")
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
        else:
            print('ID does not valid.')

    
    def view_show_list(self):
        print("Shows running:")
        for show in self.show_list:
            print(f"MovieId: {show[0]}, MovieName: {show[1]}, ShowTime: {show[2]}")
    

    def view_available_seats(self,id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col] == 'free':
                        print(f"Seat ({row}, {col})")
        else:
            print(f"Show with ID {id} does not exist.")

class Counter:
    __total_revenue = 1000
    
    def __init__(self, hall):
        self.hall = hall

    def view_all_shows(self):
        self.hall.view_show_list()

    def view_available_seats_in_show(self, id):
        self.hall.view_available_seats(id)


    def book_tickets(self, id, seat_list):
        self.hall.book_seats(id, seat_list)



h1 = Hall(2,2,1)

h1.entry_show('1', "Modhubala", "3:00")
h1.entry_show('2', "Pathan", "7:00")
h1.entry_show('3', "Tiger", "1:00")


h1.view_show_list()
h1.book_seats('1',[(0, 0)])
print(h1.seats)
h1.book_seats('2',[(0, 2)])
h1.view_available_seats('1')
counter1 = Counter(h1)

run = True
while run:
    print("\n1. View All Shows")
    print("2. View Available Seats")
    print("3. Book Tickets ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        counter1.view_all_shows()
    elif choice == "2":
        id = input("Enter the show ID: ")
        counter1.view_available_seats_in_show(id)

    elif choice == "3":
        show_id = input("Enter the show ID: ")
        seat_list = (input("Enter the seat Numer as row and colum : For Example [(0, 1)]"))
        counter1.book_tickets(show_id, seat_list)
    elif choice == "4":
        print("Exiting")
        run = False
        break
    else:
        print("Invalid. Please try again.")