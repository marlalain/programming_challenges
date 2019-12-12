// TODO Pipe
// TODO Use $PATH

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
  int prompt = 1;
  char *user;
  user = getenv("USER");
  char *pwd;
  pwd = getenv("PWD");
  pid_t pid = fork();
  // char *path;
  // path = getenv("PATH");
  char program[80];

  while (1) {
    if (prompt == 1) {
      printf("%s $ ", user);
      scanf("%s", program);
      prompt = 0;
    }
    if (pid == 0) {
      static char *argv[] = {program, "", NULL};
      execv("/bin/sh", argv);
      exit(127);
    } else {
      waitpid(pid, 0, 0);
    }
  }

  return 0;
}
