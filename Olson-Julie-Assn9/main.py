class Genome:
    def __init__(self, string=""):
        # make everything uppercase
        self.string = string.upper()
        self.newString = ""
        for ch in self.string:
            # go through the string and get rid of any characters other than T,A,G, and C
            if ch == 'T' or ch == 'A' or ch == 'C' or ch == 'G':
                self.newString = self.newString + ch
            else:
                self.newString = self.newString

    def display(self):
        # print the edited string
        print(self.newString)

    def genes(self):
        # if there is a gene in the new string
        if ('ATG' in self.string):
            while 'ATG' in self.newString:
                # find the start of the gene
                i = self.newString.find('ATG')
                # slice the string
                s1 = self.newString[i+3:]
                s2 = self.newString[i:]
                self.newString = s2
                # replace all end letter sequences with 'end'
                self.newString = self.newString.replace('TAA', 'end')
                self.newString = self.newString.replace('TAG', 'end')
                self.newString = self.newString.replace('TGA', 'end')

                # find 'end'
                j = s1.find('end')
                if (j != -1):
                    # slice string again to isolate gene
                    s1 = s1[:j]
                    # print gene
                    print(s1)
                    # string now starts after the gene that was just printed
                    self.newString = self.newString[j:]
                else:
                    continue
        # if no genes say so
        else:
            print("no gene is found")


# write your class code above this line
# make no changes below this line

def main():

    s1 = Genome("..T.aA.DERRfDww..t.wwWWwwGC..")
    s2 = Genome("TTATGTTTTAAGGATGGGGCGTTAGTT")
    s3 = Genome("TGTGTGTATAT")
    s4 = Genome("TTATGTTTAAGGATGGGGCGTTAGTT")

    s1.display()

    print("---")
    s2.display()
    s2.genes()

    print("---")
    s3.display()
    s3.genes()

    print("---")
    s4.display()
    s4.genes()


main()