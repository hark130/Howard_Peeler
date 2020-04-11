def obfuscate_string(target_string, mask_string):
    """
        PURPOSE - Obfuscate, and de-obfuscate, a string object
        PARAMETERS
            target_string - Non-empty string to obfuscate (or de-obfuscate)
            mask_string - Non-empty string to use as a mask
        RETURN - String containing the obfuscated (or de-obfuscated) target_string
        NOTES
            - Utilizes obfuscate_bytes() under the hood
    """
    # INPUT VALIDATION
    # target_string
    if not isinstance(target_string, str):
        raise TypeError('The target_string parameter must be a bytes object instead of '
                        f'{type(target_string)}')
    elif not target_string:
        raise ValueError('The target_string parameter can not be empty')
    # mask_string
    if not isinstance(mask_string, str):
        raise TypeError('The mask_string parameter must be a bytes object instead of '
                        f'{type(mask_string)}')
    elif not mask_string:
        raise ValueError('The mask_string parameter can not be empty')

    # LOCAL VARIABLES
    target_bytes = target_string.encode()
    mask_bytes = mask_string.encode()
    result_bytes = b''

    # OBFUSCATE
    result_bytes = obfuscate_bytes(target_bytes, mask_bytes)

    # DONE
    return result_bytes.decode()


def obfuscate_bytes(target_bytes, mask_bytes):
    """
        PURPOSE - Obfuscate, and de-obfuscate, a bytes object
        PARAMETERS
            target_bytes - Non-empty byte string to obfuscate (or de-obfuscate)
            mask_bytes - Non-empty byte string to use as a mask
        RETURN - Bytes object containing the obfuscated (or de-obfuscated) target_bytes
    """
    # INPUT VALIDATION
    # target_bytes
    if not isinstance(target_bytes, bytes):
        raise TypeError('The target_bytes parameter must be a bytes object instead of '
                        f'{type(target_bytes)}')
    elif not target_bytes:
        raise ValueError('The target_bytes parameter can not be empty')
    # mask_bytes
    if not isinstance(mask_bytes, bytes):
        raise TypeError('The mask_bytes parameter must be a bytes object instead of '
                        f'{type(mask_bytes)}')
    elif not mask_bytes:
        raise ValueError('The mask_bytes parameter can not be empty')

    # LOCAL VARIABLES
    mask_len = len(mask_bytes)
    result_bytes = b''

    # OBFUSCATE
    result_bytes = bytes(c ^ mask_bytes[i % mask_len] for i, c in enumerate(target_bytes))

    # DONE
    return result_bytes
