// TODO Pipe
// TODO Use $PATH

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main() {
  char *user;
  user = getenv("USER");
  char *pwd;
  pwd = getenv("PWD");
  pid_t pid = fork();
  // char *path;
  // path = getenv("PATH");
  char program[80];

  if (pid == 0) {
    static char *argv[] = {"echo", "Hello World", NULL};
    execv("/bin/echo", argv);
    exit(127);
  } else {
    waitpid(pid, 0, 0);
  }
  return 0;
}
