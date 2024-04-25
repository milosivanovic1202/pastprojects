#include <cs50.h>
#include <stdio.h>

// I made two versions for this assignment:
// 1. Utilising for-loops
// 2. Utilising multiple character printing (commented out below)

// 1. Utilising for-loops

int main(void)
{
    int n;

    // checking the inputs to be between 1 and 8
    do
    {
        n = get_int("How tall do you want the pyramid to be (1-8)? \n");
    }
    while (n < 1 || n > 8);

    // printing the towers
    for (int j = 1; j < n + 1; j++)
    {
        // printing the first block of spaces
        for (int i = 1; i < n - j + 1; i++)
        {
            printf(" ");
        }

        // printing the first block of hashes
        for (int k = 1; k < j + 1; k++)
        {
            printf("#");
        }

        // printing the two spaces beween the first and second tower
        printf("  ");

        // printing the second tower rows
        for (int k = 1; k < j + 1; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}

/* 2. Utilising multiple character print
int main(void)
{
    int n;
    do
    {
        n = get_int("How tall do you want the pyramid to be (1-8)? \n");
    }
    while(n < 1 || n > 8);

    int i = 1;

    // printing the tower, one row after another
    while (i <= n)
    {
        printf("%.*s",n-i,"       ");
        printf("%.*s",i,"########");
        printf("%.*s",2,"  ");
        printf("%.*s\n",i,"########");
        i++;
    }
}*/