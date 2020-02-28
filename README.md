A demonstration of a dask problem described in https://github.com/dask/dask-cloudprovider/issues/68.

The problem is fixed by [4d43d46023df22865a912b6225dc2ee517a49797](https://github.com/dandavison/dask-cloud-provider-problem/commit/4d43d46023df22865a912b6225dc2ee517a49797).

```
pip install -r requirements.txt
python dask_cloudprovider_bug_minimal_example.py  # This will work
python dask_cloudprovider_bug_minimal_example_importer.py  # this will fail
```

The stack trace is

```
Traceback (most recent call last):
  File "dask_cloudprovider_bug_minimal_example_importer.py", line 8, in <module>
    dask_cloudprovider_bug_minimal_example.run_tasks()  # DNW!
  File "/Users/dan/src/dask_cloudprovider_bug/dask_cloudprovider_bug_minimal_example.py", line 9, in run_tasks
    print(dask.bag.from_sequence(range(10)).map(task).compute())
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/dask/base.py", line 166, in compute
    (result,) = compute(self, traverse=False, **kwargs)
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/dask/base.py", line 437, in compute
    results = schedule(dsk, keys, **kwargs)
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/client.py", line 2595, in get
    results = self.gather(packed, asynchronous=asynchronous, direct=direct)
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/client.py", line 1893, in gather
    asynchronous=asynchronous,
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/client.py", line 780, in sync
    self.loop, func, *args, callback_timeout=callback_timeout, **kwargs
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/utils.py", line 348, in sync
    raise exc.with_traceback(tb)
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/utils.py", line 332, in f
    result[0] = yield future
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/tornado/gen.py", line 735, in run
    value = future.result()
  File "/Users/dan/src/dask_cloudprovider_bug/.venv2/lib/python3.7/site-packages/distributed/client.py", line 1752, in _gather
    raise exception.with_traceback(traceback)
distributed.scheduler.KilledWorker: ("('task-94b724e41a5f306a008072467f552008', 8)", <Worker 'tcp://172.31.62.150:35627', name: 0, memory: 0, processing: 10>)
distributed.client - ERROR - Failed to reconnect to scheduler after 10.00 seconds, closing client
_GatheringFuture exception was never retrieved
future: <_GatheringFuture finished exception=CancelledError()>
concurrent.futures._base.CancelledError
```
