
class race():
    def __init__(self):
        self.margin_of_error = []
    
    def boat_vel(self, timeHeld: int, timeLeft: int) -> int:
        velPerSec = 1
        boat_velocity = timeHeld * velPerSec
        return boat_velocity * timeLeft

    def determine_wins(self, time: int, dist_to_beat: int) -> int:
        possible_wins = 0
        for i in range(1, time):
            distance = self.boat_vel(i, time-i)
            if distance > dist_to_beat:
                possible_wins += 1
        if possible_wins > 0:
            self.margin_of_error.append(possible_wins)
        return possible_wins

    def read_test_input(self, file_path: str) -> [(int, int)]:
        lines: [str]
        with open(file_path) as f:
            times = list(filter(None, f.readline().replace('Time: ','').split(" ")))
            times = [int(time) for time in times]
            distances = list(filter(None, f.readline().replace('Distance: ','').split(" ")))
            distances = [int(dist) for dist in distances]
        return list(zip(times, distances))

    def get_margin_of_error(self):
        margin = 1
        for item in self.margin_of_error:
            margin *= item
        return margin
