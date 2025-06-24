import pandas as pd
import os
from ad_price_optimizer import config, metrics, model, visualization, data_generator


def ensure_directories():
    os.makedirs(config.INPUT_DATA_DIR, exist_ok=True)
    os.makedirs(config.OUTPUT_DATA_DIR, exist_ok=True)

def run():
    ensure_directories()
    input_path = os.path.join(config.INPUT_DATA_DIR, config.DEFAULT_INPUT_FILENAME)
    if not os.path.exists(input_path):
        print("Дані не знайдено. Генеруємо...")
        data_generator.generate_ad_data()

    df = pd.read_csv(input_path)
    cost_df = metrics.calculate_cost_metrics(df, base_cost=config.BASE_AD_COST, decay_rate=config.COST_DECAY_RATE)
    recs = model.get_cost_recommendations(cost_df)

    recs.to_csv(os.path.join(config.OUTPUT_DATA_DIR, config.RECOMMENDATIONS_CSV_FILENAME), index=False)

    visualization.plot_cost_vs_views(recs, os.path.join(config.OUTPUT_DATA_DIR, config.COST_VS_VIEWS_PLOT_FILENAME))
    visualization.plot_cost_distribution(recs, os.path.join(config.OUTPUT_DATA_DIR, config.COST_DISTRIBUTION_PLOT_FILENAME))

    print("Завершено аналіз кампанії")

if __name__ == '__main__':
    run()
