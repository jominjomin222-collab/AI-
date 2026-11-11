
# Forward Chaining Algorithm

# Initial facts
facts = ["sunny", "warm", "rain"]

# Rules
rules = [
    (["sunny", "warm"], "can_go_out"),
    (["rain"], "carry_umbrella"),
    (["sunny", "warm"], "good_weather")
]

print("FORWARD CHAINING")
print("-------------------------")

print("Initial Facts:", facts)

# Forward chaining process
changed = True

while changed:
    changed = False

    for conditions, result in rules:
        if all(condition in facts for condition in conditions):
            if result not in facts:
                facts.append(result)
                print("New Fact Added:", result)
                changed = True

print("-------------------------")
print("Forward Chaining Completed")

# Display all facts
print("Final Facts:", facts)
