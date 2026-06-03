import time

# DECORATOR: Execution timer for Ingestion Audits

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[AUDIT] '{func.__name__}' execution took {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

