import yaml

users = [
    {
        "userid":"Userid1",
        "username":"User1",
        "email":"user1@xyz.com",
        "password":"user1@test"
    },
    {
        "userid":"Userid2",
        "username":"User2",
        "email":"user2@xyz.com",
        "password":"user2@test"
    },
    {
        "userid":"Userid3",
        "username":"User3",
        "email":"user3@xyz.com",
        "password":"user3@test"
    }
]

advisors = [
    {
        "advisorid":"Advisorid1",
        "advisorname":"Advisor1",
        "advisorpic":"Advisor1_Image"
    },
    {
        "advisorid":"Advisorid2",
        "advisorname":"Advisor2",
        "advisorpic":"Advisor2_Image"
    },
    {
        "advisorid":"Advisorid3",
        "advisorname":"Advisor3",
        "advisorpic":"Advisor3_Image"
    }
]

bookings = []

with open("users.yaml", 'w') as userfile:
    data = yaml.dump(users, userfile)
    print(data)
    print("Write successful")
    userfile.close()

with open("advisors.yaml", 'w') as advisorfile:
    data = yaml.dump(advisors, advisorfile)
    print(data)
    print("Write successful")
    advisorfile.close()

with open("bookings.yaml", 'w') as bookingfile:
    data = yaml.dump(bookings, bookingfile)
    print(data)
    print("Write successful")
    bookingfile.close()