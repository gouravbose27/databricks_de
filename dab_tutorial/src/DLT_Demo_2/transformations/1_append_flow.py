import dlt

dlt.create_streaming_table(
    name = "orders_src"
)

@dlt.append_flow(
    target = "orders_src"
)
def flow1():
    df = spark.readStream.format("cloudFiles") \
         .option("cloudFiles.format", "csv") \
         .load('/Volumes/databricksdemo/bronze/autovol/flow1/')
    return df


@dlt.append_flow(
    target = "orders_src"
)
def flow2():
    df = spark.readStream.format("cloudFiles") \
         .option("cloudFiles.format", "csv") \
         .load('/Volumes/databricksdemo/bronze/autovol/flow2/')
    return df