// gcc signIn.c -O0 -fstack-protector -no-pie -o signIn

#include <stdio.h>
#include <string.h>

void init() {
  /* this disabled stream buffering. 
   * You can safely ignore this function as there is no vuln in here */
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void print_secret() { //Print flag: Nothing to exploit here
  char fp;
   FILE* fd = fopen("flag", "r");
  printf("The Flag is: \n\n");
  while((fp = fgetc(fd)) != EOF)
       printf("%c", fp);

   fclose(fd);
 }


int main(void) {
	char username[5] = {0};
	char privateUsername[5] = {0};
	char password[5] ={0};
	char privatePassword[5] = {0};
	int attempts = 3;
	init();
	while(attempts) {
		printf("Username:\n");
		scanf("%s", username);
		printf("Password:\n");
		scanf("%s", password);
		
		int authUsername = 0;
		int authPW = 0;
		if(strcmp(username, privateUsername) == 0) {
			authUsername = 1;
			if(strcmp(password, privatePassword) == 0) {
				authPW = 1;
			}
		}

		if(authUsername && authPW) {
			printf("\nn Welcome! \n");
			print_secret();
			return 0;
		} else {
			attempts--;
			printf("Please check your username or password again!\n");
		}

	}
	return 0;
}


