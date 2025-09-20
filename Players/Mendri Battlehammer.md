---
level: 3
proficiency_bonus: 2
ac: "16"
---
```stats
items:
  - label: Level
    value: "{{ frontmatter.level }}"
  - label: Proficiency
    value: "{{ frontmatter.proficiency_bonus }}"
  - label: AC
    value: "{{ add 14 (modifier abilities.dexterity) }}"
  - label: Passive Perception
    value: "{{ add 10 (modifier abilities.wisdom) frontmatter.proficiency_bonus }}"
  - label: Initiative
    value: "+{{ modifier abilities.dexterity }}"
  - label: Spell Attack Mod
    value: "+{{ add frontmatter.proficiency_bonus (modifier abilities.wisdom) }}"
  - label: Spell Save DC
    value: "{{ add 8 frontmatter.proficiency_bonus (modifier abilities.wisdom) }}"
  - label: Bonds
    value: Nostalgia
  - label: Flaws
    value: Insecurity
```


Race: Dwarf
Class: Ranger

```event-btns
items:
  - name: Short Rest
    value: short-rest
  - name: Long Rest
    value: long-rest
```

```healthpoints
state_key: mendi_battlehammer_hp
health: 24
hitdice:
  dice: d10
  value: 3
```

```ability
abilities:
  strength: 14
  dexterity: 15
  constitution: 14
  intelligence: 10
  wisdom: 14
  charisma: 8

proficiencies:
  - strength
  - dexterity   
```

```skills
proficiencies:
  - animal handling
  - athletics
  - investigation
  - stealth
  - survival
```

```consumable
items:
  - label: "Level 1 Spells"
    state_key: mendi_battlehammer_spells_1
    uses: 3
    reset_on: "long-rest"
```

## Weapons

```stats
items:
  - label: Longbow
    sublabel: 1d8
    value: +4
  - label: Longsword
    sublabel: 1d8 (+2 dueling)
    value: +4
grid:
  columns: 2
```

## Equipment
- Wanderers Scarf

## Notes
Favored Terrain: Forrest
Enemy: Undead