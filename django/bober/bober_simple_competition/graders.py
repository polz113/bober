from bond import make_bond


class NoneRuntime:
    def __init__(self):
        self.graders = dict()

    def add_grader(self, s):
        accepted_set = set([i.strip() for i in s.split(',')])

        def grader(answer, token, question):
            if answer == '' or answer is None:
                return question.none_score
            if answer in accepted_set:
                return question.max_score
            return question.min_score
        self.graders[s] = grader
        return grader

    def start(self):
        pass

    def get_grader(self, s):
        g = self.graders.get(s, None)
        if g is None:
            g = self.add_grader(s)
        # print self.graders, s
        return g


class BondRuntime(NoneRuntime):
    def start(self):
        pass

    def prepare_source(self, s):
        return s

    def add_grader_format(self, s, fn_name, lang):
        source = self.prepare_source(s)
        b = make_bond(lang)
        b.eval_block(source)
        self.graders[s] = self.b.callable(fn_name)
        return self.graders[s]


class JSGostisaRuntime(BondRuntime):
    def add_grader(self, s):
        return self.add_grader_format(s, 'grader', 'JavaScript')


class JSFranceRuntime(BondRuntime):
    def add_grader(self, s):
        return self.add_grader_format(s, 'grader', 'JavaScript')


class PythonExecRuntime(NoneRuntime):
    def start(self):
        pass

    def add_grader(self, s):
        compiled = compile(s, '<string>', 'single')
        exec(compiled)
        self.graders[s] = eval(compiled.co_names[0])
        return self.graders[s]


class PythonBondRuntime(NoneRuntime):
    def add_grader(self, s):
        return self.add_grader_format(s, 'grader', 'Python')


runtimes_dict = {
    0: NoneRuntime,
    1: JSGostisaRuntime,
    2: JSFranceRuntime,
    16: PythonExecRuntime,
    17: PythonBondRuntime,
}


class RuntimeManager:
    def __init__(self):
        self.runtimes = dict()
        for k, v in runtimes_dict.items():
            self.runtimes[k] = v()

    def start_runtimes(self):
        pass

    def get_grader(self, function, function_type):
        runtime = self.runtimes[function_type]
        return runtime.get_grader(function)


def init_runtimes(grader_runtime_manager=None):
    if grader_runtime_manager is None:
        grader_runtime_manager = RuntimeManager()
        grader_runtime_manager.start_runtimes()
    return grader_runtime_manager
