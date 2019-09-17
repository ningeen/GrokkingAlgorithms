def greedy_stations(states_needed, stations):
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states & states_needed
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        final_stations.add(best_station)
        states_needed -= states_covered
    return final_stations


states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = dict()
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = greedy_stations(states_needed, stations)

print(final_stations)
