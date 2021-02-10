
class Gaussian():

    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev
        self.data = []

    def calculate_mean(self):
        pass

    def calculate_stdev(self):
        pass

    def read_data_file(self, file_name, sample = True):
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

    def plot_histogram(self):
        pass

    def pdf(self, x):
        pass

    def plot_histogram_pdf(self, n_spaces = 50):
        pass
