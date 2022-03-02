class Job ():

    def __init__(self, machine, Job_Time):

        self._machine = machine
        self._Job_Time = Job_Time

        @property
        def machine(self):
            return self._machine

        @machine.setter
        def machine(self, machine):
            self._machine = machine

        @property
        def Job_Time(self):
            return self._Job_Time

        @Job_Time.setter
        def name(self, Job_Time):
            self._Job_Time = Job_Time

        def __str__(self):
            return f'Job: [Machine:{self._machine}, ' +\
                f'Job time:{self._Job_Time}]'