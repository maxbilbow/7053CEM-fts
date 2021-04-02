# Functional Requirements

## User Stories

### F1 - Apply for Training Events

```gherkin
Feature: F1: Apply for training events

  Scenario: F1.1 Browse available events
    Given that I am logged in
     When I click "Available Events"
     Then events that took place over a week ago are hidden
      And I am can see a list of all available training events
  
  Scenario: F1.2 View event detail
    Given that can see an event list
     When I click on an event
     Then then an event detail view is opened
      And I can see a brief synopsis
      And I can see other informatin about the course
  
  Scenario: F1.3 Apply to Join
    Given that I am viewing an event detail view
      And I select "Join and Event"
     Then I am presented with a list of available start times
  
  Scenario: F1.4 Event starting in < 24 hours
    Given that I have clicked "Joint an Event" 
      And some start times are in less than 24 hours
     Then those start times are marked unavailable
      And I cannot click on them
  
  Scenario: F1.5 Joining an event
    Given that I have clicked "Joint an Event" 
      And the start time I want is more than 24 hours in the future
     When I click on the start time
     Then I am enrolled on in the training event
      And an email with 
  

```

### F2 - Training Recommendation
```gherkin
Feature: F2 - Course Recommendation

  Scenario: F2.1 - Update Profile
    Given that I am logged in
     When I view my profile
     Then I can add and remove interests
      And I can add and remove skills
      And I can save my profile
  
  Scenario: F2.2 - Recommended Events based on profile
    Given that I have specified skills and interests in my profile
      And I am vieing the event list
     When I select "show recommended"
     Then I am presented with events that best fit my profile first
  
  Scenario: F2.3 - Recommended Events based on history
    Given that I have registered for certain events
      And I am vieing the event list
     When I select "show recommended"
     Then I am presented with events that are similar to my event history
  
  Scenario: F2.4 - Recommended Events based on similar profiles
    Given that I have registered for certain events
      And that I have specified skills and interests in my profile
     When I am view the event list
      And I select "show recommended"
     Then I am presented with events that relate to the history and interests of users with similar profiles
  

```

### F2 - Daily Emails (Stretch)
```gherkin
Feature: F3 - Training Emails

  Scenario: F3.1 Daily Emails
    Given that am an event manager
     When new attendees enroll for my events
     Then I will receive a daily email sumamry
```

# Non-functional Requirements

The application should be:
* easy to expand
* easily hosted on distributed systems
* react quickly