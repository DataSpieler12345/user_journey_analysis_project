import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """Load raw user journey CSV."""
    return pd.read_csv(path)


def clean_user_journey_column(df: pd.DataFrame,
                              col_name: str = "user_journey",
                              sep: str = "-") -> pd.DataFrame:
    """
    Cleans and processes the user_journey column.

    Steps:
    - Drops rows where user_journey is missing
    - Converts strings and splits journey by separator
    - Removes whitespace
    - Removes empty items
    - Creates helper columns:
        journey_list, journey_length, entry_page, exit_page
    """

    df = df.copy()

    # Drop missing journeys
    df = df.dropna(subset=[col_name])

    # Ensure string type
    df[col_name] = df[col_name].astype(str)

    # Split and strip pages
    df["journey_list"] = (
        df[col_name]
        .str.split(sep)
        .apply(lambda pages: [p.strip() for p in pages if p.strip()])
    )

    # Remove rows with empty lists
    df = df[df["journey_list"].str.len() > 0]

    # Helper columns
    df["journey_length"] = df["journey_list"].str.len()
    df["entry_page"] = df["journey_list"].str[0]
    df["exit_page"] = df["journey_list"].str[-1]

    return df


def save_preprocessed_data(df: pd.DataFrame, path: str) -> None:
    """Save cleaned dataframe to CSV."""
    df.to_csv(path, index=False)


def preprocess_user_journeys(
    raw_path: str,
    output_path: str,
    col_name: str = "user_journey",
    sep: str = "-"
) -> pd.DataFrame:

    # 1. Load RAW
    df_raw = load_raw_data(raw_path)
    initial_rows = len(df_raw)

    # 2. Remove rows with NULL journeys
    df_no_null = df_raw.dropna(subset=[col_name])
    after_null_rows = len(df_no_null)

    # 3. Clean and parse journey column
    df_clean = clean_user_journey_column(df_no_null, col_name=col_name, sep=sep)
    after_clean_rows = len(df_clean)

    # 4. Save
    save_preprocessed_data(df_clean, output_path)

    # 5. Report
    print("\n===== PREPROCESSING REPORT =====")
    print(f"Initial rows:                      {initial_rows}")
    print(f"Rows after removing NULLs:         {after_null_rows}")
    print(f"Rows after cleaning journeys:      {after_clean_rows}")
    print(f"Total rows removed:                {initial_rows - after_clean_rows}")
    print("=================================\n")

    return df_clean
