#include <stdio.h>
int main()
{
	int opt1,opt2,opt3;
	float ans = 0;
	float prices[] = {10000.0,7000.0,6000.0};
	int discount  = 0;
    scanf("%d", &opt1);
    scanf("%d", &opt2);
    if(opt1>3 || opt1 <1)
    {
        printf("INVALID INPUT");
        return 0;
	}
	opt1 = opt1-1;
	if(opt2==1)
	{
    scanf("%d", &opt3);
		if(opt3==0)
		{
			ans  = prices[opt1]*98/100;
    		printf("%0.1f", ans);
    		printf(" INR");
        	return 0;
		}
		else if(opt3==1)
		{
			ans  = prices[opt1]*80/100;
    		printf("%0.1f", ans);
    		printf(" INR");
        	return 0;
			
		}
		else{
        	printf("INVALID INPUT");
        	return 0;
	}
	
		
	}
	else if(opt2==0){
	ans  = prices[opt1];
    printf("%0.1f", ans);
    printf(" INR");
    return 0;
	}
	else{
        printf("INVALID INPUT");
        return 0;
	}
    
    return 0;
	}
