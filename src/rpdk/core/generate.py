"""This sub command generates code from the provider definition for a project.

Projects can be created via the 'init' sub command.
"""
import logging

from .project import Project

LOG = logging.getLogger(__name__)


def generate(_args):
    project = Project()
    project.load()
    project.generate()


def setup_subparser(subparsers, parents):
    # see docstring of this file
    parser = subparsers.add_parser("generate", description=__doc__, parents=parents)
    parser.set_defaults(command=generate)