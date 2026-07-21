import pandas as pd

ARQUIVO_CSV = "shopee.csv"


df = pd.read_csv(
    ARQUIVO_CSV,
    encoding="latin1",
    sep=",",
    engine="python",
    quotechar='"',
    quoting=3,
    on_bad_lines="skip"
)


df.columns = df.columns.str.strip()


print(df.columns.tolist())

print("\nTOTAL COLUNAS:")
print(len(df.columns))


print("\nPRIMEIRAS LINHAS:")
print(df.head(3).to_string())