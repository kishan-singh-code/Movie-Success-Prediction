#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
void conv(long int,int);
void poi(int q,int a,char str[]);
int main()
{int q,w,e,t,y,u,i,g;

  long int r=0;
  char str[30];
  printf("Enter the base: ");
  scanf("%d",&q);
  printf("Enter the number : ");
  scanf("%s",str);
  g=strlen(str);
 
 for(i=0;i<g;i++)
  {if(str[i]<58)
  {if((str[i]-48)>(q-1))
  {printf("Bosdk number teek se dal gandu madrchod\n");
   exit(0);}}
   if(str[i]>64)
   {if((str[i]-55)>(q-1))
   {printf("dubara num dal bosdk\n");
   exit(0);}}}
  for(e=0;str[e]!=46&&str[e]!='\0';e++)
   {}
  w=y=e-1;
  for(i=0;i<=y;i++,w--)
  { if(str[i]<58)
 {r=(pow(q,w))*(str[i]-48)+r;}
  if(str[i]>64)
  {r=(pow(q,w))*(str[i]-55)+r;}}
  printf("Enter the base you want to convert: ");
 scanf("%d",&u);
  conv(r,u);
  poi(q,u,str);
  printf("\n");
     return 0;}

  void conv(long int q,int w)
  { int i=0,f,rem;
    char a[100];
    while(q>0)
    { rem=q%w;
      q=q/w;
      if(rem>9 && rem <35)
     {a[i++]=rem-10+'A';}
       else
      { a[i++]=rem+'0';}}
   printf("The no. is : ");
   for(f=i-1;f>=0;f--)
   {printf("%c",a[f]); }
  }

  void poi(int q,int a,char str[])
 { int w,u,e,p,o,s;
    long double t=0,y=1,r;
    w=strlen(str);
   for(e=0;str[e]!=46;e++)
   {}
   for(p=e+1;p<w;p++)
   {if(str[p]<58) 
  {t= ((str[p]-48)/(pow(q,y)))+t ;}
    if(str[p]>64)
  {t=((str[p]-55)/(pow(q,y)))+t;}
     y++;}
    printf(".");
     for(w=0;w<5;w++)
     { e=t*a;
       r=t*a;
       t=r-e;
  
     if(e>9&&e<36)
   { e=55+e;
     printf("%c",e);
     s=e;}
   if(e<10)
     {  printf("%d",e);}}
 }

  


