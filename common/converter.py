import base64

byteorder = 'little'
def idFromInt(integerId):
    """
    Takes an integer, gets the bytes of the integer 
    in Little Endian byteorder, converts the result to a url safe base64
    and returns an id

    TODO: The implementation limits the max id of an url to 2**(3*8)
    with constant size of the generated ID set to 4.  
    """
    return base64.urlsafe_b64encode((integerId).to_bytes(3, byteorder=byteorder)).decode('ascii')

def intFromId(encodedId):
    """
    Takes an encodedId, decodes it with base64 url safe decoder,
    using Little Endian byteorder and returns an integer
    """
    return int.from_bytes(base64.urlsafe_b64decode(encodedId), byteorder=byteorder)