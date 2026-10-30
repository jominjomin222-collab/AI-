
# Vacuum Cleaner Problem

def vacuum_cleaner():
    room = {
        'A': 'Dirty',
        'B': 'Dirty'
    }

    location = 'A'

    while 'Dirty' in room.values():

        print("Vacuum is in room", location)

        if room[location] == 'Dirty':
            print("Room", location, "is Dirty")
            room[location] = 'Clean'
            print("Cleaning room", location)

        else:
            print("Room", location, "is already Clean")

        if location == 'A':
            location = 'B'
        else:
            location = 'A'

    print("\nAll rooms are clean!")
    print("Final Room Status:", room)


# Main Program
vacuum_cleaner()
