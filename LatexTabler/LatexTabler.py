#This is a collection of classes and methods to allow quick outputting to LaTex tables
#possibly in the context of a pyROOT script...
#AGB - 28/10/10

def json_extractor(jfile):
    import json
    t=json.load(t)
    return t

def tables_maker(t):
    the_tables=[]
    for k in t.keys():
        tab=table(t[k]['row_headers'],t[k]['col_headers'],t[k]['rows'],t[k]['cols'],t[k]['title'])
        the_tables.append(tab)
        
    return the_tables


class table:
    def __init__(self,rh=[],ch=[],r=[],c=[],title=''):
        self._r_header=rh
        self._c_header=ch
        self._rows=r
        self._cols=c
        self._title=title
        if ch:
            #this is a hacky fix for the time being
            if len(self._cols)!=len(ch[0]):
                for i in range(len(ch[0])):
                    self._cols.append([])
        if r:
            if len(self._cols)!=len(r[0]):
                for i in range(len(r[0])):
                    self._cols.append([])

    def __repr__(self):
        return "table"
    def __str__(self):
        return 'row headers: ' + str(self._r_header)+'\n'\
        'col headers: ' + str(self._c_header)+'\n'\
        'rows: ' + str(self._rows)+'\n'\
        'cols: ' + str(self._cols)

    def get_title(self):
        return self._title
        
    def num_rows(self):
        return len(self._rows)

    def num_cols(self):
        return len(self._cols)
        
    def r_fill(self, rows):
        self._rows=rows

    def add_row(self, row):
        self._rows.append(row)

    def c_fill(self, columns):
        self._cols=columns
        
    # @classmethod  THIS ALL NEEDS REDOING
    
    # def dic_fill(self, dic, name):
    #     self._r_header=dic[name]['row_headers']
    #     self._c_header=dic[name]['col_headers']
    #     if "rows" in dic[name].keys():
    #         self.r_fill(dic[name]["rows"])
    #     for i in range (len(dic[name]["rows"][0])):#assume that we have same num cols for all rows ie regular table
    #         self._cols.append([])
    #     if "cols" in dic[name].keys():
    #         self.c_fill(cols)
    #     return

    # def json_fill(self, t, name):
    #     import json
    #     t=json.load(j)
    #     self._r_header=t[name]['row_headers']
    #     self._c_header=t[name]['col_headers']
    #     if "rows" in t[name].keys():
    #         self.r_fill(t[name]["rows"])
    #     for i in range (len(t[name]["rows"][0])):#assume that we have same num cols for all rows ie regular table
    #         self._cols.append([])
    #     if "cols" in t[name].keys():
    #         self.c_fill(cols)
    #     return
    
    def mod_tab_elem(self, x, y):
        if x > self._cols:
            print 'Warning: x entry out of range'
            sys.exit()
        if y > self._rows:
            print 'Warning: y entry out of range'
            sys.exit()

def tex_wrapping(filename):#basically doesn't work....
    f=open(filename,'a+')
    f.seek(0)
    f.writelines(['\documentclass{article}\n','\usepackage[english]{babel}\n','\\begin{document}\n'])
    f.seek(2)
    f.write('\end{document}')
    f.close()
    return

def file_out(lines, outpath='./', filename='table.tex', append=False):
    
    import os, sys
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    if not outpath.endswith('/'):
        outpath+='/'
    if not filename.endswith('.tex'):
        filename+='.tex'
    if os.path.exists(outpath+filename) and append:
        tfile = open(outpath+filename, 'a')
    elif os.path.exists(outpath+filename) and not append:
        filename = filename.rstrip('.tex') + '_ow_.tex'
    tfile = open(outpath+filename, "w")
    tfile.writelines(lines)
    tfile.close()
    return

class texTable(table):
    def __init__(self, tab = None, *args):
        self._lines=[]
        self._caption=''
        if tab is None:
            base = table(*args)
        else:
            base = tab
        self.__dict__.update(base.__dict__)
        
        self._format=[]#the alignment of our table
        for c in range(tab.num_cols()):
            self._format.append('c')

    def __repr__(self):
        print "texTable()"

    # def forma(label):
    #     if label='centerall':
    #         for c in

    def get_rtex(self):
        return self._lines

    def texify(self):

        self._lines.append('\\begin{table}\n')
        self._lines.append('\\begin{center}\n')
        if self._caption:
            self._lines.append('\caption{'+self._caption+'}\n')
        s=r'\begin{tabular}{'
        for i in self._format:
            s=s+'|'+i
        s+='|'
        self._lines.append(s +'}\n')
        self._lines.append('\hline\n')
        for ch in self._c_header[:-1]:#column headers
            self._lines.append(str(ch) + '  &  ')
        self._lines.append(str(self._c_header[-1]))
        self._lines.append('\\\ \hline\n')
        self._lines.append('\hline\n')
        for r in self._rows:#only deal with rows so far
            for entry in r[:-1]:
                self._lines.append(str(entry) + '  &  ')
            self._lines.append(str(r[-1]))
            self._lines.append('\\\ \hline\n')
        self._lines.append('\end{tabular}\n')
        self._lines.append('\end{center}\n')
        self._lines.append('\end{table}\n')
        return

    def add_caption(self,caption):
        self._caption=caption
        return
        

    def pdfout(self):
        tex_file = self.texout
        return 
