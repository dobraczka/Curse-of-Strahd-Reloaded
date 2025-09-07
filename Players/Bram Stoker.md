---
level: 3
proficiency_bonus: 2
ac: "13"
initiative modifier: "+2"
max hit points: "19"
---
```stats
items:
  - label: Level
    value: "{{ frontmatter.level }}"
  - label: Proficiency
    value: "{{ frontmatter.proficiency_bonus }}"
  - label: AC
    value: "{{ add 11 (modifier abilities.dexterity) }}"
  - label: Passive Perception
    value: "{{ add 10 (modifier abilities.wisdom) frontmatter.proficiency_bonus }}"
  - label: Initiative
    value: "+{{ modifier abilities.dexterity }}"
  - label: Spell Attack Mod
    value: "+{{ add frontmatter.proficiency_bonus (modifier abilities.charisma) }}"
  - label: Spell Save DC
    value: "{{ add 8 frontmatter.proficiency_bonus (modifier abilities.charisma) }}"
```


Race: Halbelf
Class: Bard

```event-btns
items:
  - name: Short Rest
    value: short-rest
  - name: Long Rest
    value: long-rest
```

```healthpoints
state_key: bram_stoker_hp
health: 19
hitdice:
  dice: d8
  value: 3
```

```ability
abilities:
  strength: 10
  dexterity: 15
  constitution: 12
  intelligence: 11
  wisdom: 12
  charisma: 17

proficiencies:
  - dexterity
  - charisma   
```

```skills
proficiencies:
  - acrobatics
  - deception
  - insight
  - performance
  - persuasion

half_proficiencies:
  - animal handling
  - arcana
  - athletics
  - history
  - investigation
  - medicine
  - nature
  - perception
  - religion
  - sleight of hand
  - stealth
  - survival 
  - intimidation
  
expertise:
  - Insight
  - Persuasion
```

```consumable
items:
  - label: "Level 1 Spells"
    state_key: bram_stoker_spells_1
    uses: 4
    reset_on: "long-rest"
  - label: "Level 2 Spells"
    state_key: bram_stoker_spells_2
    uses: 2
    reset_on: "long-rest"
  - label: "Bardic Inspiration"
    state_key: bram_stoker_bardic_inspo
    uses: 3
    reset_on: "long-rest"
```

## Weapons

```stats
items:
  - label: Dagger
    sublabel: 1d4
    value: +2
  - label: Crossbow
    sublabel: 1d8
    value: +4
grid:
  columns: 2
```

## Equipment
- Entertainer Pack
- Laute
- Disguise Pack
- Bernsteinanhänger

## Notes
### Song of Rest

Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.

The extra Hit Points increase when you reach certain levels in this class: to 1d8 at 9th level, to 1d10 at 13th level, and to 1d12 at 17th level.