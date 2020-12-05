from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """
        return list(self.peer_pool.values())

class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """
        print(BINS)
        
        names = []
        for i in range(len(BINS)):
            if i < len(BINS) - 1:
                names.append(str(BINS[i]) + '-' + str(BINS[i+1]))
            else:
                names.append(str(BINS[i]) + '+')
        dict = {k: 0 for k in names}

        for data in self.backend_database:
            for d in data:

                for i in range(len(names)):
                    if i < len(BINS)-1:
                        if BINS[i] <= d < BINS[i + 1]:
                            dict[names[i]]=dict[names[i]]+1
                            break
                    else:
                        dict[names[i]] = dict[names[i]] + 1

        return dict
        
if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()
    

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()


    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()

