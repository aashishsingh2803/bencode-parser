from abc import ABC, abstractmethod

class DataType(ABC):
  
  @staticmethod
  @abstractmethod
  def encode(self):
    pass

  @staticmethod
  @abstractmethod
  def decode(self):
    pass


class IntDataType(DataType):
  
  def encode(int_data):
    return "i" + str(int_data) + "e"
    
  def decode():
    pass


class StrDataType(DataType):
  
  def encode(str_data):
    return str(len(str_data)) + ":" + str_data
    
  def decode():
    pass


class ListDataType(DataType):
  
  def encode(list_data):
    output = "l"
    for element in list_data:
      output += TYPE_TO_DATA_TYPE_MAP[type(element)].encode(element)

    output +="e"
    return output

  def decode():
    pass

class DictDataType(DataType):
  
  def encode(dict_data):
    output = "d"
    for _key, _val in dict_data.items():
      output += TYPE_TO_DATA_TYPE_MAP[type(_key)].encode(_key)
      output += TYPE_TO_DATA_TYPE_MAP[type(_val)].encode(_val)

    output += "e"
    return output

  def decode():
    pass


TYPE_TO_DATA_TYPE_MAP = {
  int: IntDataType,
  str: StrDataType,
  list: ListDataType,
  dict: DictDataType
}
