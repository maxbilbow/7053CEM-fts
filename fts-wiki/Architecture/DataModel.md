# Data Model

![](../_attachments/entity-rel.png)

## Main Entities
- TrainingEvent
- Skill/Technology
- Booking
- User

## Entity Detail
### User
| Property | Type| details |
|---|---|---|
|id|string|uniqueId never sent to the front end
|email|string|unique and used for login
|password|hash|
|Competencies|List\<Skill\>|list of self-identified capabilities
|Interests|List\<Skill\>|

### Skill (Skill/Technology)
| Property | Type|details |
|---|---|---|
|id|string (unique skill id)|PK
|displayName|string|
|aliases|List<string>|List of additional search terms relating to this skill/technology

### Skill Alias
| Property | Type|details |
|---|---|---|
|id|string| PK
|alias|string|
|skill|Skill|FK: skill.id

### Training Event
| Property | Type|details |
|---|---|---|
|id|string|PK
|trainingManager|User| FK: user.id
|startTime|long|
|title|string|
|synopsis|string|
|prerequisites|List<Skill>|
|outcomes|List<Skill>|
|attendees|List<User>|

## Booking
| Property | Type|details |
|---|---|---|
|trainingEvent|TrainingEvent|FK: trainingEvent.id|
|user|User|FT: user.id
