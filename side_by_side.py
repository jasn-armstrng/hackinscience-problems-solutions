from typing import List


def side_by_side(left: str, right: str, width: int=79, separator: str='|') -> str:
    """
    Prints two text strings side by side with a separator in between.

    The output text lines will be of specified width. The left and right texts
    are distributed evenly on each line, separated by a provided separator.

    If a text string is shorter and doesn't fill all lines, the rest of the lines
    will contain only spaces up to the separator position.

    Parameters:
    left (str): The left side text.
    right (str): The right side text.
    width (int): The width of the output lines. Default is 79.
    separator (str): The separator character used in the output lines. Default is '|'.

    Returns:
    str: Formatted text.
    """
    # The final output will be stored in this string
    text_columns: str = ""

    # If width is even, minus 1 before finding mid -point
    if width % 2 == 0:
        width -= 1

    # Separator position
    line_mid: int = width//2

    # Buffer to store each formatted line of <left chars><separator><right chars>
    buffer: List[str] = [" " for i in range(width)]

    # Markers track reading string
    left_marker: int = 0
    right_marker: int = 0

    # Calculate number of lines
    lines: int = max((len(left)//line_mid) + 1, (len(right)//line_mid) + 1)

    # Format and store lines
    for _ in range(lines):
        line_buffer: List[str] = buffer.copy()  # Create a shallow copy. Reset for each new line
        buffer_marker: int = 0  # Track the line buffers fill. Reset for each new line

        # Below, fill the line buffer with available characters up to the separator for left and to the width for right.
        for i in range(left_marker, len(left)):
            if buffer_marker == line_mid:
                break
            else:
                # Update the buffer_marker, and the string marker when the line buffer is updated.
                line_buffer[buffer_marker] = left[i]
                buffer_marker += 1
                left_marker += 1

        # When the for loop above breaks at the mid-point insert separator and
        line_buffer[line_mid] = separator
        buffer_marker = line_mid + 1  # Set the buffer_marker just after the separator to continue with right text stream

        for j in range(right_marker, len(right)):
            if buffer_marker == width:
                break
            else:
                line_buffer[buffer_marker] = right[j]
                buffer_marker += 1
                right_marker += 1

        # Update final output with the joined contents in buffer and a new-line
        text_columns += f"{''.join(line_buffer)}\n"

    return text_columns


def main() -> None:
    left_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed non risus. "
    "Suspendisse lectus tortor, dignissim sit amet, "
    "adipiscing nec, utilisez sed sin dolor."
    )

    right_string = (
    "Morbi venenatis, felis nec pretium euismod, "
    "est mauris finibus risus, consectetur laoreet "
    "sem enim sed arcu. Maecenas sit amet eleifend sem. "
    "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
    " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
    " Ut et porta augue, et convallis ante."
    )

    print(side_by_side(left_string, right_string))


if __name__ ==  "__main__":
    main()
