# csv2libsvm


Convert CSV file to libsvm format.

input可以包括string

based on: https://github.com/zygmuntz/phraug/blob/master/csv2libsvm.py


Usage example:

csvConverter = Csv2LibSvmConverter(n) # n is the count of columns in CSV file

csvConverter.convert('input_csvfile', 'output_file')


