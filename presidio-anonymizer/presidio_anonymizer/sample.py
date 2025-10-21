from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def run_anonymizer(text: str, start: int, end: int, replacement: str = "BIP", engine: AnonymizerEngine | None = None):
    """
    Testable entry point: takes inputs as parameters and returns the anonymization result.
    """
    eng = engine or AnonymizerEngine()
    result = eng.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=int(start), end=int(end), score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": replacement})},
    )
    return result

def sample_run_anonymizer():
    """
    Backward-compatible wrapper if you still want interactive mode in the future.
    Not used in tests or the default __main__ path for this lab.
    """
    text = input("text: ")
    start = int(input("start: "))
    end = int(input("end: "))
    result = run_anonymizer(text, start, end)
    print(result)
    return result

if __name__ == "__main__":
    # For the lab requirement, run the example and print the result.
    out = run_anonymizer("My name is Bond.", 11, 15, "BIP")
    print(out)
