-- Keep a log of any SQL queries you execute as you solve the mystery.

--To see the structure of the db
.schema

-- Id like to see all the reports on crimes that happened on the 28th July 2021 on Humphrey Street

SELECT description
FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day = 28
AND street = "Humphrey Street";

-- From this we see that it happened at 10:15am at the Humphrey Street bakery.
-- Each of the witnesses mentions the bakery, so thats where we are headed next.
-- First we can have a look at the interview

SELECT transcript
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28;

-- We now know that within 10 minutes of the theft, the thief seems to have entered a car
-- in the bakery parking lot. We can look at the cars that left the parking lot in that
-- time frame.

-- The witness also saw the thief withdrawing some money earlier that morning from the AT
-- at Leggett Street, so we can query the ATM to see who took money out that particular morning.

-- Also, the thief wants to take the earliest flight the next day, so we will query the
-- tickets to see which have been sold for that time spot. They called someone for less
-- than a minute just after the theft.

-- Seems a bit suspicious that 2 bothers took the rooster all the way to Paris?

-- Now we are going after those clues one by one

-- 1st the parking lot :

SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25;

-- This shows that all licence plates have exited the premise in a 10 minute window of the theft.
-- We can match this against the licence plates in people to get the names of the drivers:

--NAMES OF POTENTIAL SUSPECTS:
SELECT name
FROM people
WHERE license_plate
IN(
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25);

-- We can further narrow our search with matching these names to the atm withdrawals
-- I have run the same query with SELECT transaction_type to see how withdrawal is entered in the db.

SELECT person_id
FROM bank_accounts
WHERE bank_accounts.account_number IN(
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street');

-- Now we can link the person id which left the bakery parking lot in the given time frame with
-- the accounts id that made a withdrawal on that morning.

SELECT name, phone_number
FROM people
WHERE people.license_plate
IN(
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25)

AND people.id IN (
SELECT person_id
FROM bank_accounts
WHERE bank_accounts.account_number IN(
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street')
);

-- I do admit this looks quite ugly, but we seem to have narrowed our potential suspects to just 4
-- ('Iman', 'Luca', 'Diana', 'Bruce').
-- This could've been done with joined tables as well I guess.
-- Now we will narrow it down even further (hopefully) by the time spent on the phone for the flight
-- agreement.

SELECT caller , receiver
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND phone_calls.caller IN(
SELECT phone_number
FROM people
WHERE people.license_plate
IN(
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25)

AND people.id IN (
SELECT person_id
FROM bank_accounts
WHERE bank_accounts.account_number IN(
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street')
));

-- This gives us the two potential suspect pairs
-- Now to narrow this down, by getting the earliest flight out of Fiftyville and matching the passenger
-- names to the 2 callers. Then we find the thief and the accomplice as well as the destination

-- Even if there are more than one airport in Fiftyville, we are looking for the earliest
-- flight out of there, so it does not matter where in Fiftyville it is.

SELECT id, destination_airport_id, hour, minute
FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
AND origin_airport_id = (
SELECT id
FROM airports
WHERE full_name LIKE '%Fiftyville%'
)
ORDER BY hour, minute;

-- We can now figure out where the earliest flies, which will be our destination

SELECT city
FROM airports
WHERE id = 4;

-- We see its the Laguarida Airport. We are now interested in matching our 2 potential thives
-- with the passenger list from flight with id 36.

SELECT name
FROM people
WHERE people.passport_number IN(

SELECT passport_number
FROM passengers
WHERE flight_id = 36
AND passengers.passport_number IN
(
SELECT passport_number
FROM people
WHERE phone_number IN(

SELECT caller
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60
AND phone_calls.caller IN(
SELECT phone_number
FROM people
WHERE people.license_plate
IN(
SELECT license_plate
FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute > 15
AND minute < 25)

AND people.id IN (
SELECT person_id
FROM bank_accounts
WHERE bank_accounts.account_number IN(
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND transaction_type = 'withdraw'
AND atm_location = 'Leggett Street')
)))));

-- GOTCHA! BRUCE it is! Now we can get his number and get the accomplice :

SELECT phone_number
FROM people
WHERE name = 'Bruce';

-- We can now get the name of the accomplice

SELECT name
FROM people
WHERE phone_number = "(375) 555-8161";

-- Robin? Seems like Batman is into ducks and thievery now :)