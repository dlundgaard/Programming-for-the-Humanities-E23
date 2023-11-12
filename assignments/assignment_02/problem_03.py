import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker
from utils import *

def generate_similarity_matrix(sample_size = 20):
    dataset = pd.read_csv("horoscopes.csv").sample(n = sample_size, random_state=1)["horoscope-clean"]

    doc_term_matrix, lexicon = list_to_dtm(dataset, stopword=False)

    similarity_matrix = np.empty((len(doc_term_matrix), len(doc_term_matrix)))
    similarity_matrix[:] = np.nan
    for i, a in enumerate(doc_term_matrix):
        for j, b in enumerate(doc_term_matrix):
            if i > j:
                similarity_matrix[i, j] = cosine_similarity(a, b)

    plt.imshow(similarity_matrix, interpolation="nearest", cmap = "viridis", vmin = np.nanmin(similarity_matrix), vmax = np.nanmax(similarity_matrix))
    plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(1))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(5))
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(5))
    
    plt.xlabel("\nDocument #")
    plt.ylabel("Document #\n")
    cbar = plt.colorbar()
    cbar.ax.set_title("Cosine similarity")
    plt.tight_layout()
    plt.savefig("cosine_similarities", dpi = 100)

    print()

    min_A, min_B = np.unravel_index(np.nanargmin(similarity_matrix), similarity_matrix.shape)
    print(f"Minimum cosine similarity: {np.nanmin(similarity_matrix).round(3)} (documents {min_B}, {min_A})")
    print(f"\n\tDocument {min_B}:\n{dataset.iloc[min_B]}")
    print(f"\n\tDocument {min_A}:\n{dataset.iloc[min_A]}")

    print()

    max_A, max_B = np.unravel_index(np.nanargmax(similarity_matrix), similarity_matrix.shape)
    print(f"Maximum cosine similarity: {np.nanmax(similarity_matrix).round(3)} (documents {max_B}, {max_A})")
    print(f"\n\tDocument {max_B}:\n{dataset.iloc[max_B]}")
    print(f"\n\tDocument {max_A}:\n{dataset.iloc[max_A]}")

# def per_sign_similarity_matrix():
#     dataset = pd.read_csv("horoscopes.csv").groupby("sign")["horoscope-clean"].apply(lambda horoscope: " ".join(horoscope)).reset_index()

#     doc_term_matrix,  lexicon = list_to_dtm(dataset["horoscope-clean"], stopword=True)

#     similarity_matrix = np.empty((len(doc_term_matrix), len(doc_term_matrix)))
#     similarity_matrix[:] = np.nan
#     for i, a in enumerate(doc_term_matrix):
#         for j, b in enumerate(doc_term_matrix):
#             if i > j:
#                 similarity_matrix[i, j] = cosine_similarity(a, b)

#     plt.imshow(similarity_matrix, interpolation="nearest", cmap = "viridis", vmin = np.nanmin(similarity_matrix), vmax = np.nanmax(similarity_matrix))

#     plt.xlabel("\nDocument #")
#     plt.ylabel("Document #\n")
#     plt.xticks(dataset.index, dataset["sign"], rotation = 90)
#     plt.yticks(dataset.index, dataset["sign"])

#     cbar = plt.colorbar()
#     cbar.ax.set_title("Cosine similarity")
#     plt.tight_layout()
#     plt.savefig("cosine_similarities_per_sign", dpi = 100)

#     print("min:", np.nanmin(similarity_matrix).round(3), "max:", np.nanmax(similarity_matrix).round(3))

if __name__ == "__main__":
    generate_similarity_matrix()
    # per_sign_similarity_matrix()