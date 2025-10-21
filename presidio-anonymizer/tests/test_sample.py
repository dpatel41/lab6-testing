from presidio_anonymizer.sample import run_anonymizer

def test_sample_run_anonymizer():
    result = run_anonymizer("My name is Bond.", 11, 15, "BIP")

    # top-level text
    assert result.text == "My name is BIP."

    # items are OperatorResult objects
    assert isinstance(result.items, list)
    assert len(result.items) == 1

    item = result.items[0]
    assert item.start == 11
    assert item.end == 14          # "BIP" length is 3 → [11,14)
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
