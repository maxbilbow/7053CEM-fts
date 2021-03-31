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

### F2 - Daily Emails
```gherkin

```

### F3 - Training Recommendation
```gherkin

```