# Data Model

## Main Entities
- TrainingEvent
- Skill/Technology
- Booking
- User

## Secondary Entities
- Competency
- Prerequisite

## Entity Detail
### User
| Property | Type| details |
|---|---|---|
|id|string|uniqueId never sent to the front end
|email|string|unique and used for login
|password|hash|
|Competencies|List\<Competency\>|list of self-identified capabilities
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
|prerequisites|List<Competency>|
|outcomes|List<Competency>|
|attendees|List<User>|

## Booking
| Property | Type|details |
|---|---|---|
|trainingEvent|TrainingEvent|FK: trainingEvent.id|
|user|User|FT: user.id

### Competency
| Property | Type|details |
|---|---|---|
|skill|Skill|FK: skill.id|
|level|enum (number)| skill level, say from 1 to 5
|user|User|FK: user.id

### Prerequisite
| Property | Type|details |
|---|---|---|
|skill|Skill|FK: skill.id|
|level|enum (number)| skill level, say from 1 to 5
|trainingEvent|TrainingEvent|FK: trainingEvent.id