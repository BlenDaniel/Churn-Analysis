# backend/utils/cache.py

from typing import Dict, Any
from functools import wraps
from datetime import datetime, timedelta
from backend.config.settings import settings
from backend.config.logging import logger

cache: Dict[str, Dict[str, Any]] = {}

def cache_response(ttl: int = settings.cache_ttl):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now()
            key = (func.__name__, args, tuple(kwargs.items()))

            if key in cache and now - cache[key]["timestamp"] < timedelta(seconds=ttl):
                logger.debug(f"Cache hit for key: {key}")
                return cache[key]["value"]
            else:
                logger.debug(f"Cache miss for key: {key}")
                result = func(*args, **kwargs)
                cache[key] = {"value": result, "timestamp": now}
                return result

        return wrapper

    return decorator
