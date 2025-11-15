import pandas as pd
from collections import Counter
from itertools import pairwise


# ---------------------------------------
# BASIC METRICS
# ---------------------------------------

def most_frequent_pages(df: pd.DataFrame, top_n: int = 10):
    """Return the most common pages across all journeys."""
    all_pages = [page for journey in df['journey_list'] for page in journey]
    return Counter(all_pages).most_common(top_n)


def most_common_entry_page(df: pd.DataFrame):
    """Return the most frequent entry page."""
    return df['entry_page'].value_counts().idxmax()


def most_common_exit_page(df: pd.DataFrame):
    """Return the most frequent exit page."""
    return df['exit_page'].value_counts().idxmax()


def average_journey_length(df: pd.DataFrame):
    """Return the mean journey length."""
    return df['journey_length'].mean()


# ---------------------------------------
# JOURNEY SEQUENCE METRICS
# ---------------------------------------

def most_frequent_journeys(df: pd.DataFrame, top_n: int = 10):
    """
    Return most common full journeys as strings.
    Uses journey_list to ensure clean and consistent formatting.
    """
    journey_strings = df["journey_list"].apply(lambda x: " → ".join(x))
    return journey_strings.value_counts().head(top_n)


# ---------------------------------------
# OPTIONAL ADVANCED METRIC (transition matrix)
# ---------------------------------------

def most_common_transitions(df: pd.DataFrame, top_n: int = 10):
    """
    Count how often users move from one page to another.
    Example: Homepage → Log in
    """
    transitions = []

    for journey in df["journey_list"]:
        for (a, b) in pairwise(journey):  # pairwise = (p1,p2), (p2,p3), ...
            transitions.append((a, b))

    return Counter(transitions).most_common(top_n)
