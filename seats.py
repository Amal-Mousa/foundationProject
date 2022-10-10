print('''-WELCOME TO SHUTTLE BUSES COMPANY 🤩🚇
-BOOK YOUR SEAT BEFORE GETTING OUT OF YOUR HOME
-FEEL FREE TO INQUIRE US ANYTIME 😍😍😍...

-Here is all the busses and their seats you can know the available seat and book it 
''')

seats = []
# BookSeat = int(input('Choose a free seats from 1 to 32: '))
# Here is the buses class
class Buses:

    " All Buses information "
    def __init__(self, number, From, To, seats):
        self.number = number
        self.From = From
        self.To = To
        self.seats = seats

    'Here is the bus seats'
    for s in range(32):
        seats.append(s + 1)
        if seats[s] == 4 or \
                seats[s] == 10 or \
                seats[s] == 28 or \
                seats[s] == 20 or \
                seats[s] == 11 or \
                seats[s] == 17 or \
                seats[s] == 7 or \
                seats[s] == 14 or \
                seats[s] == 23 or \
                seats[s] == 32 or \
                seats[s] == 1:
            seats[s] = [s+1]
        else:
            seats[s] = s+1

    'Here is the user interactions'
    BookBus = " "
    # There is a problem in this function I didn't know it...🤔
    # def User(self):
    #     self.BookBus = input('Enter the Bus number: ')
    #     for x in range(len(objects)):
    #         if objects[x].number == self.BookBus:
    #             self.BookBusSeat = int(input('Enter the seat number: '))
    #             if self.BookBusSeat > 32:
    #                 print('There is no seat hold this number.')
    #             elif self.BookBusSeat <= 32:
    #                 # if objects[x].seats[self.num] == :
    #
    #                 # if objects[x].seats.seats[s] :
    #                 print('Available seat')
    #
    #         # else:
    #         #     print('Not Found')
    #     # for bus in objects:
    #     #     return  objects.append()


# Buses class objects
obj = Buses('Bus 3', 'Turkey', 'USA', seats)
obj1 = Buses('Bus 1', 'USA', 'Kanda', seats)
obj2 = Buses('Bus 2', 'Egypt', 'Emairate', seats)
obj3 = Buses('Bus 4', 'UK', 'Andonisia', seats)

# store buses information
objects = [
    [obj.number, obj.seats, obj.From, obj.To],
    [obj1.number, obj1.seats, obj1.From, obj1.To],
    [obj2.number, obj2.seats, obj2.From, obj2.To],
    [obj3.number, obj2.seats, obj3.From, obj3.To]
]

# print buses information
for n in obj, obj1, obj2, obj3:

    print('''The Bus number is''', n.number)
    print('''From: ''', n.From)
    print('''To: ''', n.To)
    print('''The seats is: ''', n.seats)
    print("=============================================")

print(objects[1][1][1])

BusNum = input('Enter Bus number: ')

ExistBus = 'Exist Bus'
NotExistBus = 'This Bus is not Exist'
def user():
    if objects[0][0] == BusNum:
        BookSeat = int(input('Enter the number of the seat between 1 and 32: '))
        if  BookSeat == 4 or \
            BookSeat == 10 or \
            BookSeat == 28 or \
            BookSeat == 20 or \
            BookSeat == 11 or \
            BookSeat == 17 or \
            BookSeat == 7 or \
            BookSeat == 14 or \
            BookSeat == 23 or \
            BookSeat == 32 or \
            BookSeat == 1:
            print('This seat was alredy booked')
        else:

            seats[BookSeat-1] = [BookSeat]
            print('Booked Went successfully!')
            print(objects[0][0])
            print(objects[0][1])
            print(objects[0][2])
            print(objects[0][3])

    elif objects[1][0] == BusNum:
        BookSeat = int(input('Enter the number of the seat between 1 and 32: '))
        if BookSeat == 4 or \
                BookSeat == 10 or \
                BookSeat == 28 or \
                BookSeat == 20 or \
                BookSeat == 11 or \
                BookSeat == 17 or \
                BookSeat == 7 or \
                BookSeat == 14 or \
                BookSeat == 23 or \
                BookSeat == 32 or \
                BookSeat == 1:
            print('This seat was alredy booked')

        else:

            seats[BookSeat - 1] = [BookSeat]
            print('Booked Went successfully!')
            print(objects[1][0])
            print(objects[1][1])
            print(objects[1][2])
            print(objects[1][3])

    elif objects[2][0] == BusNum:
        BookSeat = int(input('Enter the number of the seat between 1 and 32: '))
        if BookSeat == 4 or \
                BookSeat == 10 or \
                BookSeat == 28 or \
                BookSeat == 20 or \
                BookSeat == 11 or \
                BookSeat == 17 or \
                BookSeat == 7 or \
                BookSeat == 14 or \
                BookSeat == 23 or \
                BookSeat == 32 or \
                BookSeat == 1:
            print('This seat was alredy booked')

        else:

            seats[BookSeat - 1] = [BookSeat]
            print('Booked Went successfully!')
            print(objects[2][0])
            print(objects[2][1])
            print(objects[2][2])
            print(objects[2][3])

    elif objects[3][0] == BusNum:
        BookSeat = int(input('Enter the number of the seat between 1 and 32: '))

        if BookSeat == 4 or \
                BookSeat == 10 or \
                BookSeat == 28 or \
                BookSeat == 20 or \
                BookSeat == 11 or \
                BookSeat == 17 or \
                BookSeat == 7 or \
                BookSeat == 14 or \
                BookSeat == 23 or \
                BookSeat == 32 or \
                BookSeat == 1:
            print('This seat was alredy booked')

        else:

            seats[BookSeat - 1] = [BookSeat]
            print('Booked Went successfully!')
            print(objects[3][0])
            print(objects[3][1])
            print(objects[3][2])
            print(objects[3][3])

    else:
        print(NotExistBus)
        # BusNum = input('Enter Bus Number: ')
        # user()


user()
# num = 0
# while num<4:
#     if objects[num][0] == BusNum:
#         print('exist bus')
#     else:
#         print('This bus is not exist')
#
#     num+=1
# for nums in range(len(objects)):
#     if objects[nums][0] == BusNum:
#         print('EXIST BUS')
#
#     else:
#         print('THIS BUS IS NOT EXIST')


# BookSeat = int(input('Choose another free seat: '))
# def BookingSeat():
#     BookSeat = int(input('Choose a free seat from 1 to 32: '))
#     i = 0
#     while True:
#         if (objects[0][1][i] == [BookSeat] or
#         objects[1][1][i] == [BookSeat] or
#         objects[2][1][i] == [BookSeat] or
#         objects[3][1][i] == [BookSeat]):
#             print('This seat is already booked')
#
#
#         elif (objects[0][1][i] == BookSeat or
#         objects[1][1][i] == BookSeat or
#         objects[2][1][i] == BookSeat or
#         objects[3][1][i] == BookSeat):
#             print('Successfully booked!')
#
#
#         else:
#             break
#
#         i+=1

# def BookingSeat():
#     BookSeat = int(input('Choose a free seats from 1 to 32: '))
#     if BookSeat <=32 :
#         for b in range(len(n.seats)):
#             if (objects[0][1][b] == [BookSeat] or
#                     objects[1][1][b] == [BookSeat] or
#                     objects[2][1][b] == [BookSeat] or
#                     objects[3][1][b] == [BookSeat]):
#                 print('This seat is already booked')
#                 BookSeat = int(input('Choose another free seat: '))
#
#             elif (objects[0][1][b] == BookSeat):
#                 print('This seat is already booked')
#                 BookSeat = int(input('Choose another free seat: '))
#
#     elif BookSeat > 32:
#         print('Choose a free seats between 1 and 32')
#         BookSeat = int(input('Choose a free seat between 1 to 32: '))
#
#     else:
#         print('Someting went wrong, try to book again')



# def BookBus():
#     BookBus = input('Enter Bus number: ')
#     for b in range(len(objects)):
#         if objects[b][0] == BookBus:
#             BookingSeat()
#         # else:
#         #     print('This Bus number is not exist')
#             # BookBus = input('Enter Bus number: ')
#             # for b in range(len(objects)):
#             #     if objects[b][0] == BookBus:
#             #         BookingSeat()


# BookBus()
