#include <iostream>

void show_version(bool output) {
    if (!output) {
        // this won't be executed, but written for test of coverage
        return;
    }
    std::cout << "Version of g++: " << __GNUC__ << "." << __GNUC_MINOR__ << "."
              << __GNUC_PATCHLEVEL__ << std::endl;
}

int main() {
    show_version(true);
    return 0;
}
