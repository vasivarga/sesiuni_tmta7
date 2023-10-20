Feature: Login Page

  Background:
    Given I am on the Login Page

  @A @smoke @regression
  Scenario: Log in with unregistered email
    When I enter an unregistered email
    And I click on the login button
    Then I should see "No customer account found" main error message

  @B @smoke
  Scenario: Log in without credentials
    When I click on the login button
    Then I should see "Please enter your email" email error message


  @regression
  Scenario: Log in with invalid email format
    When I enter "tmta7_address" as email
    And I click on the login button
    Then I should see "Wrong email" email error message

  @A, @smoke
  Scenario: Check that the URL is correct
    Then The URL of the page is "https://demo.nopcommerce.com/login"



