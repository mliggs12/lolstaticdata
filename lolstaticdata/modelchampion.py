from typing import Mapping, List, Union
from dataclasses import dataclass
import dataclasses_json

from modelcommon import DamageType, Health, HealthRegen, Mana, ManaRegen, Armor, MagicResistance, AttackDamage, AbilityPower, AttackSpeed, AttackRange, Movespeed, CriticalStrikeChance, Lethality, CooldownReduction, GoldPer10, HealAndShieldPower, Lifesteal, MagicPenetration
from util import OrderedEnum


class Resource(OrderedEnum):
    NO_COST = "NO_COST"
    MANA = "MANA"
    ENERGY = "ENERGY"
    RAGE = "RAGE"
    FURY = "FURY"
    FEROCITY = "FEROCITY"
    HEALTH = "HEALTH"
    MAXIMUM_HEALTH = "MAXIMUM_HEALTH"
    CURRENT_HEALTH = "CURRENT_HEALTH"
    HEALTH_PER_SECOND = "HEALTH_PER_SECOND"
    MANA_PER_SECOND = "MANA_PER_SECOND"
    CHARGE = "CHARGE"
    COURAGE = "COURAGE"
    HEAT = "HEAT"
    GRIT = "GRIT"
    FLOW = "FLOW"
    SHIELD = "SHIELD"
    OTHER = "OTHER"
    NONE = "NONE"


class AttackType(OrderedEnum):
    MELEE = "MELEE"
    RANGED = "RANGED"


class Role(OrderedEnum):
    TANK = "TANK"
    FIGHTER = "FIGHTER"
    MAGE = "MAGE"
    MARKSMAN = "MARKSMAN"
    SUPPORT = "SUPPORT"
    WARDEN = "WARDEN"
    VANGUARD = "VANGUARD"
    JUGGERNAUT = "JUGGERNAUT"
    CONTROLLER = "CONTROLLER"
    SKIRMISHER = "SKIRMISHER"
    DIVER = "DIVER"
    SLAYER = "SLAYER"
    BURST = "BURST"
    BATTLEMAGE = "BATTLEMAGE"
    ENCHANTER = "ENCHANTER"
    CATCHER = "CATCHER"
    ASSASSIN = "ASSASSIN"
    SPECIALIST = "SPECIALIST"
    ARTILLERY = "ARTILLERY"


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Stats(object):
    health: Health
    health_regen: HealthRegen
    mana: Mana
    mana_regen: ManaRegen
    armor: Armor
    magic_resistance: MagicResistance
    attack_damage: AttackDamage
    movespeed: Movespeed
    acquisition_radius: float
    selection_radius: float
    pathing_radius: float
    gameplay_radius: float
    critical_strike: CriticalStrikeChance
    critical_strike_modifier: float
    attack_speed: AttackSpeed
    attack_speed_ratio: float
    attack_cast_time: float
    attack_total_time: float
    attack_delay_offset: float
    attack_range: AttackRange
    aram_damage_taken: float
    aram_damage_dealt: float
    aram_healing: float
    aram_shielding: float
    urf_damage_taken: float
    urf_damage_dealt: float
    urf_healing: float
    urf_shielding: float


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class AttributeRatings(object):
    damage: int
    toughness: int
    control: int
    mobility: int
    utility: int
    ability_reliance: int
    attack: int
    defense: int
    magic: int
    difficulty: int


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Modifier(object):
    values: List[Union[int, float]]
    units: List[str]


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Cooldown(object):
    modifiers: List[Modifier]
    affected_by_cdr: bool


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Cost(object):
    modifiers: List[Modifier]


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Leveling(object):
    attribute: str
    modifiers: List[Modifier]


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Effect(object):
    description: str
    icon: str
    leveling: List[Leveling]


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Ability(object):
    name: str
    effects: List[Effect]
    cost: Cost
    cooldown: Cooldown
    targeting: str
    affects: str
    spellshieldable: str
    resource: Resource
    damage_type: DamageType
    spell_effects: str
    projectile: str
    on_hit_effects: str
    occurrence: str
    notes: str
    blurb: str
    missile_speed: str
    recharge_rate: str
    collision_radius: str
    tether_radius: str
    on_target_cd_static: str
    inner_radius: str
    speed: str
    width: str
    angle: str
    cast_time: str
    effect_radius: str
    target_range: str


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Price(object):
    blue_essence: int
    rp: int


@dataclasses_json.dataclass_json(letter_case=dataclasses_json.LetterCase.CAMEL)
@dataclass
class Champion(object):
    id: int
    key: str
    name: str
    title: str
    full_name: str
    resource: Resource
    attack_type: AttackType
    adaptive_type: DamageType
    stats: Stats
    roles: List[Role]
    attribute_ratings: AttributeRatings
    abilities: Mapping[str, List[Ability]]
    release_date: str
    release_patch: str
    patch_last_changed: str
    price: Price

    def __json__(self):
        return self.to_json()