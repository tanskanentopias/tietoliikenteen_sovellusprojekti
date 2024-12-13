#include <zephyr/kernel.h>
#include <math.h>
#include "confusion.h"
#include "adc.h"
#include "keskipisteet.h"

/* 
  K-means algorithm should provide 6 center points with
  3 values x,y,z. Let's test measurement system with known
  center points. I.e. x,y,z are supposed to have only values
  1 = down and 2 = up
  
  CP matrix is thus the 6 center points got from K-means algoritm
  teaching process. This should actually come from include file like
  #include "KmeansCenterPoints.h"
  
  And measurements matrix is just fake matrix for testing purpose
  actual measurements are taken from ADC when accelerator is connected.
*/ 

/*int CP[6][3]={
    {1800,1500,1500},
    {1200,1500,1500},
    {1500,1800,1500},
    {1500,1200,1500},
    {1500,1500,1800},
    {1500,1500,1200}
};*/

int measurements[6][3]={
    {1791,1505,1505},
    {1182,1498,1498},
    {1487,1798,1497},
    {1502,1208,1502},
    {1487,1487,1786},
    {1518,1518,1226}
};
/*
int CP[6][3]={
    {1,0,0},
    {2,0,0},
    {0,1,0},
    {0,2,0},
    {0,0,1},
    {0,0,2}
};


int measurements[6][3]={
    {1,0,0},
    {2,0,0},
    {0,1,0},
    {0,2,0},
    {0,0,1},
    {0,0,2}
};*/


int CM[6][6]= {0};


void printConfusionMatrix(void)
{
    printk("Confusion matrix = \n");
    printk("   cp1 cp2 cp3 cp4 cp5 cp6\n");
    for (int i = 0; i < 6; i++)
    {
    printk("cp%d %d   %d   %d   %d   %d   %d\n", i+1, CM[i][0], CM[i][1], CM[i][2], CM[i][3], CM[i][4], CM[i][5]);
    }
}

void makeHundredFakeClassifications(void)
{
    for(int i=0; i < 6; i++)
    {
    int closestIndex = calculateDistanceToAllCentrePointsAndSelectWinner(measurements[i][0], measurements[i][1], measurements[i][2]);
    CM[i][closestIndex]++;
    }
}

void makeOneClassificationAndUpdateConfusionMatrix(int direction)
{
    
    struct Measurement m = readADCValue();
    int voittaja = calculateDistanceToAllCentrePointsAndSelectWinner(m.x, m.y, m.z);
    printk("voittaja: %d\n", direction);
    CM[direction][voittaja] = CM[direction][voittaja] + 1;
}
    


int calculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
   
   int closestIndex = 0; 
   float minDistance = INFINITY; 

   for (int i = 0; i < 6; i++) {
        int distance = sqrt(pow(x - CP[i][0], 2) + pow(y - CP[i][1], 2) + pow(z - CP[i][2], 2));

        //printk("Keskipiste %d etaisyys: %d\n", i, distance);

        if (distance < minDistance) {
            minDistance = distance;
            closestIndex = i;
        }
   }

    //printk("Lahin keskipiste: %d, Etaisyys: %d\n", closestIndex, minDistance);
    return closestIndex;
}

void resetConfusionMatrix(void)
{
	for(int i=0;i<6;i++)
	{ 
		for(int j = 0;j<6;j++)
		{
			CM[i][j]=0;
		}
	}
}

