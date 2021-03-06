#
# Copyright (C) 2016 Bert Vermeulen <bert@biot.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from opscli.cli import get_cmdtree


_contexts = []


def context_push(name, obj=None, prompt=None):
    _contexts.append(Context(name, obj=obj, prompt=prompt))


def context_pop():
    if not _contexts:
        return False
    else:
        _contexts.pop()
        return True


def context_get(name=None):
    if name:
        for ctx in _contexts:
            if ctx.name == name:
                return ctx
        raise ValueError("unknown context")
    else:
        return _contexts[-1]


def context_names():
    names = []
    for ctx in _contexts:
        names.append(ctx.name)

    return names


class Context:
    def __init__(self, name, obj=None, prompt=None):
        self.name = name
        self.cmdtree = get_cmdtree(name)
        self.obj = obj
        self.prompt = prompt
