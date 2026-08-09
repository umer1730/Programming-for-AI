import time
from fastapi import Request

async def monitoring_middleware(request: Request,call_next):
    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    response_time = end_time - start_time

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{response_time:.4f}s"
    )

    return response