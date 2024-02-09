#include <base.h>

void kernel_main()
{
		Bitmap *bmp;
		char *d;	   
		int n=0;	   
		int x=100;
		int y=100;
		unsigned char* addr;
		cls();
		NULL=0;
		
		memoryStart = (unsigned char *)0x200000;
		for (n=0;n<150;n=n+8)   
			hline(0,n,319,0);
		for (n=0;n<300;n=n+8)   
			vline(n,0,199,0);
		box(150,75,175,100,0);	   	
				
		bmp=createBitmap(x,y);
		bmp->data=getStringFromLowMemory();
		//memReplace(bmp->data,0,1,10000);
		
		pbitmap(3,3,bmp) ;

			  
	
	
}


