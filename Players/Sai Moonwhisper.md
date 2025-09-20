---
level: 3
proficiency_bonus: 2
---
```stats
items:
  - label: Level
    value: "{{ frontmatter.level }}"
  - label: Proficiency
    value: "{{ frontmatter.proficiency_bonus }}"
  - label: AC
    value: "{{ add 13 (modifier abilities.dexterity) }}"
  - label: Passive Perception
    value: "{{ add 10 (modifier abilities.wisdom) frontmatter.proficiency_bonus }}"
  - label: Initiative
    value: "+{{ modifier abilities.dexterity }}"
  - label: Spell Attack Mod
    value: "+{{ add frontmatter.proficiency_bonus (modifier abilities.wisdom) }}"
  - label: Spell Save DC
    value: "{{ add 8 frontmatter.proficiency_bonus (modifier abilities.wisdom) }}"
  - label: Bonds
    value: Determination
  - label: Flaws
    value: Control
  - label: Spells Prepared
    sublabel: Bless, Cure Wounds, Lesser Restoration, Spiritual Weapon
    value: "{{ add (modifier abilities.wisdom) frontmatter.level}}"
```


Race: Elf
Class: Cleric

```event-btns
items:
  - name: Short Rest
    value: short-rest
  - name: Long Rest
    value: long-rest
```

```healthpoints
state_key: sai_moonwhisper_hp
health: 19
hitdice:
  dice: d8
  value: 3
```

```ability
abilities:
  strength: 14
  dexterity: 12
  constitution: 13
  intelligence: 13
  wisdom: 15
  charisma: 8

proficiencies:
  - wisdom
  - charisma   
```

```skills
proficiencies:
  - athletics
  - insight
  - medicine
  - survival
```

```consumable
items:
  - label: "Level 1 Spells"
    state_key: sai_moonwhisper_spells_1
    uses: 4
    reset_on: "long-rest"
  - label: "Level 2 Spells"
    state_key: sai_moonwhisper_spells_2
    uses: 2
    reset_on: "long-rest"
  - label: "Channel Divinity"
    state_key: sai_moonwhisper_channel_divinity
	uses: 1
    reset_on: "long-rest"
```


## Weapons

```stats
items:
  - label: Mace
    sublabel: 1d6
    value: +4
  - label: Crossbow
    sublabel: 1d8
    value: +4
grid:
  columns: 2
```

## Equipment

- Priest pack
- Shield
- Holy Symbol
- Wolfszahn

## Notes

### Disciple of Life

Also starting at 1st level, your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level.

###  Channel Divinity: Turn Undead

Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

### Channel Divinity: Preserve Life

Starting at 2nd level, you can use your Channel Divinity to heal the badly injured.

As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct.