import World
import threading
import time


def run():
    World.render_cell_value()
    H = 10
    gamma = 0.9
    noise = 0.2
    for _ in range(H):
        time.sleep(.1)

        V = {}
        for state in list(World.neighbour_states.keys()):
            V[state] = World.R[state]

            # find all possible neighbour of this state
            neighbours = World.neighbour_states[state]

            # calculate value making each of them most probable action each time
            for neighbour in neighbours:
                state_val = 0
                high_prob = (1 - noise)
                low_prob = noise / (len(neighbours) - 1)

                state_val += high_prob * (World.R[state] + gamma * World.V[neighbour])

                # iterate stochastic probable state
                for other in neighbours:
                    if other != neighbour:
                        state_val += low_prob * (World.R[state] + gamma * World.V[other])

                V[state] = max(V[state], state_val)

        World.V = V
        World.render_cell_value()


if __name__ == '__main__':
    policy = {
        (0, 0): 'r',
        (0, 1): 'u',
        (0, 2): 'u',
        (1, 0): 'r',
        (1, 2): 'r',
        (2, 0): 'u',
        (2, 1): 'u',
        (2, 2): 'u',
        (3, 2): 'l',
    }

    # Enabling specific grid
    World.grid_value_mode()

    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    World.start_game()
