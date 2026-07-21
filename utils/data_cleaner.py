import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Clean column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("*", "", regex=False)
    )

    # 2. Convert date
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce" 
    )

    df = df.dropna(subset=["date"])

    # 3. Convert numeric columns (remove commas)
    for col in df.columns:
        if col != 'date':
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "")
                .astype(float)
            )

    return df