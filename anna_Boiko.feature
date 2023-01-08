# Created by anyut at 1/8/2023
Feature: Testing EPAM website


  Scenario: epam_is_loaded
    Given browser is opened and new page created
    When go to "https://www.epam.com/"
    Then "https://www.epam.com/" will be opened in new page

  Scenario: page_reload
    Given "https://www.epam.com/" is opened
    When press F5 key
    Then "https://www.epam.com/" will be reloaded

  Scenario Outline: tab_clicked
    Given "https://www.epam.com/" is opened
    When clicked on <tab>
    Then "https://www.epam.com/<tab>" will be loaded
    Examples:
    |    tab     |
    |  SERVICES  |
    |HOW WE DO IT|
    |  OUR WORK  |
    |  INSIGHTS  |
    |   ABOUT    |
    |  CAREERS   |

  Scenario: contact_button_pressed
    Given "https://www.epam.com/" is opened
    When press "CONTACT US" button
    Then page "https://www.epam.com/about/who-we-are/contact" will be loaded

  Scenario Outline: page_not_found
    Given "https://www.epam.com/" is opened
    When add to url non-existent <subdomain>
    Then page "Error 404" will be loaded
    Examples:
    |subdomain|
    |sjdlkjhfj|
    |test1    |
    |localhost|

  Scenario Outline: language_changed
    Given "https://www.epam.com/" is opened
    When press "Global (EN)" button
    And select <language>
    Then page in <language> will be loaded
    Examples:
    |language|
    |Hungary (English)|
    |Polska (Polski)  |
    |Україна (Українська)|

  Scenario: change_scaling
    Given "https://www.epam.com/" is opened
    When reduce browser scale
    Then site scale will be reduced

  Scenario: fullscreen
    Given "https://www.epam.com/" is opened
    When press F11 key
    Then site will be opened in fullscreen