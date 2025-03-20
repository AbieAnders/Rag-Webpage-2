from duckduckgo_search import DDGS

def ddg_search(keyword_input: str):
    results = DDGS().news(keywords="infosys + india today", region="wt-wt", safesearch="off", timelimit="m", max_results=20)
    print(results)
    return results