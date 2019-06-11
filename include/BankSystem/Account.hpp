#include <string>

class Account
{
private:
    std::string holderName;
    std::string accountNum;
    double balance;
public:
    Account(); //Constructor for initializing values
    ~Account(); //Destructor to free memory when required
    std::string getHolderName();
    std::string getAccountNum();
    double getBalance();
    void displayBalance();
    void withdraw(double sum); //Withdraw a certain amount from the balance
    void deposit(double sum); //Deposit a certain amount to the balance
};