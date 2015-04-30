__author__ = 'mazurdm1'
import documentfactory as df


data = {'Name': 'Daniel', 'Role': 'Student', 'Hobbies': ['airsoft', 'photography']}

to_print = df.DocumentFactory.parse_to_xml(data)

print(to_print)

