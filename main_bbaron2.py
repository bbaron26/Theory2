from ntm.runner_bbaron2 import run_simulation

if __name__ == "__main__":
    results = []

    # List of test cases
    test_cases = [
        ("aplus_bbaron2.csv", "abba"),
        ("abc_star_bbaron2.csv", "abcc"),
	("abc_star_DTM_bbaron2.csv", "abcc"),
        ("aplus_DTM_bbaron2.csv", "aaa"),
        ("aplus_bbaron2.csv", "aaa"),
	("aplus_DTM_bbaron2.csv", "a"),
        ("aplus_DTM_bbaron2.csv", "abc"),
	("equal_01s_bbaron2.csv", ""),
	("abc_star_bbaron2.csv", "cab"),
	("abc_star_DTM_bbaron2.csv", "ab"),
	("equal_01s_DTM_bbaron2.csv", "010")
    ]

    # Solve for each of the entered test cases
    for csv_file, input_string in test_cases:
        #print(f"Testing {csv_file} with input: {input_string}")
        kind, depth, total_configurations = run_simulation(csv_file, input_string, max_depth=50)
        avg_nondeterminism = total_configurations / depth if depth > 0 else 0
        results.append((csv_file, input_string, kind, depth, total_configurations, avg_nondeterminism))

    # Display results
    print("\nResults Summary:")
    print(f"{'Machine':<25} {'Input':<15} {'Result':<10} {'Depth':<10} {'# Configs':<15} {'Avg Non-Det':<15}")
    for row in results:
        print(f"{row[0]:<25} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<15} {row[5]:<15.2f}")


