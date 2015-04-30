__author__ = 'mazurdm1'


class DocumentFactory():

    def __index__(self):
        pass

    @staticmethod
    def parse_to_xml(dic):
        output = ""
        space = "   "
        output += "<Document>\n"
        for i, x in dic.iteritems():
            output += space*1 + "<" + i + ">\n"

            if isinstance(x, list):
                for k in x:
                    output += space*2 + k + "\n"
            else:
                output += space*2 + x + "\n"

            output += space*1 + "</" + i + ">\n"

        output += "</Document>"
        return output

    @staticmethod
    def parse_to_json(dic):
        output = ""
        space = "   "
        output += "<Document>\n"
        for i, x in dic.iteritems():
            output += space*1 + "<" + i + ">\n"

            if isinstance(x, list):
                for k in x:
                    output += space*2 + k + "\n"
            else:
                output += space*2 + x + "\n"

            output += space*1 + "</" + i + ">\n"

        output += "</Document>"
        return output