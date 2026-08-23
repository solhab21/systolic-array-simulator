class ProcessingElement:
    """
    Models a single integrated circuit hardware cell containing an internal 
    weight register, a moving horizontal register, and a local accumulator.
    """
    def __init__(self):
        self.weight = 0              # Stationary data element
        self.input_x = 0             # Moving data element
        self.output_x = 0            # Latched output for neighbor routing
        self.accumulator = 0         # Local running mathematical total

    def load_weight(self, weight_value):
        """Loads static weights directly into the register."""
        self.weight = weight_value

    def compute(self):
        """Executes the core MAC hardware mathematical logic for the cycle."""
        self.output_x = self.input_x
        self.accumulator += self.input_x * self.weight

