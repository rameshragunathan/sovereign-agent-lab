"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Albanach"
QUERY_1_VENUE_ADDRESS = "F2 Hunter Square, Edinburgh"
QUERY_2_FINAL_ANSWER  = "No venues in the known list can accommodate 300 people with vegan options. The largest available vegan-friendly venue is The Albanach with capacity 180."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
i modified the albanach's status to full in the mcp_veneu_server file and reran the exercise. This meant the output from search_venue, no longer listed the albanach as an option. haymarket vault was the only viable option for the query.
MCP centralises the data so that all agenst can access updated information.  
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 20   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 33   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP allows you to consilidate the data and logic allowing all agents to acces this, if this was not the case, we would need to update the tools in each agent. MCP similifies the process and reduces the riskj of inconsitent data.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- Ability to search the web for updated information on venues. Langgraph for this.
- Voice capability to interact with users, be able to pivot when the question is outside of the scope and provide a human-like response. WHiper and TTS
- Using MCP to centralise logic and business rules, so that all agents follow the same guard rails.
- Ability to escalate to human or potentially another agent with more specialised knowledge.
- Using advanced CALM flows for critical data gathering and pivoting.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph is agent for research, as it has the ability to search the web site with enough capability to finding relevant and related information without prompting.This was clearly shown when Bow bar was full and it found an alternative. When gathering data from human, we need something that follows a stricter set of rules
for thise Rasa agent is more suitable and is able to escalate when the limit for deposit exceed the £300 limit. Swapping these would create a non human like experience and requiring more code on the Rasa side to be able to present all the options.
"""
