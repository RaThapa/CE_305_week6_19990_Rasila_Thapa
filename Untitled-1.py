

def encoding(msg, poly):
    msg += '0' * (len(poly) - 1)
    
    msg_list = list(msg)
    poly_list = list(poly)
    
    for i in range(len(msg) - len(poly) + 1):
        if msg_list[i] == '1':
            for j in range(len(poly)):
                msg_list[i + j] = str(int(msg_list[i + j]) ^ int(poly_list[j]))
    

    return msg[:4] + ' ' + ''.join(msg_list[-(len(poly) - 1):])

# Example usage:
org_sig1 = '1010'  # 4-bit original binary data
poly1 = '100101'   # CRC polynomial

org_sig2 = '1100'  # 4-bit original binary data
poly2 = '100101'   # CRC polynomial

# Encoding examples
encoded_output1 = encoding(org_sig1, poly1)
print('Encoded Output 1:', encoded_output1)  # Output: '1010 00111'

encoded_output2 = encoding(org_sig2, poly2)
print('Encoded Output 2:', encoded_output2)  # Output: '1100 11001'



def decoding(rcv, poly):
    rcv = rcv.replace(" ", "")
    
    rcv_list = list(rcv)
    poly_list = list(poly)
    
    for i in range(len(rcv) - len(poly) + 1):
        if rcv_list[i] == '1':
            for j in range(len(poly)):
                rcv_list[i + j] = str(int(rcv_list[i + j]) ^ int(poly_list[j]))
    
    if all(bit == '0' for bit in rcv_list[-(len(poly) - 1):]):
        return 'No error'
    else:
        return 'Error'

# Example usage:
received_sig1 = '101000111'  # Received message without error (spaces removed)
poly1 = '100101'  # CRC polynomial
result1 = decoding(received_sig1, poly1)
print('Received Sig1 - Decoding Result:', result1)  # Output: 'No error'

received_sig2 = '101001111'  # Received message with 1-bit error (spaces removed)
poly2 = '100101'  # CRC polynomial
result2 = decoding(received_sig2, poly2)
print('Received Sig2 - Decoding Result:', result2)  # Output: 'Error'

received_sig3 = '110011001'  # Received message without error (spaces removed)
poly3 = '100101'  # CRC polynomial
result3 = decoding(received_sig3, poly3)
print('Received Sig3 - Decoding Result:', result3)  # Output: 'No error'

received_sig4 = '110011111'  # Received message with 2-bits error (spaces removed)
poly4 = '100101'  # CRC polynomial
result4 = decoding(received_sig4, poly4)
print('Received Sig4 - Decoding Result:', result4)  # Output: 'Error'
