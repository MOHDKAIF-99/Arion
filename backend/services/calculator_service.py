"""
services/calculator_service.py — Safely evaluates basic math expressions.
"""

import ast
import operator
import re

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _safe_eval(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        return ALLOWED_OPERATORS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp):
        return ALLOWED_OPERATORS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("Unsupported expression")


def calculate(text: str) -> str:
    match = re.search(r"[\d\.\+\-\*/\(\)\s]+", text)
    if not match:
        return "I couldn't find a valid math expression in that."

    expression = match.group().strip()
    if not expression:
        return "I couldn't find a valid math expression in that."

    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree.body)
        return f"{expression.strip()} = {result}"
    except Exception:
        return "That doesn't look like a valid calculation. Try something like '25*4+10'."