# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
#
# # Load API key from .env
# load_dotenv()
#
# # Create the LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     temperature=0.7
# )
#
# # Prompt template
# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         """You are an expert automotive engineer and car modification specialist.
#
#         Answer questions about:
#         - Engine tuning
#         - Turbochargers
#         - Superchargers
#         - Exhaust systems
#         - Suspension
#         - Wheels & Tires
#         - ECU tuning
#         - Car wrapping
#         - Performance upgrades
#         - Safety considerations
#         - Cost estimates
#
#         Explain everything in simple language suitable for beginners.
#         """
#     ),
#     ("human", "{question}")
# ])
#
# # Create chain
# chain = prompt | llm
#
# print("=" * 50)
# print("🚗 Car Modification AI Chatbot")
# print("Type 'exit' to quit.")
# print("=" * 50)
#
# while True:
#     question = input("\nAsk a question: ")
#
#     if question.lower() == "exit":
#         print("Goodbye!")
#         break
#
#     response = chain.invoke({"question": question})
#
#     print("\nAI:")
#     print(response.content)

from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("GOOGLE_API_KEY"))