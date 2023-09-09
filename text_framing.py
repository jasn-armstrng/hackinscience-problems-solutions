# https://www.hackinscience.org/exercises/text-framing
"""
Title: Text Framing
Author: Your Name
Date: Today's Date
Description: This program contains a function that adds a border around a given text.
It allows customization of the border characters and can handle multi-line texts and nested borders.
The border style is defined by a Frame dataclass instance which can be easily customized.
"""
from dataclasses import dataclass, replace
from datetime import datetime

@dataclass
class Frame:
    top          = "-"
    left         = "|"
    bottom       = "-"
    right        = "|"
    top_left     = "+"
    top_right    = "+"
    bottom_left  = "+"
    bottom_right = "+"

standard_frame  = Frame()
fancy_frame     = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")

def frame_text(text: str, frame: Frame) -> str:
    """
    Adds a border around a given text with the specified Frame style.

    Args:
        text (str): The text to be framed. It can be a single-line or a multi-line text.
        frame (Frame): An instance of the Frame dataclass defining the style of the border.

    Returns:
        str: The framed text as a string.

    Usage:
        >>> standard_frame = Frame()
        >>> text = "Hello, World!"
        >>> print(frame_text(text, standard_frame))
        +-------------+
        |Hello, World!|
        +-------------+
    """
    # Split text into lines if it has multiple lines and remove leading/trailing spaces
    lines: List[str] = text.split('\n')

    # Compute the max_width considering all lines and the nesting_level for the padding
    max_width: int = max(len(line) for line in lines)

    # Construct the border lines
    top_border: str = frame.top_left + frame.top * (max_width) + frame.top_right
    bottom_border: str = frame.bottom_left + frame.bottom * (max_width) + frame.bottom_right

    # Construct the nested lines. The " " ensures that multiline strings of varying lengths are bordered symmetrically
    nested_lines: list[str] = [f'{frame.left}{line}{" " * (max_width - len(line))}{frame.right}' for line in lines]

    # Join all the lines together
    result: str = '\n'.join([top_border] + nested_lines + [bottom_border])
    return result

def main() -> None:
    # Testing
    text = f"It is {datetime.now():%H:%M:%S}."
    print(text)

    framed = frame_text(text, invisible_frame)
    print(framed)

    # Testing nested
    nested_framed = frame_text(framed, standard_frame)
    print(nested_framed)

    text_2 = "It is 16h19.\nAnd it's raining."
    framed_2 = frame_text(text_2, standard_frame)
    print(framed_2)

    text_3 = "It is 11:11:23"
    framed_3 = frame_text(text_3, fancy_frame)
    print(framed_3)

    fir: str = """
      +
      *
     ***
    *****
   *******
    *****
   *******
  *********
 ***********
*************
     |||
     |||"""

    custom_frame = Frame(top='─', left='│', bottom='─', right='│', top_left='╭', top_right='╮', bottom_left='╰', bottom_right='╯')
    print(frame_text(fir, custom_frame))

if __name__ == "__main__":
    main()
