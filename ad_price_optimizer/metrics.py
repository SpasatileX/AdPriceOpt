import pandas as pd
import numpy as np

def calculate_cost_metrics(df: pd.DataFrame,
                           base_cost: float = 1.0,
                           decay_rate: float = 0.1) -> pd.DataFrame:
    agg_df = df.groupby(['user_id', 'ad_id']).agg(
        total_views=('view_count', 'max'),
        total_clicks=('clicked', 'sum'),
        avg_view_time=('view_time', 'mean')
    ).reset_index()

    agg_df['unit_cost'] = base_cost * np.exp(-decay_rate * agg_df['total_views'])
    agg_df['ctr'] = agg_df['total_clicks'] / agg_df['total_views']
    agg_df['unit_cost'] = agg_df['unit_cost'].round(4)
    return agg_df
