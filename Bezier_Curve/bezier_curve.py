import matplotlib.pyplot as plt

def bezier_curve(x, y, t):
    # Curve formula for 4 control points
    put_x = (1 - t)**3 * x[0] + 3 * t * (1 - t)**2 * x[1] + 3 * t**2 * (1 - t) * x[2] + t**3 * x[3]
    put_y = (1 - t)**3 * y[0] + 3 * t * (1 - t)**2 * y[1] + 3 * t**2 * (1 - t) * y[2] + t**3 * y[3]
    return put_x, put_y

def main():
    x = [0] * 4
    y = [0] * 4
    
    print("** Bezier Curve for 4 control points **")
    print("Please enter x and y coordinates ")

    # Input the coordinates of the control points
    for i in range(4):
        x[i], y[i] = map(int, input("(x{}, y{}): ".format(i, i)).split())
        plt.scatter(x[i], y[i], color='red')  # Mark the control points on the graph
        plt.text(x[i] - 20, y[i] - 20, f"(x{i}, y{i})", color='red')

    # Calculate and draw the bezier curve
    num_points = 1000
    for i in range(num_points + 1):
        t = i / num_points
        put_x, put_y = bezier_curve(x, y, t)
        plt.scatter(put_x, put_y, color='green')  # Plot the points on the graph

    plt.show()

if __name__ == "__main__":
    main()





# Sample input:
# 100 100
# 200 400
# 300 100
# 400 400
