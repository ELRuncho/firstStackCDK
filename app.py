#!/usr/bin/env python3

from aws_cdk import core

from first_stack.first_stack_stack import FirstStackStack


app = core.App()
FirstStackStack(app, "first-stack")

app.synth()
