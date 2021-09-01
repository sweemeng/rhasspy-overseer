# Just a simple service for rhasspy

This work by listening to rhasspy via mqtt. Username password currently hardcoded and removed temporarily. 

Each intent received will be checked, if matched, then it will call certain function. Otherwise there is a fallback that says intent not found. 

A mqtt service will be called when an intent is processed to say something when done. 

Mostly a hack, let see how far it goes
