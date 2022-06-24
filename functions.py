import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def plotting_ACC(labels, sensor):
    acceleration_time = list(labels["#->Timestamp"].values)
    matplotlib.rcParams['figure.figsize'] = [70, 10]
    ACC_X = list(labels[sensor+"-X"].values)
    ACC_Y = list(labels[sensor+"-Y"].values)
    ACC_Z = list(labels[sensor+"-Z"].values)
    plt.plot(acceleration_time, ACC_X, 'r', label="X-axis")
    plt.plot(acceleration_time, ACC_Y, 'b', label="Y-axis")
    plt.plot(acceleration_time, ACC_Z, 'g', label="Z-axis")
    plt.legend(loc="upper right")
    plt.xlabel("Time")
    plt.ylabel(sensor)
    plt.show()

def plotting_GYRO(labels, sensor):
    acceleration_time = list(labels["#->Timestamp"].values)
    matplotlib.rcParams['figure.figsize'] = [70, 10]
    GYRO_X = list(labels[sensor+"-X"].values)
    GYRO_Y = list(labels[sensor+"-Y"].values)
    GYRO_Z = list(labels[sensor+"-Z"].values)
    plt.plot(acceleration_time, GYRO_X, 'r', label="X-axis")
    plt.plot(acceleration_time, GYRO_Y, 'b', label="Y-axis")
    plt.plot(acceleration_time, GYRO_Z, 'g', label="Z-axis")
    plt.legend(loc="upper right")
    plt.xlabel("Time")
    plt.ylabel(sensor)
    plt.show()

