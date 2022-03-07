
from typing import List


class DataPrinter:
    """Abstracts a data printer object
    """
    def __init__(self, ddd_data : bytes):
        """Instantiate a data printer

        Args:
            ddd_data (bytes): DDD data read as bytes
        """
        self.data = ddd_data

    def process(self):
        """Process the DDD data into an array of lines in a specified method

        Returns:
            List<str>: Output array of processed data
        """
        output=[]
        for _data in self.data:
            output.append(_data)
        return output

class HexPrinter(DataPrinter):
    def process(self):
        """Process the DDD data into an array of lines in HEX Format

        Returns:
            List<str>: Output array of processed data in hex format
        """
        output=[]
        for _data in self.data:
            output.append("{0:#0{1}x}".format(_data,4))
        return output

class BinaryPrinter(DataPrinter):
    def process(self):
        """Process the DDD data into an array of lines in Binary format

        Returns:
            List<str>: Output array of processed data in binary format
        """
        output=[]
        for _data in self.data:
            output.append("{0:08b}".format(_data))
        return output