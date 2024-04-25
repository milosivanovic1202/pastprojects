#include <cs50.h>
#include <stdio.h>

void card_validation(long n);
long power_f(int base, int exponent);
int num_length(long n);

int main(void)
{
    long n = get_long("Please enter your credit card number? \n");

    // run validation
    card_validation(n);
}

void card_validation(long n)
{
    int l = num_length(n);
    if (l == 13 || l == 15 || l == 16)
    {
        long sum = 0;
        for (int i = 2; i < l + 1; i += 2)
        {
            long mult_dig = ((n % power_f(10, i)) - (n % power_f(10, i - 1))) / power_f(10, i - 1) * 2;
            sum += mult_dig % 10 + ((mult_dig % 100 - mult_dig % 10) / 10);
        }

        for (int i = 1; i < l + 1; i += 2)
        {
            sum += ((n % power_f(10, i)) - (n % power_f(10, i - 1))) / power_f(10, i - 1);
            printf("%ld\n", sum);
        }

        if (sum % 10 != 0)
        {
            printf("INVALID\n");
        }
        else
        {
            int card_id =
                (n / power_f(10, l - 1) * 10) + ((n % power_f(10, l - 1) - (n % power_f(10, l - 2))) / power_f(10, l - 2));
            {
                if (l == 15 && (card_id == 34 || card_id == 37))
                {
                    printf("AMEX\n");
                }
                else if ((l == 13 || l == 16) && (card_id / 10) == 4)
                {
                    printf("VISA\n");
                }
                else if (l == 16 && (card_id == 51 || card_id == 52 || card_id == 53 || card_id == 54 || card_id == 55))
                {
                    printf("MASTERCARD\n");
                }
                else
                {
                    printf("INVALID\n");
                }
            }
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int num_length(long n)
{
    if (n == 0)
        return 1;
    int count = 0;
    while (n != 0)
    {
        n = n / 10;
        ++count;
    }
    return count;
}

long power_f(int base, int exponent)
{
    long pow = 1;
    for (int i = 1; i < exponent + 1; i++)
    {
        pow = pow * base;
    }
    return pow;
}