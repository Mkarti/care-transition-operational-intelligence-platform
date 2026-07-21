from pipeline import build_pipeline
from analytics import run_insights


FILE_PATH = "data/raw/HHS_Unaccompanied_Alien_Children_Program.csv"


def main():

    df = build_pipeline(FILE_PATH)

    insights = run_insights(df)

    print(insights["risk_level"])
    print(insights["summary"])
    print(insights["anomalies"]["cbp_backlog"].head())


if __name__ == "__main__":
    main()