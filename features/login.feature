Feature: SauceDemo Login Tests

 Feature: SauceDemo Login Tests

  Scenario Outline: Verify different user login behaviors
    Given I navigate to "https://www.saucedemo.com"
    When I enter "<user>" into the username field
    And I enter "secret_sauce" into the password field
    And I click the login button
    Then I should be on the "<expected_page>" page

    Examples:
      | user                    | expected_page |
      | standard_user           | inventory     |
      | problem_user            | inventory     |
      | performance_glitch_user | inventory     |