from dataclasses import dataclass, field

@dataclass(frozen=True)
class Car:
    #id : int
    name : str
    price : int
    mileage : int
    fuel_type : str
    color : str
    transmisson_type : str
    outside_steelWork : int 
    outside_change : int
    frame_steelWork :int
    frame_change : int

    accident : str

    pass_terior : int
    pass_tire : int
    pass_consumable : int
    pass_lowerBody : int

    notice_terior : int
    notice_tire : int
    notice_consumable : int
    notice_lowerBody : int

    optionList_exterior : list[str] = field(default_factory=list)
    optionList_interior : list[str] = field(default_factory=list)
    optionList_safety : list[str] = field(default_factory=list)
    optionList_convenience : list[str] = field(default_factory=list)

    damage_amount : int
    damage_count : int
    owner_change : int 
    caution_cnt : int
    owner_age : int
    owner_sex : str
    register_gu : str
    usage_duration : float

