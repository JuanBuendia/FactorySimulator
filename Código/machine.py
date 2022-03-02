class Machine():

    def __init__(self, name):

        self._name = name
        self._available = True
        self._current_work = None
        self._count_down = 0
#descriptor
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @property
        def available(self):
            return self._available

        @available.setter
        def available(self, available):
            self._available = available

        @property
        def current_work(self):
            return self.current_work

        @current_work.setter
        def current_work(self, current_work):
            self._current_work = current_work

        @property
        def count_down(self):
            return self.count_down

        @count_down.setter
        def count_down(self, count_down):
            self._count_down = count_down


        
        def __str__(self):
            return f'Machine: [Name:{self._name}, ' +\
                f'Available:{self._available}, ' +\
                f'Current work:{self._current_work}, ' +\
                f'Count down:{self.count_down}]'



         