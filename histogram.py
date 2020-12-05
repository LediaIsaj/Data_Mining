from random import randint
import matplotlib.pyplot as plt

def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    names = []
    for i in range(len(bins)):
        if i < len(bins) - 1:
            names.append(str(bins[i]) + '-' + str(bins[i+1]))
        else:
            names.append(str(bins[i]) + '+')
    dict = {k: 0 for k in names}

    for d in data:
        for i in range(len(names)):
            if i < len(bins)-1:
                if bins[i] <= d < bins[i + 1]:
                    dict[names[i]]=dict[names[i]]+1
                    break
            else:
                dict[names[i]] = dict[names[i]] + 1



    return dict


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """

    plt.bar(bins_count.keys(), bins_count.values(), color='b')
    plt.xlabel('Bins')
    plt.ylabel('Count')
    plt.title('Distribution of data')
    plt.show()



if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
