from abc import ABC, abstractmethod
from typing import Type

# Step 1: Common interface for every element in the company tree
class ICompanyComponent(ABC):
    """
    This interface lets us treat employees and departments in the same way.
    """

    @abstractmethod
    def getTotalSalary(self) -> float:
        """
        Return the total salary for this component.
        For an employee it is just their own salary,
        for a department it will be the sum of all its children.
        """
        raise NotImplementedError

    @abstractmethod
    def doOperation(self, task: str) -> None:
        """
        Handle a task.
        An employee will do the task directly.
        A department will pass the task to all of its children.
        """
        raise NotImplementedError


# Step 2: Leaf class – Employee
class Employee(ICompanyComponent):
    """
    Leaf node in the Composite pattern.
    An employee does not contain any other elements.
    """

    def __init__(self, name: str, position: str, salary: float) -> None:
        self.__name = name
        self.__position = position
        self.__salary = salary

    # Getters so other parts of the program can read these values
    @property
    def name(self) -> str:
        return self.__name

    @property
    def position(self) -> str:
        return self.__position

    @property
    def salary(self) -> float:
        return self.__salary

    def getTotalSalary(self) -> float:
        # For a single employee, the total salary is just their own salary
        return self.__salary

    def doOperation(self, task: str) -> None:
        # When a task is assigned directly to an employee
        print(f"[EMPLOYEE] {self.__name} ({self.__position}) is performing task: {task}")


# Step 3: Composite class – Department
class Department(ICompanyComponent):
    """
    Composite node in the company tree.
    A department can contain both employees and other departments.
    """

    def __init__(self, name: str) -> None:
        self.__name = name
        # This list holds all direct children (employees or sub-departments)
        self.__children: list[ICompanyComponent] = []

    @property
    def name(self) -> str:
        return self.__name

    def add(self, component: Type[ICompanyComponent]) -> None:
        """
        Attach a new child under this department.
        This is how we grow the tree structure.
        """
        self.__children.append(component)

    def remove(self, component: Type[ICompanyComponent]) -> None:
        """
        Detach a child from this department if it exists.
        """
        if component in self.__children:
            self.__children.remove(component)
        else:
            # Helpful message if we try to remove something that is not here
            print(f"I don't have {getattr(component, 'name', 'this component')}, so I can't remove it.")

    def getTotalSalary(self) -> float:
        """
        Ask each child for its total salary and add everything up.
        This shows the main idea of the Composite pattern:
        the department does not need to know if a child is an employee
        or another department.
        """
        total = 0.0
        for child in self.__children:
            total += child.getTotalSalary()
        return total

    def doOperation(self, task: str) -> None:
        """
        A department receives a task and forwards it to all of its children.
        Each child will handle the task according to its own implementation.
        """
        print(f"[DEPARTMENT] {self.__name} received task: {task}")
        for child in self.__children:
            child.doOperation(task)

    def showHierarchy(self, indent: str = "") -> None:
        """
        Print a simple text representation of the organization tree.
        The 'indent' parameter helps to show different levels clearly.
        """
        print(f"{indent}<DEPARTMENT> {self.__name}")
        for child in self.__children:
            if isinstance(child, Department):
                child.showHierarchy(indent + "  ")
            elif isinstance(child, Employee):
                print(
                    f"{indent}  <EMPLOYEE> {child.name} "
                    f"({child.position}) - Salary: {child.salary}"
                )


# Step 4: Client code – build an example company and use the composite
def run_demo() -> None:
    """
    Build a small company structure and demonstrate:
    - how the tree is built
    - how total salaries are computed
    - how tasks can be assigned at different levels
    """

    # Top-level department (represents the whole company)
    company = Department("Head Office")

    # Sub-departments
    hr_department = Department("HR Department")
    it_department = Department("IT Department")
    dev_team = Department("Development Team")
    qa_team = Department("QA Team")

    # Employees
    e1 = Employee("Alice", "HR Manager", 70000)
    e2 = Employee("Bob", "HR Assistant", 45000)
    e3 = Employee("Charlie", "IT Manager", 80000)
    e4 = Employee("Diana", "Backend Developer", 90000)
    e5 = Employee("Ethan", "Frontend Developer", 85000)
    e6 = Employee("Fiona", "QA Engineer", 65000)

    # Build the tree structure:
    # HR department has two employees
    hr_department.add(e1)
    hr_department.add(e2)

    # Development and QA teams belong to IT
    dev_team.add(e4)
    dev_team.add(e5)
    qa_team.add(e6)

    it_department.add(e3)
    it_department.add(dev_team)
    it_department.add(qa_team)

    # Company has HR and IT as its direct children
    company.add(hr_department)
    company.add(it_department)

    # 1) Show the hierarchy
    print("=== COMPANY HIERARCHY ===")
    company.showHierarchy()

    # 2) Show salary calculations at different levels
    print("\n=== TOTAL SALARIES ===")
    print(f"Total salary for HR Department: {hr_department.getTotalSalary()}")
    print(f"Total salary for IT Department: {it_department.getTotalSalary()}")
    print(f"Total salary for entire Company: {company.getTotalSalary()}")

    # 3) Assign a task to a single employee (leaf)
    print("\n=== ASSIGN TASK TO SINGLE EMPLOYEE ===")
    e4.doOperation("Implement new authentication module")

    # 4) Assign a task to a whole department (composite)
    print("\n=== ASSIGN TASK TO A DEPARTMENT ===")
    it_department.doOperation("Prepare quarterly IT infrastructure report")

    # 5) Assign a task to the entire company (top-level composite)
    print("\n=== ASSIGN TASK TO ENTIRE COMPANY ===")
    company.doOperation("Prepare annual performance review documents")


if __name__ == "__main__":
    run_demo()
