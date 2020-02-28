from dask_cloudprovider_bug_minimal_example import run_tasks

if __name__ == "__main__":
    from dask_cloudprovider import FargateCluster
    from dask.distributed import Client

    Client(FargateCluster(n_workers=1))
    run_tasks()
