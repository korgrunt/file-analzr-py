
class EncodeUtils:
    @staticmethod
    def decode_to_latin_from_file(data):
        return data.data().decode('iso-8859-1')

    @staticmethod
    def encode_to_hex_from_file(data):
        return data.data().hex()

    @staticmethod
    def latin_to_hex(latin_string):
        latin_bytes = latin_string.encode('iso-8859-1')
        hex_representation = latin_bytes.hex()
        return hex_representation

    @staticmethod
    def utf8_to_hex(str):
        latin_bytes = str.encode('utf-8')
        hex_representation = latin_bytes.hex()
        return hex_representation

    @staticmethod
    def hex_to_latin(hex_string):
        hex_bytes = bytes.fromhex(hex_string)
        latin_string = hex_bytes.decode('iso-8859-1')
        return latin_string

    @staticmethod
    def hex_encode_to(hex_string, encode_format):
        hex_bytes = bytes.fromhex(hex_string)
        encoded_hex = hex_bytes.decode(encode_format)
        return encoded_hex

    @staticmethod
    def get_encoding(file_path):
        splited_file_path = file_path.split('.')
        extension = "bin"
        if splited_file_path:
            extension = splited_file_path[-1]
        encoding_map = {
            "jpeg": 'iso-8859-1',
            "jpg": 'utf-16',
            "png": 'utf-32',
            "bin": 'latin-1',
            "txt": 'utf-8',
            "md": 'utf-8',
            "html": 'utf-8',
            "css": 'utf-8',
            "js": 'utf-8',
            "java": 'utf-8',
            "py": 'utf-8',
            "json": 'utf-8',
        }
        return encoding_map.get(extension)

    @staticmethod
    def tagCodeToTagTitle(tagCode):
        tags = {
            254: "New Subfile Type",
            255: "Subfile Type",
            256: "Image Width",
            257: "Image Height",
            258: "Bits Per Sample",
            259: "Compression",
            262: "Photometric Interpretation",
            273: "Strip Offsets",
            274: "Orientation",
            277: "Samples Per Pixel",
            278: "Rows Per Strip",
            279: "Strip Byte Counts",
            282: "X-Resolution",
            283: "Y-Resolution",
            284: "Planar Configuration",
            296: "Resolution Unit",
            305: "Software",
            306: "Date/Time",
            315: "Artist",
            318: "White Point",
            319: "Primary Chromaticities",
            529: "YCbCr Coefficients",
            530: "YCbCr Sub-Sampling",
            531: "YCbCr Positioning",
            33432: "Copyright",
            34853: "Exif IFD Pointer",
            34850: "GPS Info IFD Pointer",
            40961: "Color Space",
            40962: "Pixel X Dimension",
            40963: "Pixel Y Dimension",
            40965: "Interoperability IFD Pointer",
            41486: "Focal Plane X-Resolution",
            41487: "Focal Plane Y-Resolution",
            41488: "Focal Plane Resolution Unit",
            41495: "Sensing Method",
            41728: "File Source",
            41729: "Scene Type",
            41730: "CFA Pattern",
            41985: "Custom Rendered",
            41986: "Exposure Mode",
            41987: "White Balance",
            41988: "Digital Zoom Ratio",
            41989: "Focal Length In 35mm Film",
            41990: "Scene Capture Type",
            41991: "Gain Control",
            41992: "Contrast",
            41993: "Saturation",
            41994: "Sharpness",
            41995: "Device Setting Description",
            41996: "Subject Distance Range",
            42016: "Image Unique ID",
            42032: "Camera Owner Name",
            42033: "Body Serial Number",
        }

        return tags.get(tagCode, "Unknown Tag")