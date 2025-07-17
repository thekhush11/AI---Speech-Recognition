import wikipedia
import webbrowser

def get_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Here are some options: {e.options}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return str(e)

def search_web(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return "Searching the web for " + query

def handle_query(query):
    if "who is" in query.lower():
        person = query.lower().replace("who is", "").strip()
        return get_wikipedia_summary(person)
    elif "what is" in query.lower():
        topic = query.lower().replace("what is", "").strip()
        return get_wikipedia_summary(topic)
    else:
        return search_web(query)

def answer_query(command):
    try:
        result = wikipedia.summary(command, sentences=2)
        print(result)
        return result
    except Exception as e:
        print("Sorry, I couldn't find an answer.")
        return "Sorry, I couldn't find an answer."