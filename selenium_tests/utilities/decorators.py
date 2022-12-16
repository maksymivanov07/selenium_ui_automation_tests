import inspect
import allure


def auto_step(cls):
    for name, method in inspect.getmembers(cls):
        if (not inspect.isfunction(method)) or inspect.isbuiltin(method) and method.__name__.startswith("__"):
            continue
        setattr(cls, name, allure.step(method))
    return cls
