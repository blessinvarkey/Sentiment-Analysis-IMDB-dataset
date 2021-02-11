import math
# import matplotlib.pyplot as plt
#
# class Gaussian():
#
#     def __init__(self, mu=0, sigma=1):
#         self.mu=mu
#         self.sigma=sigma
#         self.data = []

def calculate_mean(data):
    mu = sum(data)/len(data)
#    print(mu)
    return mu
    #
def calculate_stdev(mu, data):
    counter =0
    for number in data:
        result = mu - data
        squared = result*result
        counter = counter + squared

    mu_squared = counter/len(data)
    stdev = math.sqrt(mu_squared)
    return stdev


    #
    # def read_data_file(self, filename, sample = True):
    #     with open(filename) as file:
    #         data_list = []
    #         line = file.readline()
    #         while line:
    #             data_list.append(int(line))
    #         file.close()
    #
    #         self.data = data_list
    #         self.mean = self.calculate_mean()
    #         self.sigma = self.calculate_stdev()
    #
    # def plot_histogram(self):
    #     plt.hist(self.data)
    #     plt.title('Histogram of data')
    #     plt.xlabel('data')
    #     plt.ylabel('count')

def main():
    data = [1,3,99,100,120,32,330,23,76,44,31]
    mu = calculate_mean(data)
    print(mu)
    calculate_stdev(mu, data)
    print(stdev)

if __name__ == '__main__':
    main()
