import matplotlib.pyplot as plt
import numpy as np

# Function to generate a random path for the bomber
def generate_random_path(length=10):
    return np.random.uniform(0, 1000, size=(length,))

# Function to simulate the pure pursuit problem
def pure_pursuit():
    # Generate random paths for the bomber
    x_bomber = generate_random_path()
    y_bomber = generate_random_path()

    # Initialize the position of the fighter and its speed
    xf, yf = np.random.uniform(0, 1000), np.random.uniform(0, 1000)
    fighter_speed = 200

    # Lists to store the positions of the fighter over time
    x_fighter = []
    y_fighter = []

    # Initialize time and set distances for catching and escaping
    time = 0
    escape_distance, caught_distance = 900, 100

    # Simulation loop
    while time < len(x_bomber):
        # Append current position of the fighter to the lists
        x_fighter.append(xf)
        y_fighter.append(yf)

        # Clear the current plot and set the title
        plt.clf()
        plt.title("Simulation of a Pure Pursuit")

        # Plot the path of the fighter and the portion of the bomber's path covered so far
        plt.plot(x_fighter, y_fighter, marker="o", label="Fighter")
        plt.plot(x_bomber[0:time + 1], y_bomber[0:time + 1], marker="o", label="Bomber")

        # Set axis limits, add legend, grid, and pause for visualization
        plt.xlim(0, 1000)
        plt.ylim(0, 1000)
        plt.legend()
        plt.grid()
        plt.pause(1)

        # Calculate the distance between fighter and bomber
        distance = ((xf - x_bomber[time]) ** 2 + (yf - y_bomber[time]) ** 2) ** 0.5

        # Print the output in the desired format
        print(f"time={time}   xf={xf:.2f}  yf={yf:.2f}  xb={x_bomber[time]:.2f}  yb={y_bomber[time]:.2f}  distance={distance:.2f}")

        # Check if the target is caught or escaped
        if distance < caught_distance:
            print(f"The bomber plane caught at {time}th second")
            break
        if distance >= escape_distance:
            print(f"The bomber plane escaped from sight at {time}th second")
            break

        # Calculate sine and cosine for direction
        sin = (y_bomber[time] - yf) / distance
        cos = (x_bomber[time] - xf) / distance

        # Increment time and update fighter's position based on speed and direction
        time += 1
        xf += fighter_speed * cos
        yf += fighter_speed * sin

        if time == len(x_bomber):
            print(f"timed out for {time} seconds!!")

    plt.show()

# Main function to initiate the simulation
def main():
    pure_pursuit()

# Execute the main function if the script is run
if __name__ == "__main__":
    main()
