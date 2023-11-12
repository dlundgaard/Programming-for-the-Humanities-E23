import pandas as pd
from utils import *

def get_most_frequent_words(data, n = 200):
    return data.str.split().explode().value_counts().index.values[:n]

def get_sign_idiosyncratic_word(dataset, signs, num_idiosyncratic = 10):
    idiosyncratic_for_sign = dict()
    for sign in signs: # loop over signs
        frequency_ranked_words_all_other_signs = get_most_frequent_words(
            dataset[dataset["sign"].isin(signs) & ~(dataset["sign"] == sign)]["horoscope-clean"]
        ) # getting the top-200 ranked words for all horoscopes in two of the three signs 
        frequency_ranked_words_sign = get_most_frequent_words(
            dataset[dataset["sign"] == sign]["horoscope-clean"] 
        ) # getting top-200 ranked words for currently active sign

        idiosyncratic = difference(
            frequency_ranked_words_sign, 
            frequency_ranked_words_all_other_signs
        )[:num_idiosyncratic] # find words which differ between currently surveyed sign and collective top-200 for the two other surveyed signs
        idiosyncratic_for_sign[sign] = idiosyncratic # store idiosyncratic words to compare
    
    df_compare = pd.DataFrame.from_records(idiosyncratic_for_sign).rename_axis("Rank", axis = "index")
    df_compare.index += 1
    return df_compare

if __name__ == "__main__":
    dataset = pd.read_csv("horoscopes.csv")

    sampled_signs = dataset.drop_duplicates("sign").sample(n = 3, random_state = 0)["sign"] # randomly sampling three signs from the 12 available (currently seeded for reproducibility)

    print(get_sign_idiosyncratic_word(dataset, sampled_signs).to_markdown())
