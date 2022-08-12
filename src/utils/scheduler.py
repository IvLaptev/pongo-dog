import threading


class Scheduler:
    '''
    Планировщик, вызывающий функцию на определённом объекте
    '''

    timer: threading.Timer

    def __init__(self, func_name: str, obj: object, interval: float):
        '''
        Параметры:
            func_name:  название функции, которая будет вызываться

            obj:        объект, на котором будет вызываться метод

            interval:   время между вызовами (секунды)
        '''
        
        self.func = getattr(obj, func_name)
        self.interval = interval

    def start(self) -> None:
        def set_interval(func, interval):
            def func_wrapper():
                set_interval(func, interval)
                func()

            self.timer = threading.Timer(interval, func_wrapper)
            self.timer.start()
            return self.timer

        set_interval(self.func, self.interval)

    def stop(self) -> None:
        self.timer.cancel()
