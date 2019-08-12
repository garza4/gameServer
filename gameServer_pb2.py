# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gameServer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gameServer.proto',
  package='gameServer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10gameServer.proto\x12\ngameServer\"\xd7\x01\n\x06Player\x12\x0e\n\x06health\x18\x01 \x01(\x05\x12\x0f\n\x07stamina\x18\x02 \x01(\x05\x12\x0c\n\x04mana\x18\x03 \x01(\x05\x12\x34\n\tspellbook\x18\x04 \x03(\x0b\x32!.gameServer.Player.SpellbookEntry\x12\r\n\x05level\x18\x05 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x06 \x01(\x02\x12\x0c\n\x04xVal\x18\x07 \x01(\x05\x12\x0c\n\x04yVal\x18\x08 \x01(\x05\x1a\x30\n\x0eSpellbookEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"5\n\tDirection\x12\x13\n\x0bx_direction\x18\x01 \x01(\t\x12\x13\n\x0by_direction\x18\x02 \x01(\t\"2\n\x08Position\x12\x12\n\nx_position\x18\x01 \x01(\x05\x12\x12\n\ny_position\x18\x02 \x01(\x05\"\x1b\n\x06Health\x12\x11\n\thealthBar\x18\x01 \x01(\x05\"\x15\n\x05Magic\x12\x0c\n\x04mana\x18\x01 \x01(\x05\"\x1a\n\x07Stamina\x12\x0f\n\x07stamina\x18\x01 \x01(\x05\"\x18\n\x06\x41ttack\x12\x0e\n\x06\x64\x61mage\x18\x01 \x01(\x05\"v\n\tSpellBook\x12\x37\n\tspellbook\x18\x01 \x03(\x0b\x32$.gameServer.SpellBook.SpellbookEntry\x1a\x30\n\x0eSpellbookEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"\"\n\x04Pair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x03\x42\x61g\x12#\n\tequipment\x18\x01 \x03(\x0b\x32\x10.gameServer.Pair2\xeb\x01\n\x0bGameService\x12\x35\n\x04Move\x12\x15.gameServer.Direction\x1a\x14.gameServer.Position\"\x00\x12\x37\n\x0bMagicAttack\x12\x12.gameServer.Player\x1a\x12.gameServer.Player\"\x00\x12:\n\x0ePhysicalAttack\x12\x12.gameServer.Player\x1a\x12.gameServer.Player\"\x00\x12\x30\n\x04Heal\x12\x12.gameServer.Player\x1a\x12.gameServer.Player\"\x00\x62\x06proto3')
)




_PLAYER_SPELLBOOKENTRY = _descriptor.Descriptor(
  name='SpellbookEntry',
  full_name='gameServer.Player.SpellbookEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gameServer.Player.SpellbookEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='gameServer.Player.SpellbookEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=248,
)

_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='gameServer.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health', full_name='gameServer.Player.health', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='gameServer.Player.stamina', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mana', full_name='gameServer.Player.mana', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spellbook', full_name='gameServer.Player.spellbook', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='gameServer.Player.level', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp', full_name='gameServer.Player.exp', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xVal', full_name='gameServer.Player.xVal', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yVal', full_name='gameServer.Player.yVal', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PLAYER_SPELLBOOKENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=248,
)


_DIRECTION = _descriptor.Descriptor(
  name='Direction',
  full_name='gameServer.Direction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_direction', full_name='gameServer.Direction.x_direction', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_direction', full_name='gameServer.Direction.y_direction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=303,
)


_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='gameServer.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_position', full_name='gameServer.Position.x_position', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y_position', full_name='gameServer.Position.y_position', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=355,
)


_HEALTH = _descriptor.Descriptor(
  name='Health',
  full_name='gameServer.Health',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='healthBar', full_name='gameServer.Health.healthBar', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=384,
)


_MAGIC = _descriptor.Descriptor(
  name='Magic',
  full_name='gameServer.Magic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mana', full_name='gameServer.Magic.mana', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=407,
)


_STAMINA = _descriptor.Descriptor(
  name='Stamina',
  full_name='gameServer.Stamina',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stamina', full_name='gameServer.Stamina.stamina', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=435,
)


_ATTACK = _descriptor.Descriptor(
  name='Attack',
  full_name='gameServer.Attack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='damage', full_name='gameServer.Attack.damage', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=437,
  serialized_end=461,
)


_SPELLBOOK_SPELLBOOKENTRY = _descriptor.Descriptor(
  name='SpellbookEntry',
  full_name='gameServer.SpellBook.SpellbookEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gameServer.SpellBook.SpellbookEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='gameServer.SpellBook.SpellbookEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=248,
)

_SPELLBOOK = _descriptor.Descriptor(
  name='SpellBook',
  full_name='gameServer.SpellBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spellbook', full_name='gameServer.SpellBook.spellbook', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SPELLBOOK_SPELLBOOKENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=581,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='gameServer.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='gameServer.Pair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='gameServer.Pair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=617,
)


_BAG = _descriptor.Descriptor(
  name='Bag',
  full_name='gameServer.Bag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipment', full_name='gameServer.Bag.equipment', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=661,
)

_PLAYER_SPELLBOOKENTRY.containing_type = _PLAYER
_PLAYER.fields_by_name['spellbook'].message_type = _PLAYER_SPELLBOOKENTRY
_SPELLBOOK_SPELLBOOKENTRY.containing_type = _SPELLBOOK
_SPELLBOOK.fields_by_name['spellbook'].message_type = _SPELLBOOK_SPELLBOOKENTRY
_BAG.fields_by_name['equipment'].message_type = _PAIR
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['Direction'] = _DIRECTION
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Health'] = _HEALTH
DESCRIPTOR.message_types_by_name['Magic'] = _MAGIC
DESCRIPTOR.message_types_by_name['Stamina'] = _STAMINA
DESCRIPTOR.message_types_by_name['Attack'] = _ATTACK
DESCRIPTOR.message_types_by_name['SpellBook'] = _SPELLBOOK
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['Bag'] = _BAG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {

  'SpellbookEntry' : _reflection.GeneratedProtocolMessageType('SpellbookEntry', (_message.Message,), {
    'DESCRIPTOR' : _PLAYER_SPELLBOOKENTRY,
    '__module__' : 'gameServer_pb2'
    # @@protoc_insertion_point(class_scope:gameServer.Player.SpellbookEntry)
    })
  ,
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Player)
  })
_sym_db.RegisterMessage(Player)
_sym_db.RegisterMessage(Player.SpellbookEntry)

Direction = _reflection.GeneratedProtocolMessageType('Direction', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTION,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Direction)
  })
_sym_db.RegisterMessage(Direction)

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), {
  'DESCRIPTOR' : _POSITION,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Position)
  })
_sym_db.RegisterMessage(Position)

Health = _reflection.GeneratedProtocolMessageType('Health', (_message.Message,), {
  'DESCRIPTOR' : _HEALTH,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Health)
  })
_sym_db.RegisterMessage(Health)

Magic = _reflection.GeneratedProtocolMessageType('Magic', (_message.Message,), {
  'DESCRIPTOR' : _MAGIC,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Magic)
  })
_sym_db.RegisterMessage(Magic)

Stamina = _reflection.GeneratedProtocolMessageType('Stamina', (_message.Message,), {
  'DESCRIPTOR' : _STAMINA,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Stamina)
  })
_sym_db.RegisterMessage(Stamina)

Attack = _reflection.GeneratedProtocolMessageType('Attack', (_message.Message,), {
  'DESCRIPTOR' : _ATTACK,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Attack)
  })
_sym_db.RegisterMessage(Attack)

SpellBook = _reflection.GeneratedProtocolMessageType('SpellBook', (_message.Message,), {

  'SpellbookEntry' : _reflection.GeneratedProtocolMessageType('SpellbookEntry', (_message.Message,), {
    'DESCRIPTOR' : _SPELLBOOK_SPELLBOOKENTRY,
    '__module__' : 'gameServer_pb2'
    # @@protoc_insertion_point(class_scope:gameServer.SpellBook.SpellbookEntry)
    })
  ,
  'DESCRIPTOR' : _SPELLBOOK,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.SpellBook)
  })
_sym_db.RegisterMessage(SpellBook)
_sym_db.RegisterMessage(SpellBook.SpellbookEntry)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Pair)
  })
_sym_db.RegisterMessage(Pair)

Bag = _reflection.GeneratedProtocolMessageType('Bag', (_message.Message,), {
  'DESCRIPTOR' : _BAG,
  '__module__' : 'gameServer_pb2'
  # @@protoc_insertion_point(class_scope:gameServer.Bag)
  })
_sym_db.RegisterMessage(Bag)


_PLAYER_SPELLBOOKENTRY._options = None
_SPELLBOOK_SPELLBOOKENTRY._options = None

_GAMESERVICE = _descriptor.ServiceDescriptor(
  name='GameService',
  full_name='gameServer.GameService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=664,
  serialized_end=899,
  methods=[
  _descriptor.MethodDescriptor(
    name='Move',
    full_name='gameServer.GameService.Move',
    index=0,
    containing_service=None,
    input_type=_DIRECTION,
    output_type=_POSITION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MagicAttack',
    full_name='gameServer.GameService.MagicAttack',
    index=1,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PhysicalAttack',
    full_name='gameServer.GameService.PhysicalAttack',
    index=2,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Heal',
    full_name='gameServer.GameService.Heal',
    index=3,
    containing_service=None,
    input_type=_PLAYER,
    output_type=_PLAYER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMESERVICE)

DESCRIPTOR.services_by_name['GameService'] = _GAMESERVICE

# @@protoc_insertion_point(module_scope)
