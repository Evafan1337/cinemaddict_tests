Feature: Content view of current film card on the website
  Scenario: Click on first film preview
    Given film_card.website is open
    When we click on film preview of film with number 1
    Then film card is opened
    And we close it

  Scenario: Click on first film title
    Given film_card.website is open
    When we click on film title of film with number 1
    Then film card is opened
    And we close it

  Scenario: Click on first film comment count
    Given film_card.website is open
    When we click on film comment count of film with number 1
    Then film card is opened
    And we close it

#  Scenario: Click on first film rating
#    Given film_card.website is open
#    When we click on film rating of film with number 1
#    Then film card is opened
#    And we close it

  Scenario: Click on first film release date
    Given film_card.website is open
    When we click on film release date of film with number 1
    Then film card is opened
    And we close it

  Scenario: Click on first film duration
    Given film_card.website is open
    When we click on film duration of film with number 1
    Then film card is opened
    And we close it

  Scenario: Click on first film genre
    Given film_card.website is open
    When we click on film genre of film with number 1
    Then film card is opened
    And we close it