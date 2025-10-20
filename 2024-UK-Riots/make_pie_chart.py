import polars as pl
import plotly.express as px


df = pl.read_csv("Patriotic_Alternative_Nodes.csv")
core_nodes = (
    df.filter(pl.col("Id").str.split("__").list.get(1).cast(int) < 1000000)
    .group_by("SNS")
    .len()
    .with_columns(SNS=pl.when(pl.col("len") < 10).then(pl.lit("Other")).otherwise(pl.col("SNS")))
    .group_by("SNS")
    .sum()
)

fig = px.pie(
    names=core_nodes["SNS"],
    values=core_nodes["len"],
    color=core_nodes["SNS"],
)
fig.update_traces(textinfo="none")
fig.write_image("core_into_pa.png")
