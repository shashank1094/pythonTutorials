print("DIR() CALLED IN", __file__, "BEFORE IMPORT", dir(),  "\nPACKAGE::", __package__ )
import maindir

print("DIR() CALLED IN", __file__, "AFTER IMPORT", dir())
print("DIR(maindir)", dir(maindir), "\nFILE::", maindir.__file__, "\nPACKAGE::", maindir.__package__)
