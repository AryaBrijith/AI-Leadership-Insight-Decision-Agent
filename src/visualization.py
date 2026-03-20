import matplotlib.pyplot as plt
import os

def plot_revenue():
    revenue = [10, 12, 15]

    os.makedirs("outputs", exist_ok=True)

    plt.figure()
    plt.plot(revenue)
    plt.title("Revenue Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Revenue ($M)")

    plt.savefig("outputs/revenue_plot.png")
    plt.show()
    plt.close()