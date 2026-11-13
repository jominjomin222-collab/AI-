
# Recommendation System using Collaborative Filtering

ratings = {
    "User1": [5, 4, 1],
    "User2": [4, 5, 1],
    "User3": [1, 2, 5]
}

movies = ["Movie1", "Movie2", "Movie3"]

print("MOVIE RECOMMENDATION SYSTEM")

user = input("Enter user name (User1/User2/User3): ")

if user in ratings:

    print("Recommendations for", user)

    user_ratings = ratings[user]

    scores = [0, 0, 0]

    for other in ratings:

        if other != user:

            other_ratings = ratings[other]

            similarity = 0

            for i in range(3):
                similarity += abs(
                    user_ratings[i] - other_ratings[i]
                )

            similarity = 1 / (1 + similarity)

            for i in range(3):
                if user_ratings[i] == 0:
                    scores[i] += other_ratings[i] * similarity

    print("Recommended Movies:")

    for i in range(3):
        if user_ratings[i] == 0:
            print(movies[i])

    print("Recommendation system completed")

else:
    print("Invalid user name")
