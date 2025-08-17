import multiprocessing
import os

# Настройка привязки к порту
bind = f"0.0.0.0:{os.getenv('PORT', '10000')}"

# Оптимизированное количество воркеров для Render
workers = 4
worker_class = 'sync'

# Таймауты
timeout = 120
graceful_timeout = 60
keepalive = 5

# Ограничения для стабильности
max_requests = 1000
max_requests_jitter = 50
worker_connections = 1000

# Логирование
accesslog = '-'
errorlog = '-'
loglevel = 'info'
access_log_format = '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Настройки для оптимизации производительности
worker_tmp_dir = '/dev/shm'
preload_app = True
forwarded_allow_ips = '*'
