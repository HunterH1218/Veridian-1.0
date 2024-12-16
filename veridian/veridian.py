import veridian
from veridian.search import *
from veridian.search import search_junction
from veridian.search import query_generator
from veridian.search import summerize_model
from veridian.search import google_search
from veridian.veridian_base_model import veridian_base


def main(query):
  search = search_junction.generate_response(query)
  if search == 'yes':
    search_query = query_generator.generate_response(query)
    search_result = google_search.main(search_query)
    summerized_result = summerize_model.generate_response(search_result)
    return summerized_result
  else:
    return veridian_base.generate_response(query)