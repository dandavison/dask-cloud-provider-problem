from pathlib import Path

from dask_cloudprovider_problem import dask_cloudprovider_bug_minimal_example

if __name__ == "__main__":
    from dask_cloudprovider import FargateCluster
    from dask.distributed import Client

    egg_file = Path("__file__").parent / "dist" / "dask_cloudprovider_problem-0.0.0-py3.7.egg"
    assert egg_file.exists()
    client = Client(FargateCluster(n_workers=1))
    client.upload_file(egg_file)
    dask_cloudprovider_bug_minimal_example.run_tasks()
