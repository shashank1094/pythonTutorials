from abc import ABC, abstractmethod
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Step 1: Define Abstract Class for Operations
class Operation(ABC):
    @abstractmethod
    def execute(self, *args: float) -> float:
        pass


# Step 2: Implement Concrete Operations
class Addition(Operation):
    def execute(self, *args: float) -> float:
        return sum(args)


class Subtraction(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiplication(Operation):
    def execute(self, *args: float) -> float:
        result = 1
        for num in args:
            result *= num
        return result


class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# Unary Operations
class SquareRoot(Operation):
    def execute(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(a)


class Negation(Operation):
    def execute(self, a: float) -> float:
        return -a


# Step 3: Implement a Factory for Operations
class OperationFactory:
    _operations = {}

    @classmethod
    def register_operation(cls, symbol: str, operation: Operation):
        cls._operations[symbol] = operation

    @classmethod
    def get_operation(cls, symbol: str) -> Operation:
        if symbol not in cls._operations:
            raise ValueError(f"Operation '{symbol}' not found.")
        return cls._operations[symbol]


# Register default operations
OperationFactory.register_operation("+", Addition())
OperationFactory.register_operation("-", Subtraction())
OperationFactory.register_operation("*", Multiplication())
OperationFactory.register_operation("/", Division())
OperationFactory.register_operation("sqrt", SquareRoot())
OperationFactory.register_operation("neg", Negation())


# Step 4: Implement Memory Feature, Command Pattern, and Logging
class Calculator:
    def __init__(self):
        self.memory = None
        self.history = []
        self.redo_stack = []

    def calculate(self, operation: str, *args: float) -> float:
        try:
            operation_instance = OperationFactory.get_operation(operation)
            result = operation_instance.execute(*args)
            self.memory = result
            self.history.append((operation, args, result))
            self.redo_stack.clear()  # Clear redo stack on new operation
            logging.info(f"Performed operation: {operation} on {args} = {result}")
            return result
        except Exception as e:
            logging.error(f"Error during calculation: {e}")
            raise

    def recall_memory(self) -> float:
        if self.memory is None:
            raise ValueError("No stored memory value.")
        return self.memory

    def clear_memory(self):
        self.memory = None
        logging.info("Memory cleared.")

    def undo(self):
        if not self.history:
            raise ValueError("No operations to undo.")
        last_operation = self.history.pop()
        self.redo_stack.append(last_operation)
        logging.info(f"Undo operation: {last_operation}")
        return last_operation

    def redo(self):
        if not self.redo_stack:
            raise ValueError("No operations to redo.")
        redo_operation = self.redo_stack.pop()
        self.history.append(redo_operation)
        logging.info(f"Redo operation: {redo_operation}")
        return redo_operation


# Step 5: Example Usage
if __name__ == "__main__":
    calculator = Calculator()
    print("3 + 5 + 2 =", calculator.calculate("+", 3, 5, 2))
    print("10 - 4 =", calculator.calculate("-", 10, 4))
    print("6 * 7 * 2 =", calculator.calculate("*", 6, 7, 2))
    print("8 / 2 =", calculator.calculate("/", 8, 2))
    print("sqrt(16) =", calculator.calculate("sqrt", 16))
    print("neg(5) =", calculator.calculate("neg", 5))

    # Memory feature
    print("Recalling Memory:", calculator.recall_memory())
    calculator.clear_memory()

    # Undo/Redo Feature
    print("Undo Last Operation:", calculator.undo())
    print("Redo Last Operation:", calculator.redo())
