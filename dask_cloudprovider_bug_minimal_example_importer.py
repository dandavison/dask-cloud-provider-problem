import dask_cloudprovider_bug_minimal_example

if __name__ == "__main__":
    from dask_cloudprovider import FargateCluster
    from dask.distributed import Client

    Client(FargateCluster(n_workers=1))
    dask_cloudprovider_bug_minimal_example.run_tasks()  # ERROR!
    # distributed.scheduler.KilledWorker: ("('task-94b724e41a5f306a008072467f552008', 8)", <Worker 'tcp://172.31.62.150:35627', name: 0, memory: 0, processing: 10>)
