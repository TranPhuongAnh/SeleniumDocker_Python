# Author: Phuong Anh
# Date: 24/04/2025
# Description: Demo open Docker

@smoke
Feature: Demo open Docker

  @screenshot
  Scenario: Screenshot Search Result
    Given Create driver
    When Open web browser
    Then Check title page
    When Search data in website
    Then Take screenshot search result
    Then Screenshot: Close browser

  @example_local
  Scenario: Open website
    Given Create driver for local test
    When Open browser and url
    Then Check tile page
    Then Local: Close browser

  @search
  Scenario: Search on google
    Given Create a new browser instance
    And I navigate to Google
    When I search for "{search_query}"
    Then I should see the search results
    Then Search: Close Browser