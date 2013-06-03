from Bio import SeqIO
import json

ecoli = SeqIO.read('sequence-e-coli.gb', 'genbank')
ec_genes = [a for a in ecoli.features if a.type=='gene']
ec_length = []
for g in ec_genes:
    c = 0
    for i, sub in enumerate(g.sub_features):
        d = {'name': '%s_sub%d' % (g.qualifiers['gene'][0], i),
             'x': sub.location.end - sub.location.start}
        ec_length.append(d)
        c += 1
    if c > 0:
        print 'ec: found %d subfeatures' % c
        continue                     
    d = {'name': g.qualifiers['gene'][0], 'x': g.location.end - g.location.start}
    ec_length.append(d)

tmaritima = SeqIO.read('sequence-t-maritima.gb', 'genbank')
tm_genes = [a for a in tmaritima.features if a.type=='gene']
tm_length = []
for g in tm_genes:
    c = 0
    for i, sub in enumerate(g.sub_features):
        d = {'name': '%s_sub%d' % (g.qualifiers['locus_tag'][0], i),
             'x': sub.location.end - sub.location.start}
        tm_length.append(d)
        c += 1
    if c > 0:
        print 'ec: found %d subfeatures' % c
        continue                     
    d = {'name': g.qualifiers['locus_tag'][0], 'x': g.location.end - g.location.start}
    tm_length.append(d)
        
out = {'data': [ec_length, tm_length],
       'options': {
           'x_axis_label':'gene length',
           'x_data_label':'E. coli MG1655 genes',
           'y_data_label':'T. maritima genes'
           }
      }

print 'max %d' % max([a['x'] for a in tm_length])
print 'min %d' % min([a['x'] for a in tm_length])
    
filename = 'ec-tm-gene-length.json'
with open(filename, 'w') as f:
        json.dump(out, f)
