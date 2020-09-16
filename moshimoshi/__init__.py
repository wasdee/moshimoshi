import importlib
import json
from inspect import iscoroutine
from json import JSONDecodeError
from typing import Callable

from parse import parse


class moshi:
    def __new__(cls, to: str, *args, fallback: Callable = None, **kwargs):
        function_path = a_json = to

        try:
            call_detail = json.loads(a_json)

            function_path = call_detail["call"]
            # prioritize args and kwargs
            args = [*call_detail["args"], *args]
            kwargs = {**call_detail["kwargs"], **kwargs}

        except JSONDecodeError:
            pass

        parsed = parse(r"{import_path}:{function_name:w}", function_path)
        if parsed:
            if fallback:
                return fallback(*args, **kwargs)
            else:
                raise Exception("argument `to` is invalid.")

        import_path = parsed["import_path"]
        function_name = parsed["function_name"]

        try:
            module = importlib.import_module(f"{import_path}")
            function = getattr(module, function_name)
            return function(*args, **kwargs)

        except ModuleNotFoundError as e:
            if fallback:
                return fallback(*args, **kwargs)

            else:
                raise e

    @staticmethod
    async def moshi(*args, **kwargs):
        function_path = aJson = args[0]

        # isolate fallback from kwargs
        fallback = kwargs.get("fallback")
        if fallback:
            del kwargs["fallback"]

        try:
            call_detail = json.loads(aJson)

            function_path = call_detail["call"]
            # prioritize args and kwargs
            args = [*call_detail["args"], *args]
            kwargs = {**call_detail["kwargs"], **kwargs}

        except JSONDecodeError:
            pass

        parsed = parse(r"{import_path}:{function_name:w}", function_path)
        import_path = parsed["import_path"]
        function_name = parsed["function_name"]

        try:
            module = importlib.import_module(f"{import_path}")
            function = getattr(module, function_name)
            ret = function(*args, **kwargs)
            if iscoroutine(ret):
                await ret

        except ModuleNotFoundError as e:
            if fallback:
                ret = fallback(*args, **kwargs)
                if iscoroutine(ret):
                    await ret

            else:
                raise e
