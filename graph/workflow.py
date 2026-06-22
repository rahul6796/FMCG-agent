from langgraph.graph import StateGraph
from graph.state import NewsletterState
from agents.fetch_agent import fetch_news
from agents.clean_agent import clean_news
from agents.dedup_agent import deduplicate_news
from agents.relevance_agent import relevance_check
from agents.credibility_agent import  credibility_agent
from agents.newsletter_agent import generate_newsletter


builder = StateGraph(NewsletterState)

builder.add_node("fetch",fetch_news)
builder.add_node("clean",clean_news)
builder.add_node("dedup",deduplicate_news)
builder.add_node("relevance",relevance_check)
builder.add_node("credibility",credibility_agent)
builder.add_node("newsletter",generate_newsletter)

builder.set_entry_point("fetch")

builder.add_edge("fetch","clean")
builder.add_edge("clean","dedup")
builder.add_edge("dedup","relevance")

builder.add_edge("relevance","credibility")
builder.add_edge("credibility","newsletter")

graph = builder.compile()


