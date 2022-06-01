# This is a 'source distribution trap', file that is EXCLUDED from the release package
# and only available on the raw source code package.
# It exists to warn 'source package' users that they are not installing the submod the right way
# and also provide them with help link (to our Discord.)

init -10000 python:
    raise RuntimeError(""
        "\n\n\n\n\n!!! PLEASE READ THIS !!!\n\n"
        "You have installed MAS Self-Harm Submod using source code package.\n"
        "Please follow instructions in the README (scroll down on the repository homepage)\n"
        "in order to get this submod to work.\n\n"
        "If you're still having trouble installing mod, feel free to ask us\n"
        "for help on our Discord: https://mon.icu/discord."
        "\n\n\n\n\n\n\n\n\n\n\n\n"
    )
