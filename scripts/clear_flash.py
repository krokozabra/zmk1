"""
Скрипт для создания clear.uf2 файла для nRF52840 (nice!nano v2)
Этот файл полностью очищает флеш-память микроконтроллера
"""

UF2_MAGIC_START = 0x0A324655  # "UF2\n"
UF2_MAGIC_END = 0x0AB16F30
UF2_FLAG_FAMILY_ID = 0x00002000
UF2_FAMILY_ID_NRF52840 = 0xADA52840

# Создаем заголовок UF2
def create_uf2_block(addr, data):
    block = bytearray(512)
    # Магические числа
    block[0:4] = UF2_MAGIC_START.to_bytes(4, 'little')
    block[4:8] = UF2_MAGIC_END.to_bytes(4, 'little')
    # Флаги
    block[8:12] = UF2_FLAG_FAMILY_ID.to_bytes(4, 'little')
    # Адрес
    block[12:16] = addr.to_bytes(4, 'little')
    # Размер данных
    block[16:20] = len(data).to_bytes(4, 'little')
    # Номер блока
    block[20:24] = (0).to_bytes(4, 'little')
    # Всего блоков
    block[24:28] = (1).to_bytes(4, 'little')
    # ID семьи
    block[28:32] = UF2_FAMILY_ID_NRF52840.to_bytes(4, 'little')
    # Данные (пустые)
    block[32:32+len(data)] = data
    return block

# Создаем UF2 файл
with open('clear_flash.uf2', 'wb') as f:
    # Пустой блок, который очищает память
    block = create_uf2_block(0x00000000, bytes([0xFF]*476))
    f.write(block)