def get_args_for_decorator(*args):
    def decorator(func):
        def wrapper():
            func(args)

        return wrapper

    return decorator


if __name__ == '__main__':
    @get_args_for_decorator(1, 2, 3, 5, 6)
    def args_without_first_arg(args):
        print(args[1:])


    args_without_first_arg()
