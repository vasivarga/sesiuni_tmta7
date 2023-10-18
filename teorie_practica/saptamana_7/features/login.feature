Feature: Test login functionality

  Background:
    Given I am on login page

  Scenario: Test valid login
    When I send a valid username
    And I send a valid password
    And I click on Login button
    Then A success message will be displayed on the screen

  Scenario Outline: Test invalid username/password
    When I use an invalid "<username>" or "<password>"
    And I click on Login button
    Then An error message will be displayed on the screen
    Examples:
      | username  | password             |
      | tomsmith | invalid              |
      | invalid   | SuperSecretPassword! |
      | invalid   | invalid              |


