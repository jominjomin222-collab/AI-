
# Backward Chaining Algorithm

# Initial Facts
facts = ["sunny", "warm", "rain"]

# Rules
rules = {
    "can_go_out": ["sunny", "warm"],
    "carry_umbrella": ["rain"],
    "good_weather": ["sunny", "warm"]
}

# Backward Chaining Function
def prove(goal):
    if goal in facts:
        return True

    if goal in rules:
        conditions = rules[goal]

        for condition in conditions:
            if not prove(condition):
                return False

        return True

    return False


# Main Program
print("BACKWARD CHAINING")
print("----------------------")

goal = input("Enter the goal: ").lower()

if prove(goal):
    print("Goal is proved.")
else:
    print("Goal cannot be proved.")
