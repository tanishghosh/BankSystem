#include <iostream>
#include<cstring>
#include "../include/BankSystem/Account.hpp"

Account::Account() //Constructor for initializing values
{
    this->holderName = "John Doe";
    this->accountNum = "123456789";
    this->balance = 0;
    this->password = "abcd";
}

Account::~Account() //Destructor to free memory when required
{
}

std::string Account::getHolderName()
{
    return (this->holderName);
}

std::string Account::getAccountNum()
{
    return (this->accountNum);
}


void Account::getPassword()                                             //Function to get password of account holder.
{
	std::string temp,temp1;                                             //Declaration of two temporary passwords.
	std::cout<<"Set password:";                                         
	std::cin>>temp;
	std::cout<<"\nConfirm password again:";
	std::cin>>temp1;
	if(temp.compare(temp1)==0)	                                       //Comparison of two passwords for confirmation purposes.
		{
			std::cout<<"\nPassword successfully";
			this->password=temp;                                       //On confirmation, password is set.
		}
	else
		{
			std::cout<<"\nPasswords donot match.Try again";            //While loop can be done here until a password is set successfully.
		}
}

int Account::verification()
{
	std::string pass;
	std::cout<<"Enter password:";                               
	std::cin>>pass;
	
	if(pass.compare(this->password)==0)                                //Comparison of entered password with earlier set password.
		return -1;                                                     //According to result of comparison, an integer value is returned.
	else
		return 0;
}


void Account::displayBalance()
{
    std::cout << "The current balance is " << this->balance << ".\n";
}

double Account::getBalance()
{
    return (this->balance);
}

void Account::withdraw(double sum) //Withdraw a certain amount from the balance
{
    if (this->balance - sum > 0)
    {
        this->balance -= sum;
        std::cout << sum << " withdrawn from the account.\n";
        this->displayBalance();
    }
    else
    {
        std::cout << "Insufficient balance in the account!\n";
    }
}

void Account::deposit(double sum) //Deposit a certain amount to the balance
{
    this->balance += sum;
    std::cout << sum << " deposited to the account.\n";
    this->displayBalance();
}
