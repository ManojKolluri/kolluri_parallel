import concurrent.futures
from typing import Callable, Iterable, Dict

def parallel_for(
    iterable: Iterable,
    iterable_function: Callable,
    max_workers: int = 3,
    executor: str = "thread"
) -> Dict:
    """
    Execute iterations in parallel.
    
    Args:
        iterable: Items to process (e.g., range(1, 6))
        iterable_function: Function to apply to each item. Must return (key, value)
        max_workers: Number of parallel workers
        executor: "thread" (default) or "process"
    
    Returns:
        Dictionary of {key: value} results
    """
    results = {}
    
    executor_class = (
        concurrent.futures.ThreadPoolExecutor 
        if executor == "thread" 
        else concurrent.futures.ProcessPoolExecutor
    )
    
    with executor_class(max_workers=max_workers) as executor:
        futures = {executor.submit(iterable_function, item): item for item in iterable}
        for future in concurrent.futures.as_completed(futures):
            try:
                key, value = future.result()
                results[key] = value
            except Exception as e:
                print(f"Error processing item: {e}")
    
    return results