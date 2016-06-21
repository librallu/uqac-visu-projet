file_name = 'off'

class Data:
    """
    extracts data from csv.
    """
    
    def __init__(self, filename):
        """
        filename: string for the csv file
        """
        self.data_fields = {} # name -> int
        self.data_fields_order = []
        self.data = [] 

        with open(filename) as f:
            names = f.readline().split('\t')
            for i,name in enumerate(names):
                self.data_fields[name] = i
                self.data_fields_order.append(name)

            for a in f.readlines():
                fields = [b.replace('\n', '') for b in a.split('\t')]
                if len(fields) == len(names):
                    self.data.append(fields)
    
    def get_row(self, i):
        """
            :param i: row number in data
            :return: list of field values
        """
        return self.data[i]
    
    def get_nblines(self):
        """ :return: number of lines in the record """
        return len(self.data)
    
    def get_row_dict(self, i):
        res = {}
        for pos, val in enumerate(self.data_fields_order):
            res[val] = self.data[i][pos]
        return res
    
    def get_headers(self):
        return self.data_fields.keys()
    
    def get_fields(self, name):
        res = []
        i = self.data_fields[name]
        for a in self.data:
            res.append(a[i])
        return res
    
    def eliminate_nodes(self, fun_check):
        """ if fun_check returns false, eliminate node from data """
        tmp = []
        for i in range(len(self.data)):
            if fun_check(self.get_row_dict(i)):
                tmp.append(self.data[i])
        self.data = tmp
    

off = Data(file_name+'.csv')

def check_name(row):
    return row['product_name'] != ''

print(off.get_nblines())
off.eliminate_nodes(check_name)
print(off.get_nblines())
