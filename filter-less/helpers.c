#include "helpers.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// BITMAPFILEHEADER 14 bytes long (1 byte equals 8 bits)

// BITMAPINFOHEADER 40 bytes long

// BMP stores triplets backwards : BGR (8 bits each)

// Convert image to grayscale
// 0x00 - Black
// 0xff - White

// image height many rows, and width many RGBTRIPLEs
int minval(int a, int b);

int minval(int a, int b)
{
    if (a > b)
    {
        return b;
    }
    return a;
}

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int sum;
    int avg;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sum = image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen;
            avg = round(sum / 3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int originalRed;
    int originalGreen;
    int originalBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            originalRed = image[i][j].rgbtRed;
            originalGreen = image[i][j].rgbtGreen;
            originalBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = minval(round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue), 255);
            image[i][j].rgbtGreen = minval(round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue), 255);
            image[i][j].rgbtBlue = minval(round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue), 255);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE holder;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2.00; j++)
        {
            holder = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = holder;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy of the original image to have original color values

    RGBTRIPLE og_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            og_image[i][j] = image[i][j];
        }
    }

    // now we are going pixel by pixel in the
    // image to change it
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int counter = 0;
            float sum_Red = 0;
            float sum_Blue = 0;
            float sum_Green = 0;

            // sum all 3x3 blocks for every pixel
            // but if the i and j indices are non existent, skip
            for (int vertical_shift = -1; vertical_shift < 2; vertical_shift++)
            {
                for (int horiz_shift = -1; horiz_shift < 2; horiz_shift++)
                {
                    if (i + vertical_shift < 0 || i + vertical_shift >= height)
                    {
                        int dummy = 0;
                    }
                    else if (j + horiz_shift < 0 || j + horiz_shift >= width)
                    {
                        int dummy = 0;
                    }
                    else
                    {
                        sum_Red += og_image[i + vertical_shift][j + horiz_shift].rgbtRed;
                        sum_Blue += og_image[i + vertical_shift][j + horiz_shift].rgbtBlue;
                        sum_Green += og_image[i + vertical_shift][j + horiz_shift].rgbtGreen;
                        counter++;
                    }
                }
            }
            
            // Average
            image[i][j].rgbtRed = round(sum_Red / counter);
            image[i][j].rgbtBlue = round(sum_Blue / counter);
            image[i][j].rgbtGreen = round(sum_Green / counter);
        }
    }
    return;
}