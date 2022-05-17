

class Reward:
    def init(self):
        self.fastest_lap = 900

    def reward_function(self, params):
        if params.progress == 100:
            if self.params['steps'] <= self.fastest_lap:
                return float((self.fastest_lap - self.params['steps'])**2)
                self.fastest_lap = self.params['steps']
            else:
                return float(0.5)
reward_object = Reward()

def reward_function(params):
    return reward_object.reward_function(params)