import csv


class StringValuesHelper:
    def __init__(self, column_count):
        self._cache = [{}] * column_count

    def get_value_for(self, value_index, value):
        target_column_dict = self._cache[value_index]

        if not (value in target_column_dict):
            target_column_dict[value] = len(target_column_dict.keys())

        return target_column_dict[value]


class Csv2LibSvmConverter:
    def __init__(self, column_count, label_index=0, skip_headers=False):
        self._string_helper = StringValuesHelper(column_count)
        self._label_index = label_index
        self._skip_headers = skip_headers

    def convert(self, input_file, output_file):

        i = open(input_file, 'rb')
        o = open(output_file, 'wb')

        reader = csv.reader(i)

        if self._skip_headers:
            headers = reader.next()

        for line in reader:
            if self._label_index == -1:
                label = '1'
            else:
                label = line.pop(self._label_index)

            new_line = self._construct_line(label, line)
            o.write(new_line)

    def _is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def _construct_line(self, label, line):
        new_line = []
        if float(label) == 0.0:
            label = "0"
        new_line.append(label)

        for i, item in enumerate(line):
            concat_item = item.strip()
            if not self._is_number(item):
                concat_item = str(self._string_helper.get_value_for(i, item))

            new_item = "%s:%s" % (str(i + 1), concat_item)

            new_line.append(new_item)

        new_line = " ".join(new_line)
        new_line += "\n"
        return new_line

