from .models import Medicine
from fuzzywuzzy import fuzz

def get_key_values_similarity(key):
    similar_values = []
    for medicine in Medicine.objects.all():
        similarity_ratio = fuzz.ratio(key,medicine.value)
        if similarity_ratio > 50:
            similar_values.append(
                {
                    "value": medicine.value,
                    "ratio": similarity_ratio
                }
            )
    return similar_values