import pandas as pd

def get_cost_recommendations(cost_df: pd.DataFrame, min_ctr: float = 0.05):
    df = cost_df.copy()
    df['recommendation'] = df.apply(
        lambda row: 'show' if row['unit_cost'] <= 0.5 and row['ctr'] >= min_ctr else 'pause', axis=1
    )
    return df[['user_id', 'ad_id', 'total_views', 'unit_cost', 'ctr', 'recommendation']]
