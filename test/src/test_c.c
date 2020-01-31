#include <stdio.h>

void show_version(int output) {
    if (output == 0) {
        // this won't be executed, but written for test of coverage
        return;
    }
    printf("Version of gcc: %d.%d.%d", __GNUC__, __GNUC_MINOR__,
        __GNUC_PATCHLEVEL__);
}

int main() {
    show_version(1);
    return 0;
}
