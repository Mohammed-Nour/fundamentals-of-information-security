#include <stdio.h>
#include<stdlib.h>
#include <string.h>
#include<unistd.h>

void start_level() {
  char buffer[64];
  gets(buffer);
}

int main(int argc, char **argv) {
  start_level();
  return 0;
}