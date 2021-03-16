from enum import Enum


class SensorType(Enum):
    Any = -1
    Hydrophone = 0
    Voice = 1


class PipeMaterialType(Enum):
    Any = -1
    Unknown = 0        # Comment: None,             Color: 0, ShortName: Unk
    Metal = 1          # Comment: Steel,            Color: 0, ShortName: Metal
    PVC = 2            # Comment: Black plastic,    Color: 0, ShortName: PVC
    AzbestCement = 3   # Comment: None,             Color: F, ShortName: AC
    PolyEthelen = 4    # Comment: None,             Color: 0, ShortName: PE
    Concrete = 5       # Comment: None,             Color: 0, ShortName: Concrete
    LargeDiameter = 6  # Comment: None,             Color: 8, ShortName: LargeD
    CastIron = 7       # Comment: None,             Color: 0, ShortName: CI
    Brass = 8          # Comment: None,             Color: 0, ShortName: Brass
    Wood = 9           # Comment: None,             Color: 5, ShortName: Woood
    Wall = 10          # Comment: None,             Color: 6, ShortName: Wall
    DuctileIron = 11   # Comment: None,             Color: 7, ShortName: DI
    Copper = 12        # Comment: None,             Color: F, ShortName: Copper
    Lead = 13          # Comment: None,             Color: a, ShortName: Lead
    MDPE = 14          # Comment: None,             Color: f, ShortName: MDPE


class AlgParamOperationType(Enum):
    NoOperation = 0
    Replace = 1
    Multiply = 2


