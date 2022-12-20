Feature: Content view of current film card on the website
  Scenario: Click on first film poster
    Given film_card.website is open
    When we click on film poster of film with number 1
    Then film card is visible
    And we close it

  Scenario: Click on first film title
    Given film_card.website is open
    When we click on film title of film with number 1
    Then film card is visible
    And we close it

  Scenario: Click on first film comment count
    Given film_card.website is open
    When we click on film comments of film with number 1
    Then film card is visible
    And we close it

#  Scenario: Click on first film rating
#    Given film_card.website is open
#    When we click on film rating of film with number 1
#    Then film card is invisible
#    And we close it

#  Scenario: Click on first film release date
#    Given film_card.website is open
#    When we click on film date of film with number 1
#    Then film card is invisible
#    And we close it
#
#  Scenario: Click on first film duration
#    Given film_card.website is open
#    When we click on film duration of film with number 1
#    Then film card is invisible
#    And we close it
#
#  Scenario: Click on first film genre
#    Given film_card.website is open
#    When we click on film genre of film with number 1
#    Then film card is invisible
#    And we close it