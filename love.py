import time

# Function to print a heart shape using "I love you Sara"
def heart_shape():
    message = "I love you Sara "
    for y in range(15, -15, -1):
        row = ""
        for x in range(-30, 30):
            formula = ((x*0.04)**2 + (y*0.1)**2 - 1)**3 - (x*0.04)**2 * (y*0.1)**3
            if formula <= 0:
                row += message[(x - y) % len(message)]
            else:
                row += " "
        print(row)

# Show the heart once
heart_shape()

print("\nNow my love goes on forever ❤️\n")

# Infinite loop of love
while True:
    print("❤️  I love you Sara ❤️")
    time.sleep(0.5)  # adjust speed
