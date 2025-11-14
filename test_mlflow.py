import mlflow

# Connect to remote MLflow server
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("my-first-experiment")

print(f"Tracking URI: {mlflow.get_tracking_uri()}")
print(f"Experiment ID: {mlflow.get_experiment_by_name('my-first-experiment').experiment_id}")

print("It Works!!")