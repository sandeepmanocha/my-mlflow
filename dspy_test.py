import dspy
import mlflow
# Configure DSPy to use Ollama
# lm = dspy.LM(
#     model="ollama/llama3.1:8b",
#     api_base="http://localhost:11434",
#     max_tokens=500,
#     temperature=0.7
# )

lm = dspy.LM(
    model='openai/Qwen/Qwen3-0.6B',
    api_base='http://localhost/v1',  # Through NGINX
    api_key='EMPTY',  # vLLM doesn't require API key
    max_tokens=200
)

dspy.settings.configure(lm=lm)

# mlflow.set_tracking_uri("http://localhost:5000")
# mlflow.set_experiment("my-dspy-experiment")
# mlflow.autolog()


# Define a simple signature
class BasicQA(dspy.Signature):
    """Answer questions with short factual answers."""
    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")

# Create a predictor
generate_answer = dspy.Predict(BasicQA)

# Use it
pred = generate_answer(question="Who developed LLM models for the first time?")
print(pred.answer)
