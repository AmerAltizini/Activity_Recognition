import matplotlib
import matplotlib.pyplot as plt
import numpy as np
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


## Define function
def fit_n_pred(clf_, X_tr, X_te, y_tr):
    """Takes in Classifier, training data (X,y), and test data(X). Will output
    predictions based upon both the training and test data using the sklearn
    .predict method. MUST unpack into two variables (train, test)."""

    ## Fitting classifier to training data
    clf_.fit(X_tr, y_tr)

    ## Generate predictions for training + test data
    y_hat_trn = clf_.predict(X_tr)
    y_hat_tes = clf_.predict(X_te)

    ## Optional display check
    display(clf_)

    return y_hat_trn, y_hat_tes



def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center")
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

def evaluate(window_size, overlap, sampling_rate, feature_set, training_participants, testing_participants):
    segments = withoutLabelDF.rolling(window=window_size, center=True, min_periods=window_size).agg(
        ['min', 'max', 'sum', 'mean', 'std'])
    segments.columns = ['-'.join(tup).rstrip('-') for tup in segments.columns.values]
    segments = pd.concat([withoutTS.iloc[:, -1], segments], axis=1)
    segments = segments.dropna()
    segments = segments[::(int)(window_size * overlap)]
    return segments
    # do preprocessing, segmentation, classification for this configuration
    print("classification accuracy = x %")
    # for each activity print recall, precision, Fl Score
    # ideally, store all the information for this configuration to a csv file
    # which is better for a Later evaluation


def evaluate(window, overlap, sampling_rate, feature_set, training_participants, testing_participants):
    # do preprocessing, segmentation, classification for this configuration
    print("classification accuracy = x %")
    # for each activity print recall, precision, Fl Score
    # ideally, store all the information for this configuration to a csv file
    # which is better for a Later evaluation
window_sizes = [0.2, 0.4, 0.5, 0.7, 0.9, 1.0]
overlaps = [0, 0.25, 0.5, 0.75, 0.9, 'max']
sampling_rates = [5, 10, 25, 35]
feature_sets = [["mean", "std"], ["mean", "std", "slope", "energy"]]
training_participants = ["p_1", "p_2"]
testing_participants = ["p_3", "p_4"]

for window in window_sizes:
    for overlap in overlaps:
        for sampling_rate in sampling_rates:
            for feature_set in feature_sets:
                evaluate(window, overlap, sampling_rate, feature_set, training_participants, testing_participants)