from pe import ProcessingElement

class SystolicArraySimulator:
    """
    Coordinates a 3x3 matrix grid of Processing Elements and manages
    synchronized clock boundary propagation delays.
    """
    def __init__(self):
        self.grid = [[ProcessingElement() for _ in range(3)] for _ in range(3)]
        self.clock_cycles = 0

    def load_weights(self, matrix_b):
        """Maps whole weights into corresponding matrix cells."""
        for i in range(3):
            for j in range(3):
                self.grid[i][j].load_weight(matrix_b[i][j])

    def tick(self, left_inputs):
        """Simulates a single concurrent system clock pulse edge."""
        self.clock_cycles += 1

        # Phase 1: Force data streams specifically into entry gate Column 0
        for i in range(3):
            self.grid[i][0].input_x = left_inputs[i]

        # Phase 2: Execute MAC operations in parallel
        for i in range(3):
            for j in range(3):
                self.grid[i][j].compute()

        # Phase 3: Route horizontal signals to intermediate state tracking tables
        next_input_x = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if j + 1 < 3:
                    next_input_x[i][j+1] = self.grid[i][j].output_x

        # Phase 4: Advance the clock edge to transition state buffers into cells
        for i in range(3):
            for j in range(3):
                if j > 0:
                    self.grid[i][j].input_x = next_input_x[i][j]



