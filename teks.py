class Teks:
    #============================================================================
    # Tekniks
    #============================================================================        
    def __physical(tek, attacker, defender):
        return Pokecalc.physical_damage(tek, attacker, defender)

    def __thundershock(tek, attacker, defender):
        pass

    def __growl(tek, attacker, defender):
        pass

    #============================================================================
    # Class data
    #============================================================================    
    teks = {
        'Tackle' : Teknik (
            name = 'Tackle',
            tektype = 'Normal',
            category = 'Physical',
            base_pp = 35,
            max_pp = 56,
            power = 50,
            accuracy = 100,
            func = __physical
        ),

        'Thunder Shock' : Teknik (
            name = 'Thunder Shock',
            tektype = 'Electric',
            category = 'Special',
            base_pp = 30,
            max_pp = 48,
            power = 50,
            accuracy = 100,
            func = __thundershock
        ),

        'Growl' : Teknik (
            name = 'Growl',
            tektype = 'Normal',
            category = 'Status',
            base_pp = 40,
            max_pp = 64,
            power = None,
            accuracy = 100,
            func = __growl
        )
    }

    
