from data_type import TYPE_TO_DATA_TYPE_MAP

class BencodeParser( ):
  def __init__(self):
    pass

  # returns bencoded of the value.
  @staticmethod
  def encode(data):
    data_type = type(data)
    print(f"data_type for data = {data} is {data_type}")
    return TYPE_TO_DATA_TYPE_MAP[data_type].encode(data)

  @staticmethod
  def decode(self, data):
    data_type = type(data)
    return TYPE_TO_DATA_TYPE_MAP[data_type].decode(data)


print(f'encoded form - {BencodeParser.encode("random string 12345:asas")}')
print(f"encoded form - {BencodeParser.encode(1)}")
print(f'encoded form - {BencodeParser.encode({"a":1, "b": "2", 3: "c"})}')
print(f"encoded form - {BencodeParser.encode(['a', 'b', 1])}")
print(f'encoded form - {BencodeParser.encode({"a":1, "b": "2", 3: [1, 2, "abcd"]})}')
