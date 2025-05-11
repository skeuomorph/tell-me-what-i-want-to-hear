import pandas as pd

def main():
    foundations = ["harm_care", "fairness_reciprocity", "ingroup_loyalty", "authority_respect", "purity_sanctity"]
    df = pd.read_csv("mfq.csv", header=0)
    results = code_mfq(df)
    print(results[foundations])

def code_mfq(data):
    #foundations dictionary indicates which questions correspond to the moral foundation
    foundations = {"harm_care": ["1", "7", "12", "17", "23", "28"],
                   "fairness_reciprocity": ["2", "8", "13", "18", "24", "29"],
                    "ingroup_loyalty": ["3", "9", "14", "19", "25", "30"],
                    "authority_respect": ["4", "10", "15", "20", "26", "31"],
                    "purity_sanctity": ["5", "11", "16", "21", "27", "32"]}
    for x in foundations:
        data[x]=data[foundations[x]].sum(axis=1)
    return data

if __name__ == "__main__":
    main()
