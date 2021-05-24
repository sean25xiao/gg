#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define NUM_FILE 5
#define IMAGE_DIM 3840

int main(int argc, char **argv) {

  if (argc != 2) {
    printf("Please input the path to store the .csv files\n");
    exit(0);
  }

  FILE *fp = NULL;
  float val;

  srand((unsigned)time(NULL));

  if (chdir(argv[1]) != 0) 
    perror("chdir() failed");

  for (int i = 0; i < NUM_FILE; i++) {

    char buffer[32];
    snprintf(buffer, sizeof(char) * 32, "image%i.txt", i);

    fp = fopen(buffer, "w");
    for (int n = 0; n < IMAGE_DIM * IMAGE_DIM; n++) {
      val = (float)rand()/RAND_MAX;
      fprintf(fp, "%3.3f  ", val);
    }
    fclose(fp);
    printf("image%d.txt has been prepared \n", i);
  }

}
