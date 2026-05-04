import pandas as pd

# Ler CSV
df = pd.read_csv("../data/raw/skins_data.csv")

# Converter data
df["collected_at"] = pd.to_datetime(df["collected_at"])

# Limite de 30 dias
limit = pd.Timestamp.now() - pd.Timedelta(days=30)

# Loop por skin
for skin, group in df.groupby("skin_name"):

    print(f"\nAnalyzing: {skin}")

    # Ordenar por data
    group = group.sort_values("collected_at")

    # Filtrar últimos 30 dias
    df_last_30_days = group[group["collected_at"] >= limit]

    if df_last_30_days.empty:
        print("Not enough data")
        continue

    # Média
    avg_lowest_price = df_last_30_days["lowest_price"].mean()

    # Preço mais recente
    recent_price = group["lowest_price"].iloc[-1]

    # Percentual
    percentage_diff = ((recent_price - avg_lowest_price) / avg_lowest_price) * 100

    # Score contínuo
    score = 50 - percentage_diff * 5
    score = max(0, min(100, score))

    # Threshold
    threshold = -5

    # Classificação
    if percentage_diff <= threshold:
        label = "Strong Buy"
    elif percentage_diff < 0:
        label = "Buy"
    else:
        label = "No Opportunity"

    # Output
    print(f"Average (30d): {avg_lowest_price:.2f}")
    print(f"Current price: {recent_price:.2f}")
    print(f"Percentage diff: {percentage_diff:.2f}%")
    print(f"Score: {score:.2f}")
    print(f"Signal: {label}")