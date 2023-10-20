Feature: Register Page

  Background: I am on the Register Page
    Given I am on the Register Page

    @smoke
    Scenario:
      When I click on the register button
      Then First name error is displayed
      And Last name error is displayed
      And Email error is displayed
      And Password error is displayed
      And Confirm password error is displayed