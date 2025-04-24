def construct_ingest_query(self, static_path, columns):
    num_shards = self.num_shards
    target_partition_size = self.target_partition_size
    if self.target_partition_size == -1:
        if self.num_shards == -1:
            target_partition_size = DEFAULT_TARGET_PARTITION_SIZE
    else:
        num_shards = -1
    metric_names = [m['fieldName'] for m in self.metric_spec if m['type'] != 'count']
    dimensions = [c for c in columns if c not in metric_names and c != self.ts_dim]
    ingest_query_dict = {'type': 'index_hadoop', 'spec': {'dataSchema': {'metricsSpec': self.metric_spec, 'granularitySpec': {'queryGranularity': self.query_granularity, 'intervals': self.intervals, 'type': 'uniform', 'segmentGranularity': self.segment_granularity}, 'parser': {'type': 'string', 'parseSpec': {'columns': columns, 'dimensionsSpec': {'dimensionExclusions': [], 'dimensions': dimensions, 'spatialDimensions': []}, 'timestampSpec': {'column': self.ts_dim, 'format': 'auto'}, 'format': 'tsv'}}, 'dataSource': self.druid_datasource}, 'tuningConfig': {'type': 'hadoop', 'jobProperties': {'mapreduce.job.user.classpath.first': 'false', 'mapreduce.map.output.compress': 'false', 'mapreduce.output.fileoutputformat.compress': 'false'}, 'partitionsSpec': {'type': 'hashed', 'targetPartitionSize': target_partition_size, 'numShards': num_shards}}, 'ioConfig': {'inputSpec': {'paths': static_path, 'type': 'static'}, 'type': 'hadoop'}}}
    if self.job_properties:
        ingest_query_dict['spec']['tuningConfig']['jobProperties'].update(self.job_properties)
    if self.hadoop_dependency_coordinates:
        ingest_query_dict['hadoopDependencyCoordinates'] = self.hadoop_dependency_coordinates
    return ingest_query_dict