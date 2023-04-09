

def test(func):
    """used for test purpose only"""
    async def warpper(*args, **kwargs):
        return func(*args, **kwargs)
    return warpper