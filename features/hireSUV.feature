Feature: Hire SUV
  Scenario Outline: Hire budget SUV with five seats for one week trip
    Given user is on budget application home page
	When user types "<location search keyword>" and selects pickup and return location as "<location>"
	And pickup date as week ahead of current date
	And return date as week ahead of pickup date
	And clicks Select My car option to navigate to reservations page
	And chooses lowest price SUV with "<X>" doors and "<Y>" seats and click pay now option
	Then user validates base rate, fees and taxes and estimated prepaid total succesfully
    Examples:
      |location search keyword|location|X|Y|
      |aus|Austin Bergstrom Intl Airport|4|5|