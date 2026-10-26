from google.adk.agents import LlmAgent

finance_agent = LlmAgent(
    name="FinanceAgent",
    model="gemini-3.5-flash-lite",
    description= "A simple finance agent that helps users with financial goals.",
    instruction= """ You are a helpful finance agent. You can provide advice on budgeting
    saving, investing, and other financial topics. 
    Please answer questions clearly and concisely.
    """,
)

root_agent = finance_agent