class PngReader():
    _expected_magic = b'\x89PNG\r\n\x1a\n'
    
    def __init__(self, file_path) -> None:
        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' exension")
        self.__path = file_path
        self.__file_object = None
    
    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')
        
        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError('Th File is not properly formatted .png file!')
        return self
    
    def __exit__(self, type, val, tb):
        if self.__file_object is not None:
            self.__file_object.close()
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__file_object is not None:
            initial_data = self.__file_object.read(4)
        
        if self.__file_object is None or initial_data == b'':
            raise StopIteration
        else:
            chunk_len = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.__file_object.read(4)
            chunk_data = self.__file_object.read(chunk_len)
            chunk_crc = self.__file_object.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc
        
        
if __name__ == '__main__':
    with PngReader('./read_write_files/jack_russell.png') as reader:
        for l, t, d, c in reader:
            print(f'{l: 05}, {t},  {c}')