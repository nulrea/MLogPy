"""
A file for all the objects in the game in `@`.
"""

# Built-in
## Processor
THIS = '@this'
"The logic block executing the code"
THISX = '@thisx'
"X coordinate of the block executing the code"
THISY = '@thisy'
"Y coordinate of the block executing the code"
LINKS = '@links'
"Total number of blocks linked to this processor"
IPT = '@ipt'
"Execution speed of the processor in instructions per tick (60 ticks = 1 second)"
## General
FALSE = 'false'
"0"
TRUE = 'true'
"1"
PI = '@pi' # 3.141592653589793
"The mathematical constant pi (3.141...)"
E = '@e' # 2.718281828459045
"The mathematical constant e (2.718...)"
DEG_TO_RAD = '@degToRad'
"Multiply by this number to convert degrees to radians"
RAD_TO_DEG = '@radToDeg'
"Multiply by this number to convert radians to degrees"
## Map
TIME = '@time'
"Playtime in current save, in miliseconds"
TICK = '@tick'
"Playtime in current save, in ticks (1 second = 60 ticks)"
SECOND = '@second'
"Playtime in current save, in seconds"
MINUTE = '@minute'
"Playtime in current save, in minutes"
WAVE_NUMBER = "@waveNumber"
"Current wave number, if waves are enabled"
WAVE_TIME = "@waveTime"
"Countdown timer for waves, in seconds"
MAP_WIDTH = '@mapw'
"Map width in tiles"
MAP_HEIGHT = '@maph'
"Map height in tiles"
WAIT = '@wait'
## Network/Clientside [World Processor Only]
SERVER = '@server'
"True if the code is running on a server or in singleplayer, false otherwise"
CLIENT = '@client'
"True if the code is running on a client connected to a server"
CLIENT_LOCATE = '@clientLocate'
"Locate of the client running the code. For example: en_US"
CLIENT_UNIT = '@clientUnit'
"Unit of client running the code"
CLIENT_NAME = '@clientName'
"Player name of client running the code"
CLIENT_TEAM = '@clientTeam'
"Team ID of client running the code"
CLIENT_MOBILE = '@clientMobile'
"True if the client is running the code on mobile, false otherwise"
## Lookup
BLOCK_COUNT = '@blockCount'
"Total number of types of block content in the game; used with the lookup instruction"
UNIT_COUNT = '@unitCount'
"Total number of types of unit content in the game; used with the lookup instruction"
ITEM_COUNT = '@itemCount'
"Total number of types of item content in the game; used with the lookup instruction"
LIQUID_COUNT = '@liquidCount'
"Total number of types of liquid content in the game; used with the lookup instruction"

# Items
COPPER = '@copper'
LEAD = '@lead'
METAGLASS = '@metaglass'
GRAPHITE = '@graphite'
SAND = '@sand'
COAL = '@coal'
TITANIUM = '@titanium'
THORIUM = '@thorium'
SCRAP = '@scrap'
SILICON = '@silicon'
PLASTANIUM = '@plastanium'
PHASE_FABRIC = '@phase-fabric'
SURGEALLOY = '@surgealloy'
SPORE_POD = '@spore-pod'
BLAST_COMPOUND = '@blast-compound'
PYRATITE = '@pyratite'
BERYLLIUM = '@beryllium'
TUNGSTEN = '@tungsten'
OXIDE = '@oxide'
CARBINE = '@carbine'

# Fluids
WATER = '@water'
SLAG = '@slag'
OIL = '@oil'
CYROFLUID = '@cryofluid'
NEOPLASM = '@neoplasm'
ARKYSITE = '@arkysite'
OZONE = '@ozone'
HYDROGEN = '@hydrogen'
NITROGEN = '@nitrogen'
CYANOGEN = '@cyanogen'

# Units and buildings
DAGGER = '@dagger'
MACE = '@mace'
FORTRESS = '@fortress'
SCEPTER = '@scepter'
REIGN = '@reign'
NOVA = '@nova'
PULSAR = '@pulsar'
QUASAR = '@quasar'
VELA = '@vela'
CORVUS = '@corvus'
CRAWLER = '@crawler'
ATRAX = '@atrax'
SPIROCT = '@spiroct'
ARKYID = '@arkyid'
TOXOPID = '@toxopid'
FLARE = '@flare'
HORIZON = '@horizon'
ZENITH = '@zenith'
ANTUMBRA = '@antumbra'
ECLIPSE = '@eclipse'
MONO = '@mono'
POLY = '@poly'
MEGA = '@mega'
QUAD = '@quad'
OCT = '@oct'
RISSO = '@risso'
MINKE = '@minke'
BRYDE = '@bryde'
SEI = '@sei'
OMURA = '@omura'
RETUSA = '@retusa'
OXYNOE = '@oxynoe'
CYERCE = '@cyerce'
AEGIRES = '@aegires'
NAVANAX = '@navanax'
ALPHA = '@alpha'
BETA = '@beta'
GAMMA = '@gamma'
STELL = '@stell'
LOCUS = '@locus'
PRECEPT = '@precept'
VANQUISH = '@vanquish'
CONQUER = '@conquer'
MERUI = '@merui'
CLEROI = '@cleroi'
ANTHICUS = '@anthicus'
TECTA = '@tecta'
COLLARIS = '@collaris'
ELUDE = '@elude'
AVERT = '@avert'
OBVIATE = '@obviate'
QUELL = '@quell'
DISRUPT = '@disrupt'
EVOKE = '@evoke'
INCITE = '@incite'
EMANATE = '@emanate'
GRAPHITE_PRESS = '@graphite-press'
MULTI_PRESS = '@multi-press'
SILICON_SMELTER = '@silicon-smelter'
SILICON_CRUCIBLE = '@silicon-crucible'
KILN = '@kiln'
PLASTANIUM_COMPRESSOR = '@plastanium-compressor'
PHASE_WEAVER = '@phase-weaver'
SURGE_SMELTER = '@surge-smelter'
CRYOFLUID_MIXER = '@cryofluid-mixer'
PYRATITE_MIXER = '@pyratite-mixer'
BLAST_MIXER = '@blast-mixer'
MELTER = '@melter'
SEPARATOR = '@separator'
DISASSEMBLER = '@disassembler'
SPORE_PRESS = '@spore-press'
PULVERIZER = '@pulverizer'
CULTIVATOR = '@cultivator'
COAL_CENTRIFUGE = '@coal-centrifuge'
INCINERATOR = '@incinerator'
SILICON_ARC = '@silicon-arc'
ELECTROLYZER = '@electrolyzer'
ASMOSPHERE_CONCENTRATOR = '@atmosphere-concentrator'
OXIDATION_CHAMBER = '@oxidation-chamber'
ELECTRIC_HEATER = '@electric-heater'
SLAG_HEATER = '@slag-heater'
PHASE_HEATER = '@phase-heater'
HEAT_REDIRECTOR = '@heat-redirector'
SMALL_HEAT_REDIRETOR = '@small-heat-redirector'
HEAT_ROUTER = '@heat-router'
SLAG_INCINERATOR = '@slag-incinerator'
CARBINE_CRUCIBLE = '@carbine-crucible'
SURGE_CRUCIBLE = '@surge-crucible'
CYANOGEN_SYNTHESIZER = '@cyanogen-synthesizer'
PHASE_SYNTHESIZER = '@phase-synthesizer'
COPPER_WALL = '@copper-wall'
LARGE_COPPER_WALL = '@copper-wall-large'
TITANIUM_WALL = '@titanium-wall'
LARGE_TITANIUM_WALL = '@titanium-wall-large'
PLASTANIUM_WALL = '@plastanium-wall'
LARGE_PLASTANIUM_WALL = '@plastanium-wall-large'
THORIUM_WALL = '@thorium-wall'
LARGE_THORIUM_WALL = '@thorium-wall-large'
PHASE_WALL = '@phase-wall'
LARGE_PHASE_WALL = '@phase-wall-large'
SURGE_WALL = '@surge-wall'
LARGE_SURGE_WALL = '@surge-wall-large'
DOOR = '@door'
LARGE_DOOR = '@door-large'
SCRAP_WALL = '@scrap-wall'
LARGE_SCRAP_WALL = '@scrap-wall-large'
HUGE_SCRAP_WALL = '@scrap-wall-huge'
GIGANTIC_SCRAP_WALL = '@scrap-wall-gigantic'
THRUSTER = '@thruster'
BERYLLIUM_WALL = '@beryllium-wall'
LARGE_BERYLLIUM_WALL = '@beryllium-wall-large'
TUNGSTEN_WALL = '@tungsten-wall'
LARGE_TUNGSTEN_WALL = '@tungsten-wall-large'
BLAST_DOOR = '@blast-door'
REINFORCED_SURGE_WALL = '@reinforced-surge-wall'
REINFORCED_SURGE_WALL_LARGE = '@reinforced-surge-wall-large'
CARBINE_WALL = '@carbine-wall'
LARGE_CARIBNE_WALL = '@carbine-wall-large'
SHIELDED_WALL = '@shielded-wall'
MENDER = '@mender'
MEND_PROJECTOR = '@mend-projector'
OVERDRIVE_PROJECTOR = '@overdrive-projector'
OVERDRIVE_DOME = '@overdrive-dome'
FORCE_PROJECTOR = '@force-projector'
SHOCK_MINE = '@shock-mine'
BUILD_TOWER = '@build-tower'
REGEN_PROJECTOR = '@regen-projector'
SHOCKWAVE_TOWER = '@shockwave-tower'
CONVEYOR = '@conveyor'
TITANIUM_CONVEYOR = '@titanium-conveyor'
PLASTANIUM_CONVEYOR = '@plastanium-conveyor'
ARMORED_CONVEYOR = '@armored-conveyor'
JUNCTION = '@junction'
BRIDGE_CONVEYOR = '@bridge-conveyor'
PHASE_CONVEYOR = '@phase-conveyor'
SORTER = '@sorter'
INVERTED_SORTER = '@inverted-sorter'
ROUTER = '@router'
DISTRIBUTOR = '@distributor'
OVERFLOW_GATE = '@overflow-gate'
UNDERFLOW_GATE = '@underflow-gate'
MASS_DRIVER = '@mass-driver'
DUCT = '@duct'
ARMORED_DUCT = '@armored-duct'
DUCT_ROUTER = '@duct-router'
OVERFLOW_DUCT = '@overflow-duct'
UNDERFLOW_DUCT = '@underflow-duct'
DUCT_BRIDGE = '@duct-bridge'
DUCT_UNLOADER = '@duct-unloader'
SURGE_CONVEYOR = '@surge-conveyor'
SURGE_ROUTER = '@surge-router'
UNIT_CARGO_LOADER = '@unit-cargo-loader'
UNIT_CARGO_UNLOAD_POINT = '@unit-cargo-unload-point'


# Miscs
align = [
    'center',
    'top',
    'bottom',
    'left',
    'right',
    'topLeft',
    'topRight',
    'bottomLeft',
    'bottomRight'
]
CENTER = 'center'
TOP = 'top'
BOTTOM = 'bottom'
LEFT = 'left'
RIGHT = 'right'
TOP_LEFT = 'topLeft'
TOP_RIGHT = 'topRight'
BOTTOM_LEFT = 'bottomLeft'
BOTTOM_RIGHT = 'bottomRight'
target = [
    'any',
    'enemy',
    'ally',
    'player',
    'attacker',
    'flying',
    'boss',
    'ground'
]
ANY = 'any'
ENEMY = 'enemy'
ALLY = 'ally'
PLAYER = 'player'
ATTACKER = 'attacker'
FLYING = 'flying'
BOSS = 'boss'
GROUND = 'ground'
sort = [
    'distance',
    'health',
    'shield',
    'armor',
    'maxHealth'
]
DISTANCE = 'distance'
HEALTH = 'health'
SHIELD = 'shield'
ARMOR = 'armor'
MAX_HEALTH = 'maxHealth'
lookup_type = [
    'block',
    'unit',
    'item',
    'liquid'
    'team'
]
BLOCK = 'block'
UNIT = 'unit'
ITEM = 'item'
LIQUID = 'liquid'
TEAM = 'team'
find = [
    'ore',
    'building',
    'spawn',
    'damaged'
]
ORE = 'ore'
"Ore deposit."
BUILDING = 'building'
"Building in a specific group."
SPAWN = 'spawn'
"Enemy spawn point. Maybe a core or a position."
DAMAGED = 'damaged'
"Damaged ally building."
ControlType = [
    'idle',
    'stop',
    'move',
    'approach',
    'pathfind',
    'autoPathfind',
    'boost',
    'target',
    'targetp',
    'itemDrop',
    'itemTake',
    'payDrop',
    'payTake',
    'payEnter',
    'mine',
    'flag',
    'build',
    'getBlock',
    'within',
    'unbind'
]
IDLE = 'idle'
STOP = 'stop'
MOVE = 'move'
APPROACH = 'approach'
PATHFIND = 'pathfind'
AUTOPATHFIND = 'autoPathfind'
BOOST = 'boost'
TARGET = 'target'
TARGETP = 'targetp'
ITEMDROP = 'itemDrop'
ITEMTAKE = 'itemTake'
PAYDROP = 'payDrop'
PAYTAKE = 'payTake'
PAYENTER = 'payEnter'
MINE = 'mine'
FLAG = 'flag'
BUILD = 'build'
GETBLOCK = 'getBlock'
WITHIN = 'within'
UNBIND = 'unbind'
