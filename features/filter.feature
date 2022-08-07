Feature: Content view using filtration
  Scenario: Click on watchlist button and return back
    Given website is open and all movies parameter set
    When we click on watchlist button
    Then count films on clicked filter parameter and count all films
    And return on all movies view

  Scenario: Click on history button and return back
    Given website is open and all movies parameter set
    When we click on history button
    Then count films on clicked filter parameter and count all films
    And return on all movies view

  Scenario: Click on favorites button and return back
    Given website is open and all movies parameter set
    When we click on favorites button
    Then count films on clicked filter parameter and count all films
    And return on all movies view