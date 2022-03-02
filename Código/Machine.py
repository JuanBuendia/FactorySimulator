import time
class Machine: Thread

    id_machine int
    name str
    id_work
    available bool
    def define_work(self):
        pass

    def execute_task(self, ms):
        time.sleep(ms)
