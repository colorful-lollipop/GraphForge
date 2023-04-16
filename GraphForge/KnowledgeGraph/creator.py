from ..GQL.nGQL import Task


class Creator:
    def __init__(self, name: str | None = None):
        self.space_name = name
        self._task = Task(eager=False)
        self._task_eager = Task()

    def set_name(self, name: str):
        self.space_name = name

    def add_entity_type(self, name: str, attribute: dict[str, str] | str | None = None):
        self._task.create_tag(name, attribute)

    def add_relation_type(self, rela: list[str], attribute: dict[str, str] | str | None = None):
        if len(rela) != 3:
            raise Exception("illegal relationship, eg ['S','P','O']")
        self._task.create_tag(rela[1], attribute)

    def create(self):
        if self.space_name is None:
            raise Exception("space_name is none")
        self._task_eager.create_space(self.space_name)
        # TODO
        self._task.run_all()


class Type:
    INT = 'INT'
    FLOAT = 'FLOAT'
    DOUBLE = 'DOUBLE'
    STRING = 'STRING'
    BOOL = 'BOOL'
