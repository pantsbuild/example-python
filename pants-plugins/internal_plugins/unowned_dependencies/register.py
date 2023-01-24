from internal_plugins.unowned_dependencies.rules import rules as unowned_deps_rules


def rules():
    return [*unowned_deps_rules()]
