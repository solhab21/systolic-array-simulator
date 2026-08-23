from simulator import SystolicArraySimulator

def main():
    print("--- STEP 1: INITIALIZING VIRTUAL INTEGRATED CHIP ---")
    sim = SystolicArraySimulator()

    # Define Matrix B weights
    matrix_b = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sim.load_weights(matrix_b)
    print("[SUCCESS] Matrix B stationary weights loaded into 3x3 register cells.\n")

    print("--- STEP 2: GENERATING DATA-SKEWING TIMING PIPELINE ---")
    # Matrix A inputs padded with zeros to stagger arrival times diagonally
    input_stream_matrix_a = [
        [1, 2, 3, 0, 0, 0, 0],  # Row 0
        [0, 4, 5, 6, 0, 0, 0],  # Row 1
        [0, 0, 7, 8, 9, 0, 0]   # Row 2
    ]
    print("[SUCCESS] Data-skewing input streams generated.\n")

    print("--- STEP 3: RUNNING SYSTEM CLOCK HEARTBEAT LOOP ---")
    total_cycles = 7
    
    for cycle in range(1, total_cycles + 1):
        left_inputs = [input_stream_matrix_a[i][cycle - 1] for i in range(3)]
        top_inputs = [0, 0, 0]

        # Fire the system clock pulse!
        sim.tick(left_inputs, top_inputs)

        # Track the center cell's calculations as data marches through
        center_cell_output = sim.grid[1][1].output_acc
        print(f"Clock Cycle {cycle:02d} ➔ Left Wall Inputs Fed: {left_inputs} | Center Cell OutputAcc = {center_cell_output}")

    print("\n[SUCCESS] Hardware simulation run complete!")

if __name__ == "__main__":
    main()
