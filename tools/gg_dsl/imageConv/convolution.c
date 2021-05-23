#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <math.h>
#include <unistd.h>

#define IMAGE_DIM 300
#define KERNEL_SZ 5 

void print_matrix(float *m, int dim) {
  
  for (int i = 0; i < dim; i++) {
    for (int j = 0; j < dim; j++) {
      printf("%3.3f  ", m[i*dim+j]); 
    }
    printf("\n");
  }

}

void write_matrix(float *m, int dim, FILE *fp) {
  for (int i = 0; i < dim; i++) {
    for (int j = 0; j < dim; j++) {
      fprintf(fp, "%3.3f  ", m[i*dim+j]);
    }
    fprintf(fp, "\n");
  }
}

int main(int argc, char **argv) {

  if (argc != 4) {
    printf("Usage: ./convolution <path-to-txt-files> <file-name.txt> <output-name.out>\n");
    exit(0);
  }

  // ======== Read txt file and form an array ========
  FILE *fp = NULL;
  FILE *rp = NULL;

  if (chdir(argv[1]) != 0) 
    perror("convolution: chdir() failed");

  fp = fopen(argv[2], "r");

  float *arr = (float *) malloc(sizeof(float) * IMAGE_DIM * IMAGE_DIM);

  int i=0;
  float num;
  while(fscanf(fp, "%f", &num) > 0) {
    arr[i] = num;
    i++;
  }
  //print_matrix(arr, IMAGE_DIM);

  // ======== Convolution ========
  srand((unsigned)time(NULL));
  float *kernel = (float *) malloc(sizeof(float) * KERNEL_SZ * KERNEL_SZ);
  for (int i = 0; i < KERNEL_SZ*KERNEL_SZ; i++) {
    kernel[i] = (float)rand()/RAND_MAX;
  }
  float *result = (float *) malloc(sizeof(float) * (IMAGE_DIM-KERNEL_SZ+1) * (IMAGE_DIM-KERNEL_SZ+1));

  float tmp;
  for (int i = 0; i <= IMAGE_DIM-KERNEL_SZ; i++) {
    for (int j = 0; j <= IMAGE_DIM-KERNEL_SZ; j++) {
       
      tmp = 0.0;
      for (int ki = 0; ki < KERNEL_SZ; ki++) {
	      for (int kj = 0; kj < KERNEL_SZ; kj++) {
          tmp += arr[i*IMAGE_DIM+j+ki*IMAGE_DIM+kj] * kernel[ki*KERNEL_SZ+kj];
      	} // end of kj 
      } // end of ki
      result[i*(IMAGE_DIM-KERNEL_SZ+1)+j] = tmp; 

    } // end of j
  } // end of i

  //printf("======== Result ======== \n");
  //print_matrix(result, IMAGE_DIM-KERNEL_SZ+1);
  rp = fopen(argv[3], "w");
  write_matrix(result, IMAGE_DIM-KERNEL_SZ+1, rp);
  


  free(arr);
  free(kernel);
  free(result);
  fclose(fp);
  fclose(rp);

  return 0;
}
