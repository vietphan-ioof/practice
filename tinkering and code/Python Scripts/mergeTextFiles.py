import glob


readFiles = glob.glob("*.txt")

with open("results.txt", "wb") as outfile:
    for f in readFiles:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
C:\Users\madhu\OneDrive\Desktop\SciFILSTMFiles\Sci-FILSTMTrainingBooks
