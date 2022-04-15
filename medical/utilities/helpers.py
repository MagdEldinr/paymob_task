from .csv_handler import load_column_from_dataset

def get_key_values_similarity(key):
    similar_values = []
    for value in load_column_from_dataset('Values'):
        similarity_ratio = get_similarity_algorithm(key.split(), value.split())
        if similarity_ratio > 5:
            similar_values.append(
                {
                    "value": value,
                    "ratio": similarity_ratio
                }
            )
    return similar_values

def get_similarity_algorithm(first_text, second_text):
    intersection_score = len(set.intersection(*[set(first_text), set(second_text)]))
    union_score = len(set.union(*[set(first_text), set(second_text)]))
    return intersection_score/float(union_score) * 100

