class AsciiHandler:    
    def get_binary(self, s):
        return ''.join(bin(ord(c))[2:].zfill(8) for c in s)
    
    def to_char(self, binary):
        chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
        return ''.join([chr(int(chunk, 2)) for chunk in chunks])
    
    def is_ascii(self, s):
        return all(ord(c) < 128 for c in s)
    