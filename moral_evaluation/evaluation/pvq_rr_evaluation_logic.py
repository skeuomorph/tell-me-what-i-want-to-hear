import pandas as pd

def main():
    values = ["selfdirection_thought",
"selfdirection_action",
"stimulation",
"hedonism",
"achievement",
"power_dominance",
"power_resources",
"face",
"security_personal",
"security_societal",
"tradition",
"conformity_rules",
"conformity_interpersonal",
"humility",
"universalism_nature",
"universalism_concern",
"universalism_tolerance",
"benevolence_care",
"benevolence_dependability"]
    df = pd.read_csv("pvq.csv", header=0)
    results = code_pvq(df)
    print(results[values])

def code_pvq(data):
    #values dictionary indicates which questions correspond to the moral value
    values = {"selfdirection_thought":[1, 23, 39],
                   "selfdirection_action":[16, 30, 56],
                   "stimulation":[10, 28, 43],
                   "hedonism":[3, 36, 46],
                   "achievement":[17, 32, 48],
                   "power_dominance":[6, 29, 41],
                   "power_resources":[12, 20, 44],
                   "face":[9, 24, 49],
                   "security_personal":[13, 26, 53],
                   "security_societal":[2, 35, 50],
                   "tradition":[18, 33, 40],
                   "conformity_rules":[15, 31, 42],
                   "conformity_interpersonal":[4, 22, 51],
                   "humility":[7, 38, 54],
                   "universalism_nature":[8, 21, 45],
                   "universalism_concern":[5, 37, 52],
                   "universalism_tolerance":[14, 34, 57],
                   "benevolence_care":[11, 25, 47],
                   "benevolence_dependability":[19, 27, 55]}
    for x in values:
        data[x]=data[values[x]].mean(axis=1)
    return data

if __name__ == "__main__":
    main()
