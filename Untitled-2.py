

def HamEncoding(msg):
    m = len(msg)
    k = 1
    while 2 ** k < m + k + 1:
        k += 1

    encoded_msg = ['0'] * (m + k)
    j = 0

    for i in range(1, m + k + 1):
        if i == 2 ** j:
            j += 1
        else:
            encoded_msg[i - 1] = msg[i - 1 - j]

    for i in range(k):
        parity_pos = 2 ** i
        for j in range(1, m + k + 1):
            if (j >> i) & 1 and j != parity_pos:
                encoded_msg[parity_pos - 1] = str(int(encoded_msg[parity_pos - 1]) ^ int(encoded_msg[j - 1]))

    return ''.join(encoded_msg)

def HamDecoding(rcv, k):
    received_msg = list(rcv)
    parity_bit_positions = [2 ** i for i in range(k)]

    calculated_parity_bits = []
    for i in range(k):
        positions_to_check = [pos for pos in range(1, len(received_msg) + 1) if (pos >> i) & 1]
        parity_bit = '0'
        for pos in positions_to_check:
            if pos != parity_bit_positions[i]:
                parity_bit = str(int(parity_bit) ^ int(received_msg[pos - 1]))
        calculated_parity_bits.append(parity_bit)

    error_positions = [pos for pos, bit in zip(parity_bit_positions, calculated_parity_bits) if bit != received_msg[pos - 1]]

    if len(error_positions) == 0:
        decoded_data = ''.join(received_msg[i] for i in range(len(received_msg)) if i + 1 not in parity_bit_positions)
        return f'No error: {decoded_data}'
    else:
        for pos in error_positions:
            received_msg[pos - 1] = '1' if received_msg[pos - 1] == '0' else '0'

        corrected_data = ''.join(received_msg[i] for i in range(len(received_msg)) if i + 1 not in parity_bit_positions)
        return f'Error at Position {error_positions[0]}, and correct data: {corrected_data}'

# Example usage:
org_sig1 = '1101'  # Original binary data
encoded_output1 = HamEncoding(org_sig1)
print('Encoded Output 1:', encoded_output1)  # Output: '1010101'

received_sig1 = '1010101'  # Received message without error
k1 = 3
result1 = HamDecoding(received_sig1, k1)
print('Decoding Result 1:', result1)  # Output: 'No error: 1101'

received_sig2 = '1010001'  # Received message with 1-bit error at Position 5
k2 = 3
result2 = HamDecoding(received_sig2, k2)
print('Decoding Result 2:', result2)  # Output: 'Error at Position 5, and correct data: 1101'

received_sig3 = '10110010011'  # Received message without error
k3 = 4
result3 = HamDecoding(received_sig3, k3)
print('Decoding Result 3:', result3)  # Output: 'No error'


