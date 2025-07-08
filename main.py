from flytekit import task, workflow
import random

@task
def greet(name: str) -> str:
    return f"Hello {name}, the Cunt!"

@task
def lucky_number(lower: int, upper: int) -> int:
    return random.randint(lower, upper)

@task
def combine(greeting: str, number: int) -> str:
    return f"{greeting}. Your lucky number is {number}"

@workflow
def workflow_tefa(name: str) -> str:
    greeting = greet(name)
    number = lucky_number(1, 100)
    return combine(greeting, number)

if __name__ == "__main__":
    print(workflow_tefa("Moustafa"))