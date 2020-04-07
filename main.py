print("Welcome to the World of the One Slime. You're walking through the forest when you stumble upon a weak slime. It's nothing special, hardly even has the capacity to recognize you're existance. You are unarmed and unarmored, but decide to attack anyways. Before we engage, we need to know how strong you are.")

def getAttribute(Attribute,PointsAllowed):
    isset = False
    while(not isset):
        AttributeValue = int(input("Choose your starting "+Attribute+"\n"))
        if (AttributeValue) <= PointsAllowed:
            isset = True
    return AttributeValue


Strength = getAttribute("Strength",10)

Intelligence = getAttribute("Intelligence",10-Strength)

Agility = getAttribute("Agility",10-Strength-Intelligence)

PlayerHealth = 10

#   RAW DAMAGE VALUE

WeapPhysMod = 0
WeapMagicMod = 0

PhysicalDamage = Strength + WeapPhysMod

MagicDamage = Intelligence + WeapMagicMod



#   RAW DEFENCE VALUE UNUSED

PhysHeadDefMod = 0
PhysChestDefMod = 0
PhysArmDefMod = 0
PhysHandDefMod = 0
PhysLegDefMod = 0
PhysFootDefMod = 0
PhysShieldDefMod = 0

PlayerPhysDefence = PhysHeadDefMod+PhysChestDefMod+PhysArmDefMod+PhysHandDefMod+PhysLegDefMod+PhysFootDefMod+PhysShieldDefMod

MagHeadDefMod = 0
MagChestDefMod = 0
MagArmDefMod = 0
MagHandDefMod = 0
MagLegDefMod = 0
MagFootDefMod = 0
MagShieldDefMod = 0

PlayerMagDefence = MagHeadDefMod+MagChestDefMod+MagArmDefMod+MagHandDefMod+MagLegDefMod+MagFootDefMod+MagShieldDefMod


#   ENEMY RAW DEFENCE VALUE UNUSED

EnemyPhysDefence = 0
EnemyMagDefence = 0



#   ENEMY STATISTIC VALUES


#       SLIME STATS

SlimeHealth = 5
SlimeMaxHealth = 5
SlimePhysDefence = 2
SlimeMagDefence = 0
SlimePhysDamage = 2
SlimeMagDamage = 0


#   DAMAGE DEALT VALUE

# Run Slime Encounter

def checkHealth(health):
    if health > 0:
        return True
    else:
        return False

def updateHealth(EntityHealth,EntityPhysDamage,EntityPhysDefense,EntityType):
    DamageDealt = EntityPhysDamage - EntityPhysDefense
    newhealth = EntityHealth - DamageDealt
    print("{2} Health :{0:10} ~~  New {2:10} Health {1:10}".format(EntityHealth,newhealth,EntityType))
    return newhealth

def combatEncounter(Enemy):
    global SlimeHealth
    global PlayerHealth
    print("You Encounter a "+Enemy+"")
    while(checkHealth(PlayerHealth) and checkHealth(SlimeHealth)):
#        print("The Slime has "+str(SlimeHealth)+" hp out of "+str(SlimeMaxHealth)+" hp.")
  #      PlayerDamageDealt = PhysicalDamage - SlimePhysDefence
 #       print("You deal "+str(PlayerDamageDealt)+" damage to the enemy!")
        SlimeHealth = updateHealth(SlimeHealth,PhysicalDamage,SlimePhysDefence,"Slime")
        if SlimeHealth <= 0:
            print("You killed the Slime!")
        else:


    #        EnemyDamageDealt = SlimePhysDamage - PlayerPhysDefence
    #       print("The Slime attacks you back for "+str(EnemyDamageDealt)+"")
    #      PlayerHealth = PlayerHealth - EnemyDamageDealt
    #     print("You have "+str(PlayerHealth)+" health left!")
            PlayerHealth = updateHealth(PlayerHealth,SlimePhysDamage,PlayerPhysDefence,"Player")
            if PlayerHealth <= 0:
                print("You died, loser!")
    
             
combatEncounter("Slime")

#    print("The Slime has "+str(SlimeHealth)+" hp out of "+str(SlimeMaxHealth)+" hp.")
 #   PlayerDamageDealt = PhysicalDamage - SlimePhysDefence
  #  print("You deal "+str(PlayerDamageDealt)+" damage to the enemy!")
   # SlimeHealth = SlimeHealth - PlayerDamageDealt   
   # return health+modifier
#blahblah = updateHealth(PlayerHealth,SlimePhysDamage,PlayerPhysDefence,"Slime")
#print(blahblah)

print("Success")