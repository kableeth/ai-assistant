import os
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms  import OpenAI

load_dotenv()

os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.7)

tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
verbose=True)

agent.run('''You are my helpful AI Assistant that I send emails to and you decide what needs to be done next and makes that as easy as possible for me to complete. If, I need to write an email, draft the email. Here's the task: Figure out how to get a refund for this:      	
 
Tiller
 
 
 	
Receipt from Tiller
$79.00
Paid May 19, 2023
 
 
 
invoice illustration
Image Download invoice	 	Image Download receipt
 
Receipt number	 	2133-5478
 
Invoice number	 	8AEA6E82-0002
 
Payment method	 	Mastercard - 0611
 
 
 
 
 	Receipt #2133-5478
 
 	MAY 19, 2023 – MAY 19, 2024
 
 	
Tiller
 
Qty 1
 	
$79.00
 
 
 
 	 	 
 
 	
Total
 	
$79.00
 
 
 
 	 	 
 
 	
Amount paid $79.00.    Questions? Visit our support site at https://help.tillerhq.com, contact us at billing@tillerhq.com, or call us at +1 908-845-5371. Tiller contributes 0.5% of purchases to remove CO₂ from the atmosphere. Powered by stripe logo   |   Learn more about Stripe Billing
''')