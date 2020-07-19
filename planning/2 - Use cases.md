# Use cases

Without authentication:

1. User can create a poll

1. User can edit his polls

1. User can see the results of his polls

1. User can vote on poll

1. User can change his vote

1. User can share his poll

1. User can create a account

With authentication:

1. User can log in

1. User keeps his polls and votes after registration/login

## Guest Mode

When an user isn't logged in and creates or answer a poll, a new User is created in the database flagged as guest.
Then a authentication Token is generated and sended to the frontend.
This token is identical to the Token of a non-guest user, and will be kept in the Local Storage.
In the frontend, the guest user has access to the register/login page.
When he does one or the other, all of the polls and answers from the guest user are transfered to the non-guest user.
