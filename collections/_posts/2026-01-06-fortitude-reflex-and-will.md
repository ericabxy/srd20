---
layout: post
title: Fortitude, Reflex, and Will
date: 2026-01-06 18:00:00 -0800
published: false
---

Saving throws follow a simple progression pattern that gets very complex when multi-classing comes into play. For something as simple as a number that can be defined as "Good" or "Poor" or somewhere in-between, the fine-grained bonus resulting from multiple class tables added together doesn't add much of value to the game. I propose that any character's save bonuses should be easily calculable at any given time---instead of totaling up bonuses from different tables---with edge cases requiring multiple table lookup replaced by a single penalty for mixing classes.

Instead of combining tables, each _character_ is treated as having one or more "good" saving throws, calculated by character level. The remaining saves are treated as "poor" except in special cases.

__Primary Saves:__ Each character's highest-level class (or "primary class") grants the character good saving throws based on its class table, e.g. a 4th-level fighter / 2nd-level rogue has a good Fortitude save.

__Secondary Saves:__ Each character's lower-level classes may also grant good saving throws as long as they are within ONE level of the primary class, e.g. a 5th-level fighter / 4th-level wizard has both a good Fortitude save and a good Will save.

__Inferior Saves:__ Classes that don't meet the above criteria grant a flat +2 save bonus for every good saving throw in the class tables, provided that save is not already considered good due to a higher class, e.g. a 6th-level wizard / 5th-level barbarian / 1st-level rogue has good Fortitude and Will saves, but a poor Reflex save with a temporary +2 bonus (until the rogue class reaches 5th level and grants a good save instead).

As a short rule-of-thumb, a multiclass character has good saving throws matching their highest-level class and any classes within one level of that class, with no overlap. All other saving throws are treated as poor, but any lower-level classes grant a temporary +2 save bonus to any saving throws not already considered good.

### Example: Multiclass Monk

A 5th-level monk has good Fortitude, Reflex, and Will saving throws (+4 each for a 5th-level character). If she takes levels in ranger, those saving throws will remain the same until her ranger levels reach 7th level or higher. At that point she'll have good Fortitude and Reflex saving throws (+8 each for a 12th-level character), and her Will save will become poor (+4) except her lapsing monk training will still add a +2 save bonus to Will saves (+6 total). Since she cannot gain any more monk levels, she would have to take levels in e.g. wizard to restore her good Will save as a 7th-level ranger / 6th-level wizard / 5th-level monk.
