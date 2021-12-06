from extract_data import extract_epicenter

filepath = "../data/utf-8/i1919.dat"
with open(filepath, "r") as f:
    for line in f:
        if not line.startswith("A"):
            continue

        try:
            epicenter = extract_epicenter(line)
        except Exception as e:
            print(line)
            raise e
        print(epicenter)
