from main_agent import RAGLLMAgent

agent = RAGLLMAgent()

result = agent.run(
    symptoms=["fever", "fatigue", "rash"],
    history="25-year-old male recently returned from tropical travel."
)

print(result)
