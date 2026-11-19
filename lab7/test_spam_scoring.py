from hypothesis import given, settings, strategies as st

from spam_scoring import first_link, sender_domain, shout_ratio


FUZZ_INPUTS = st.one_of(st.text(), st.none())


@settings(max_examples=200, deadline=None)
@given(value=FUZZ_INPUTS)
def test_sender_domain_handles_arbitrary_input(value):
    result = sender_domain(value)
    assert isinstance(result, str)


@settings(max_examples=200, deadline=None)
@given(value=FUZZ_INPUTS)
def test_first_link_handles_arbitrary_input(value):
    result = first_link(value)
    assert isinstance(result, str)


@settings(max_examples=200, deadline=None)
@given(value=FUZZ_INPUTS)
def test_shout_ratio_handles_arbitrary_input(value):
    result = shout_ratio(value)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


def test_sender_domain_normalizes_valid_address():
    assert sender_domain("offers@Deals.com") == "deals.com"


def test_sender_domain_rejects_malformed_address():
    for value in (None, "", "offers", "@example.com", "offers@", "a@@b"):
        assert sender_domain(value) == ""


def test_first_link_returns_first_http_url():
    assert first_link("See https://example.com/a and http://example.org") == "https://example.com/a"


def test_first_link_returns_empty_when_absent():
    assert first_link("no link here") == ""
    assert first_link(None) == ""


def test_shout_ratio_counts_only_letters():
    assert shout_ratio("FREE prize NOW!") == 7 / 12


def test_shout_ratio_is_zero_without_letters():
    assert shout_ratio("") == 0.0
    assert shout_ratio("123 !?") == 0.0
    assert shout_ratio(None) == 0.0
