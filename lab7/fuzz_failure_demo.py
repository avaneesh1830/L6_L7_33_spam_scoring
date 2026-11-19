"""Run explicitly to reproduce the three crashes in the original code."""

from hypothesis import given, settings, strategies as st

from baseline_spam_scoring import first_link, sender_domain, shout_ratio


FUZZ_INPUTS = st.text()


@settings(max_examples=50, deadline=None)
@given(value=FUZZ_INPUTS)
def test_original_sender_domain_crashes_on_unexpected_input(value):
    sender_domain(value)


@settings(max_examples=50, deadline=None)
@given(value=FUZZ_INPUTS)
def test_original_first_link_crashes_when_link_is_missing(value):
    first_link(value)


@settings(max_examples=50, deadline=None)
@given(value=FUZZ_INPUTS)
def test_original_shout_ratio_crashes_without_letters(value):
    shout_ratio(value)
