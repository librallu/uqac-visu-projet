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

        with open(filename, encoding="utf8") as f:
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

#off.eliminate_nodes(check_name)

bipartite = {}
prop = 'countries_tags'

l = off.get_fields(prop)
edges = []
for i,a in enumerate(l):
    edges.extend([ (i, j.replace(' ', '')) for j in a.split(',') ])
# now edges contains a list of (product, country)

# bipartite: country -> [product id(int)] list
for u,v in edges:
    if v in bipartite:
        bipartite[v].append(u)
    else:
        bipartite[v] = [u]


filename2 = file_name+'_edges_countries.csv'
with open(filename2, 'w+', encoding="utf8") as f:
    f.write("in out\n")
    for i in bipartite:
        if i != "":
            for j in bipartite[i]:
                f.write('{} {}\n'.format(i,j))

fields = ['product_name', 'packaging', 'additives_fr', 'nutrition-score-fr_100g', 'allergens']
missing_value = '#'

filename3 = file_name+'_nodes_countries.csv'
with open(filename3, 'w', encoding="utf8") as f:
    f.write((' '.join(['indice']+fields))+' type\n')
    for i in range(off.get_nblines()):
        tmp = off.get_row_dict(i)
        indice = str(i)
        packaging = tmp['packaging'] if tmp['packaging'] != '' else missing_value
        name = tmp['product_name'] if tmp['product_name'] != '' else missing_value
        additives = tmp['additives_fr'] if tmp['additives_fr'] != '' else missing_value
        score = tmp['nutrition-score-fr_100g'] if tmp['nutrition-score-fr_100g'] != '' else missing_value
        allergens = tmp['allergens'] if tmp['allergens'] != '' else missing_value
        f.write('{} {} {} {} {} {} {}\n'.format(indice, name.replace(' ', '-'), packaging.replace(' ', ''), additives.replace(' ', ''), score, allergens.replace(' ', ''), 0))
    for i in bipartite:
        f.write('{} {} {} {} {} {} {}\n'.format(i, "", "", "", "", "", 1))
