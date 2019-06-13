#include <iostream>
#include "../include/BankSystem/Account.hpp"

int main(int argc, char const *argv[])
{
    Account *a = new Account();
    
	if(a->verification()==-1)
    {
		std::cout << a->getAccountNum() << "\n";
    	std::cout << a->getHolderName() << "\n";
    	std::cout << "The current balance is " << a->getBalance() << ".\n";
	}
	else
	{
		std::cout<<"Wrong Password";
	}
	
	a->deposit(1000.0);
    a->withdraw(200.0);
    a->withdraw(2000.0);
    a->displayBalance();
    delete (a);
    return 0;
}
