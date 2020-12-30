# JSON - str
# XML - int

class JSONObjectInfo:

    def get_info(self) -> str:
        return '1234'


class XMLObjectInfo:

    def get_info(self) -> int:
        return 5678

class Adapter(XMLObjectInfo):

    def get_info(self) -> int:
        return str(super(Adapter, self).get_info())

def main(obj):
    print('Info: ' + obj.get_info())

if __name__ == '__main__':
    obj = Adapter()
    main(obj)