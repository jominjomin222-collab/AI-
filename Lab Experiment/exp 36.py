
print("SENTIMENT ANALYSIS USING NLP")

positive = ["good", "happy", "excellent", "great", "love"]
negative = ["bad", "sad", "poor", "hate", "worst"]

text = input("Enter a sentence: ")

text = text.lower()
words = text.split()

p = 0
n = 0

for word in words:

    if word in positive:
        p = p + 1

    if word in negative:
        n = n + 1

print("Positive words:", p)
print("Negative words:", n)

if p > n:
    print("Sentiment is Positive")

elif n > p:
    print("Sentiment is Negative")

else:
    print("Sentiment is Neutral")
