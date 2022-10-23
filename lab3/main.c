#include <stdio.h>
#include <string.h>
#include <ctype.h>


int my_printf(char *format_string, char *param){
	int format_string_length = strlen(format_string);

	for(int i=0;i<format_string_length;i++){
		if((format_string[i] == '#') && (format_string[i+1] == 'k')){
				for(int j=0;j<strlen(format_string);j++){
					if(isalpha(format_string[j])!=0){
						if(isupper(format_string[j])>0){
							format_string[j] = tolower(format_string[j]);
						}else
							format_string[j] = toupper(format_string[j]);
					}
				}
			i++;
			printf("%s",param);
		}else
			putchar(format_string[i]);

	}

	puts("");
	return 0;	
}		
	
	


int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}
