class Gaussian():

    def __init__(self, mean, stdev):
        self.mean = mean
        self.stdev = stdev
        self.data = []

    def calculate_mean(self):
        self.data
        self.mean = float(sum(self.data)/len(self.data))
        return self.mean


    def calculate_stdev(self):
        j = 0
        for i in range(len(self.data)):
            result = self.mean - self.data[i]
            squared = result*result
            j = j + squared
            print(result)
            print(squared)
        print('--Total---')
        print(j)
            value =  sum(squared)/len(squared)

            self.stdev = (self.mean)*(1-)
#        return self.stdev


    def read_data_file(self, file_name, sample = True):
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list
        self.mean = calculate_mean()
        self.stdev = self.calculate_stdev(sample)

    def plot_histogram(self):
        pass

    def pdf(self, x):
        pass

    def plot_histogram_pdf(self, n_spaces = 50):
        pass

#magic methods
    def __add__(self, other):
        pass

#magic methods
    def __repr__(self):
        pass


    def main():
        pass


    if __name__ == '__main__':
        main()
