from dataclasses import dataclass

from pants.backend.python.target_types import PythonSourcesGeneratingSourcesField
from pants.engine.internals.graph import Owners, OwnersRequest
from pants.engine.internals.selectors import Get
from pants.engine.rules import rule, collect_rules
from pants.engine.target import InferDependenciesRequest, InferredDependencies, FieldSet, MultipleSourcesField
from pants.engine.unions import UnionRule

import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SpecialDependenciesInferenceFieldSet(FieldSet):
    required_fields = (PythonSourcesGeneratingSourcesField,)
    sources: MultipleSourcesField


class InferSpecialDependenciesRequest(InferDependenciesRequest):
    infer_from = SpecialDependenciesInferenceFieldSet


@rule
async def infer_special_dependencies(request: InferSpecialDependenciesRequest) -> InferredDependencies:
    logger.warning(request)
    owners = await Get(Owners, OwnersRequest(("helloworld/translator/foobar.py",)))
    logger.warning(owners)
    return InferredDependencies(include=owners)


def rules():
    return [
        *collect_rules(),
        UnionRule(InferDependenciesRequest, InferSpecialDependenciesRequest),
    ]

