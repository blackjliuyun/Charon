import difflib
import requests
import random
from urllib.parse import urlparse


def is_similar_by_degree_of_similarity(standard_text, text):
    degree_of_similarity = difflib.SequenceMatcher(None, standard_text, text).quick_ratio()
    if degree_of_similarity < 0.85:
        return True
    return False


def check_200_or_404(url):
    # 200 -> True    404 -> False
    parse_result = urlparse(url)
    random_num = ''.join(str(i) for i in random.sample(range(0, 9), 5))
    url_404 = "%s://%s/this_is_404_page_%s" % (parse_result.scheme, parse_result.netloc, random_num)
    try:
        standard_text = requests.get(url_404).text
    except:
        pass
    try:
        text = requests.get(url).text
    except:
        pass
    return is_similar_by_degree_of_similarity(standard_text, text)
