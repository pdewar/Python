#Problem 1(b)
#Author: Dewar P.

def rle_decompress(in_RLE):
    i = 0
    n = ''
    while i < len(in_RLE):
            if in_RLE[i] == "*":
                l = 0
                while l < int(in_RLE[i+1]):
                    n = n + (in_RLE[i+2])
                    l = l+1
                i = i+1
            else:
                n = n + in_RLE[i]
            i = i+1
    return n

if __name__ == "__main__":
    print(rle_decompress("*61000*51"))
    print(rle_decompress("00*41000"))
    print(rle_decompress("0*41000"))
    print(rle_decompress("1*50*51"))