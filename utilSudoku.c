#include <stdlib.h>
#include <stdio.h>
#include <string.h>
         
     
int lireSudoku(FILE *fich,int sudoku[9][9])
{int i,j,res;
 int val; 
 for (i=0; i<9; i++) 
   for (j=0; j<9; j++) 
     {
       res=fscanf(fich, "%d",&val);
       if (res==EOF)
         {
           fprintf(stderr,"Fin de ficher atteinte: manque des coefficients\n");
           exit(-1);
         }
       sudoku[i][j]=val;
     }
 return(0);
}

int ecrireSudoku(FILE *fich,int sudoku[9][9])
{int i,j;
 for (i=0; i<9; i++) 
   {
     for (j=0; j<9; j++) 
       {
         fprintf(fich, "%d ",sudoku[i][j]);
       }
     fprintf(fich, "\n");
   }
 return(0);
}

int sudokuValide(int sudoku[9][9])
{
	int li,col,num,countCol,countLi;
	for (li=0; li<9; li++)
	{
		for(num=1; num<10; num++)
		{
			countCol=0;
			countLi=0;
			for(col=0; col<9; col++)
			{
				if(sudoku[li][col]==num)
				{
					countCol++;
				}
				if(sudoku[col][li]==num)
				{
					countLi++;
				}
			}
			if(countCol!=1) return(0);
			if(countLi !=1) return(0);
		}
	}

	//pour les cases maintenant
	int count1,count2,count3,count4,count5,count6,count7,count8,count9;
	for (num=1; num<10; num++)
	{
		count1=0;
		count2=0;
		count3=0;
		count4=0;
		count5=0;
		count6=0;
		count7=0;
		count8=0;
		count9=0;
		for(li=0; li<3; li++)
		{
			for(col=0; col<3; col++)
			{
				if(sudoku[li][col]==num) count1++;
				if(sudoku[li][col+3]==num) count2++;
				if(sudoku[li][col+6]==num) count3++;
				if(sudoku[li+3][col]==num) count4++;
				if(sudoku[li+3][col+3]==num) count5++;
				if(sudoku[li+3][col+6]==num) count6++;
				if(sudoku[li+6][col]==num) count7++;
				if(sudoku[li+6][col+3]==num) count8++;
				if(sudoku[li+6][col+6]==num) count9++;
			}
		}
		if(count1 != 1) return(0);
		if(count2 != 1) return(0);
		if(count3 != 1) return(0);
		if(count4 != 1) return(0);
		if(count5 != 1) return(0);
		if(count6 != 1) return(0);
		if(count7 != 1) return(0);
		if(count8 != 1) return(0);
		if(count9 != 1) return(0);
	}
	return(1);
}

int sudokuSimple(int sudoku[9][9])
{
	int M[9][9][9]={0};//il faut tout instancier à 0
	int li,col,i,k;
	int somme=0;
	int valeur;
	int change=1;	
	
	while(change==1)
	{
		change=0;
		for (li=0; li<9; li++)
		{
			for(col=0; col<9; col++)
			{
				if(sudoku[li][col] !=0)
				{
					k=sudoku[li][col]-1;
					for(i=0; i<9; i++)
					{
						M[i][col][k]=1;
						M[li][i][k]=1;
						M[(li/3)*3+i/3][(col/3)*3+i%3][k]=1;
					}
				}
			}
		}
		//
		
		//on cherche chaque case vide si il y a un seul k

		for (li=0; li<9; li++)
		{
			for(col=0; col<9; col++)
			{
				if(sudoku[li][col]==0)
				{
					somme=0;
					for(k=0; k<9; k++)
					{ 
						somme += M[li][col][k];
						if(M[li][col][k]==0) valeur=k+1;
						
					}
					if(somme==8)
					{
						sudoku[li][col]=valeur;
						change=1;
					}
				}
			}
		}
		if(change==0) return(0);
	}
	return(1);	
}

