from constraint import *

problem = Problem()

villagers = {
    "hubert": {
        "neck": "purple scarf",
        "instrument": "panpipes",
        "age": "young",
        "race": "human",
        "gender": "male",
        "drink": "beer",
        "perform": "feats of strength"
    },
    "samson": {
        "head": "red hat",
        "age": "older",
        "race": "human",
        "gender": "male",
        "drink": "beer",
        "perform": "half-hearted dancer"
    },
    "daisy": {
        "neck": "white shawl",
        "instrument": "harp",
        "age": "young",
        "race": "halfling",
        "gender": "female",
        "drink": "beer",
        "perform": "acrobatic dancing"
    },
    "jocelin": {
        "head": "green bonnet",
        "instrument": "drum",
        "age": "older",
        "race": "human",
        "gender": "female",
        "drink": "wine",
        "perform": "graceful and talented dancer"
    }
}

# problem.addConstraint(lambda v, i: v != i, ["villager", "imposter"])

problem.addVariable("imposters", list(villagers.keys()))

print(problem.getSolutions())
