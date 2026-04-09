"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  Hi, I'm calling from The Albanach to confirm the booking for tonight                                                                                                                                                                    
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                                                                                                                                                                                                              
And how many of those guests will need vegan meals?
Your input ->  20 guests will need vegan meals                                                                                                                                                                                                         
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  200                                                                                                                                                                                                                                     
Thank you — booking confirmed. 160 guests, 20 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking                                                                                                                                                                                                            
How many guests are you confirming for tonight's event?
Your input ->  160                                                                                                                                                                                                                                     
And how many of those guests will need vegan meals?
Your input ->  50                                                                                                                                                                                                                                      
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  500                                                                                                                                                                                                                                     
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160
And how many of those guests will need vegan meals?
Your input ->  can you arrange a cake
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, 
please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
It responded with a polite refusal, explaining that it is not trained to handle that request and redirecting to the event organiser. It then offered to continue with the booking confirmation.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Calm handles out of scope queries with the current approach by politely refusing and redirecting the user to the appropriate contact, whereas LangGraph might attempt to handle or improvise a response based on its broader context understanding. However the outcome is not
guranteed or consistent.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I changed the time code on that was blanked out to true, thus simulating a time after 16:45. I then ran the conversation and observed that it escalated with the correct reason.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
we replaced explict instructions for every possible dialogue with an LLM but kepth the business control in python to ensure the LLM has guardrails to work within. This allows us to use the LLM to handle
dialogue with the human, making the interaction more natural.


"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """

langGraog is simpler however harder to control, for business use cases auditable traces may be needed, specific inputs must be collect and stored to ensure compliance. Rasa Pro allows us to do this and still have the 
benefits of an LLM handling the dialogue, but it does require more setup and maintenance than a langGraph approach.
"""



