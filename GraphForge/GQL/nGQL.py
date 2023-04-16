r"""
define the basic nGQL commands
"""
import re

import type


class Task:
    def __init__(self, eager: bool = True, echo: bool = False):
        self._eager: bool = eager
        self._tasks: list[str] = []
        self._echo = echo

    def eager(self, flag: bool):
        self._eager = flag

    def echo(self, flag: bool):
        self._echo = flag

    def run_all(self):
        for sentence in self._tasks:
            if self._echo:
                print(sentence)
            # TODO
            pass
        self._tasks.clear()

    def append(self, sentence: str):
        self._tasks.append(sentence)
        if self._eager:
            self.run_all()

    def clear(self):
        self._tasks.clear()

    def __str__(self):
        return str(self._tasks)

    def __len__(self):
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks)

    def _repr_html_(self):
        items_html = "<li>" + "</li><li>".join(str(task) for task in self._tasks) + "</li>"
        return f"<ul>{items_html}</ul>"

    def create_space(
            self,
            space_name: str,
            *,
            partition_num: int = 10,
            replica_factor: int = 1,
            vid_type: str = 'FIXED_STRING(30)'
    ) -> None:
        if str == 'INT64' or str == 'INT' or re.match(r'^FIXED_STRING\(\d+\)$', s):
            self._tasks.append(
                f'create space {space_name}(partition_num={partition_num},'
                f'replica_factor={replica_factor},vid_type={vid_type});'
            )
        else:
            raise Exception("vid_type should be INT64 or FIXED_STRING(<N>)")

    def use_space(self, name: str) -> None:
        self.append(f'use {name};')

    def drop_space(self, name: str):
        self.append(f'drop space {name};')

    def __create(self, target: str, name: str, attr: dict[str, str] | None = None):
        if attr is None or len(attr) == 0:
            attr = {'value': 'str'}
        for key in attr:
            attr[key] = type.get_type(attr[key])
        attr_list: list[str] = []
        for key, value in attr.items():
            attr_list.append(f'`{key}` {value},')
            attr_list.append(',')
        attr_list.pop()
        attr_str: str = ''.join(attr_list)
        self.append(f'create {target} `{name}`({attr_str});')

    def create_tag(self, name: str, attr: dict[str, str] | None = None):
        self.__create('tag', name, attr)

    def create_edge(self, name: str, attr: dict[str, str] | None = None):
        self.__create('edge', name, attr)

    def sleep(self, time: int = 20):
        self.append(f':sleep {time};')


class GraphDB:
    def __init__(self):
        self._tasks: Task = Task()

    def run_tasks(self):
        self._tasks.run_all()

    def set_task_mode(self, *, eager, echo):
        self._tasks.eager(eager)
        self._tasks.echo(echo)
