#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string key);
char rotate(char c, int n);

// code name is also counted into argc!
int main(int argc, string argv[])
{
    if (argc > 2 || argc < 2)
    {
        printf("Usage: ./caesar key - too many ARGUMENTS\n");
        return 1;
    }
    else
    {
        if (only_digits(argv[1]) == false)
        {
            printf("Usage: ./caesar key - too many DIGITS\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);
    string plaintxt = get_string("Plaintext : ");

    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintxt); i < len; i++)
    {
        printf("%c", rotate(plaintxt[i], key));
    }
    printf("\n");
}

bool only_digits(string key)
{
    bool onlydigits = true;
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        if (isdigit(key[i]) == 0)
        {
            onlydigits = false;
        }
    }
    return onlydigits;
}

char rotate(char c, int n)
{
    int intc = (int) c;
    // uppercase
    if (intc > 64 && intc < 91)
    {
        return (char) (((intc - 64) + n) % 26 + 64);
    }
    // lowercase
    else if (intc > 96 && intc < 123)
    {
        return (char) (((intc - 96) + n) % 26 + 96);
    }
    // other char
    else
    {
        return c;
    }
}