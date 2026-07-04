import feedparser

RSS_SOURCES = {
    "nasa_artemis": "https://www.nasa.gov/missions/artemis/feed/",
    "nasa_technology": "https://www.nasa.gov/technology/feed/",
    "nasa_news": "https://www.nasa.gov/news-release/feed/",
    "twitter_engineering": "https://blog.twitter.com/engineering/en_us/blog.rss",
    "cloudflare_engineering": "https://blog.cloudflare.com/rss/w",
    "psychology": "http://feeds.feedburner.com/PsychologyBlog",
    "neuroscience_news": "http://neurosciencenews.com/feed/",
    "mit_news": "https://news.mit.edu/rss/research",
    "science_news": "https://www.sciencealert.com/rss"
}

get_rss = {
    "type": "function",
    "function": {
        "name": "get_rss",
        "description": (
            "Reads the latest articles from a trusted RSS source. "
            "Use this tool whenever the user asks for recent news or updates."
            "if the user request for any type of news you SHOULD use this."
            f"This are your resources: {list(RSS_SOURCES.keys())}"
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "source": {
                    "type": "string",
                    "enum": list(RSS_SOURCES.keys()),
                    "description": "Trusted RSS source to read."
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of articles to return.",
                    "default": 5
                }
            },
            "required": ["source"]
        }
    }
}

def execute(**kwargs):

    parameter = kwargs["source"]
    limit = kwargs.get("limit", 5)

    feed = feedparser.parse(parameter)

    return {
        "success": True,
        "content": feed.get(feed)
    }.__str__()

REGISTER = {
        "schema": get_rss,
        "handler": execute,
        "enabled": True,
        "version": "1.0v",
        "author": "Flowers"
    }