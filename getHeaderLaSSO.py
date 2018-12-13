fname=input('Nome do arquivo gff de introns: ')
try:
    file=open(fname)
except:
    print('Não foi possível abrir o arquivo:', fname)
    quit()

fname2=input('Nome do arquivo gff de exons: ')
try:
    file2=open(fname2)
except:
    print('Não foi possível abrir o arquivo:', fname2)
    quit()

for line in file:
#Intron part
    introns=line.split()
#   print(introns)
    start=int(introns[3])
    end=int(introns[4])
#   print('start:', start, "end:", end)
#    print(start,';',end)
#    print('Exons coordenadas:', start-1, end+1)
    infointron=introns[8].split(':')
    nameintron=infointron[2]
#    print(nameintron)
    stran=introns[6]
    if stran=='-':
        strand=-1
    else:
        strand=1
    chr=int(introns[0])
#Exon part
    UTR3=0
    UTR5=0
    for line in file2:
        exons=line.split()
#        print(exons[4],exons[3])
        if int(exons[3]) == int(end+1):
#           print('ACHOOOUUUU 3-UTR')
            if UTR3==0:
                name=exons[8].split(';')
                nam=name[3].split('=')
                UTR3=nam[1]
#                print('UTR-3:',UTR3)
        elif int(exons[4]) == int(start-1):
        #       print('ACHOOOOOUUU 5-UTR')
            if UTR5==0:
                name=exons[8].split(';')
        #       print(name)
                nam=name[3].split('=')
        #       print(nam)
                UTR5=nam[1]
#                print('UTR-5:',UTR5)
        else:
                continue
        file2=open(fname2)
    print(nameintron,';',chr,';',strand,';',start,';',end,';',UTR5,'-',UTR3, sep='')
    f = open( 'headerLaSSO.txt', 'a' )
    f.write("%s;%i;%s;%i;%i;%s-%s\n" % (nameintron, chr, strand, start, end, UTR5, UTR3))
    f.close()
