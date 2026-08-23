from simulator import SystolicArraySimulator

def test_hardware_block():
    print("--- STARTING HARDWARE DESIGN VERIFICATION TESTBENCH ---")
    sim = SystolicArraySimulator()

    # Declare Matrix B weights using basic list definitions to avoid syntax bugs
    row0 = list((1, 2, 3))
    row1 = list((4, 5, 6))
    row2 = list((7, 8, 9))
    matrix_b = list((row0, row1, row2))
    sim.load_weights(matrix_b)

    # Generate diagonal data-skewed streams for Matrix A
    stream0 = list((1, 2, 3, 0, 0, 0, 0))
    stream1 = list((0, 4, 5, 6, 0, 0, 0))
    stream2 = list((0, 0, 7, 8, 9, 0, 0))
    input_stream_matrix_a = list((stream0, stream1, stream2))

    total_cycles = 7
    print("[PROCESSING] Pumping data-skewed matrices through the 3x3 array...")
    
    for cycle in range(1, total_cycles + 1):
        left_inputs = [input_stream_matrix_a[i][cycle - 1] for i in range(3)]
        sim.tick(left_inputs)

    # Sample our internal target processing register 
    center_cell_result = sim.grid[1][1].accumulator
    expected_value = 75

    print(f"\nSimulation Complete over {sim.clock_cycles} Clock Cycles.")
    print(f"➔ Center Cell (1,1) Hardware Register Output: {center_cell_result}")
    print(f"➔ Expected Mathematical Baseline Value: {expected_value}")

    if center_cell_result == expected_value:
        print("\n[PASSED] Microarchitecture verification successful! Hardware outputs match.")
    else:
        print("\n[FAILED] Output mismatch detected.")

if __name__ == "__main__":
    test_hardware_block()
