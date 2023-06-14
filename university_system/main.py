"""
main.py
-------

This script initializes the Interface class from the `modules.interface` module
and displays the user interface.
"""

from modules.interface import Interface


def main():
    """
    Initialize the Interface class and display the user interface.
    """
    interface = Interface()

    interface.show_interface()


if __name__ == "__main__":
    main()
