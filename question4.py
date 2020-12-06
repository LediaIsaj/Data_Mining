"""
    addition
"""
import random

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        return compute_histogram_bins(self.peer_pool.values(),BINS)
       

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        dict = self.backend_database[0]
        for hist in range(1, len(self.backend_database)):
            for key in self.backend_database[hist].keys():
                if key in dict:
                    dict[key] += self.backend_database[hist][key]
                else:
                    dict[key] = self.backend_database[hist][key]

        return dict
if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
