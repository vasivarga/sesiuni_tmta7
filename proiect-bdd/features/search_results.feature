Feature: Search Results Page

  Background:
    Given I am on the home page

  @X
  Scenario Outline: Verify that search results return at least "<number>" results
    When I type "<product_name>" in the search box
    And I click on the search button
    Then I should see at least "<number>" results
    Examples:
    |product_name| number |
    |laptop      |2  |
    |phone       |3  |
    |shirt       |3  |
    |wefrwersr   |0  |
