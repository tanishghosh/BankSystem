#include <string>

class Account
{
private:
    std::string holderName;
    std::string accountNum;
    std::string password;
    double balance;
public:
    Account(); //Constructor for initializing values
    ~Account(); //Destructor to free memory when required
    std::string getHolderName();
    std::string getAccountNum();
    void getPassword();            //Function to set password 
    int verification();            //Function to be used while login for verification purposes.
    double getBalance();
    void displayBalance();
    void withdraw(double sum); //Withdraw a certain amount from the balance
    void deposit(double sum); //Deposit a certain amount to the balance
};
