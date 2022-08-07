Feature: Content view using sorting
  Scenario: Sorting by date
    Given website is open, all movies parameter set, sort is default
    When we click on sort by date
    Then compare all films and check this release date
