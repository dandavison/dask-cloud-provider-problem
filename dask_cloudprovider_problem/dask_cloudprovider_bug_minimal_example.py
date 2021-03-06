import dask.bag


def task(i):
    return i + 1


def run_tasks():
    print(dask.bag.from_sequence(range(10)).map(task).compute())


if __name__ == "__main__":
    from dask_cloudprovider import FargateCluster
    from dask.distributed import Client

    Client(FargateCluster(n_workers=1))
    run_tasks()  # WORKS
