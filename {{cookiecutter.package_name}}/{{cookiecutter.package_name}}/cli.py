#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# from .{{cookiecutter.package_name}} import *
import click


@click.command()
@click.argument('files', nargs=-1)
@click.option('--options', '-o', default=None, type=str, help='')
def main(files, options):
    pass


if __name__ == '__main__':
    main()
