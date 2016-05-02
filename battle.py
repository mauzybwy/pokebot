import time

class Battle():
    @staticmethod
    def turn(attacker, defender):
        print attacker.name + "'s turn."
        attacker.take_turn()
        while(attacker.is_busy()):
            time.sleep(.1)

        return attacker.is_leaving()


    
    def begin(self, remote_trainer, local_trainer):
        while True:
            if Battle.turn(remote_trainer, local_trainer):  break
            if Battle.turn(local_trainer,  remote_trainer): break

        print "BATTLE ENDED"
            
        print remote_trainer.name, remote_trainer.state
        print local_trainer.name,  local_trainer.state
