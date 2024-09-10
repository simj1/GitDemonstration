from analysis_functions.import_data import import_data

DATA_FILEPATH = "./data/titanic.csv"

def main():
    print("This is a demonstration of git")
    df = import_data(DATA_FILEPATH)
    

if __name__ == "__main__":
    main()