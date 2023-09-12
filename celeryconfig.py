broker_url='redis://redis:6379/0'
result_backend='redis://redis:6379/1'

imports = ('tasks', )

worker_concurrency = 1
worker_pool = 'solo'