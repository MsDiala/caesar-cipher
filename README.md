[]Create an encrypt function that takes in a plain text phrase and a numeric shift.
[]the phrase will then be shifted that many letters.
E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘acb’, 10) would return ‘klm’
[]shifts that exceed 26 should wrap around
E.g. encrypt(‘abc’,27) would return ‘bcd’
[]Create a decrypt method that takes in encrypted text and numeric shift which will restore the encrypted text back to [][]its original form as long as correct key is supplied.
[]Break the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
[]Devise a method for the computer to determine if code was broken with minimal human guidance.